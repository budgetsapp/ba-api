from graphql import GraphQLError
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims

from ..expense.schema import ExpenseType
from app.models import Category as CategoryModel
from app.extensions import db
# Example: https://github.com/graphql-python/graphene/issues/592


class CategoryType(graphene.ObjectType):
    class Meta:
        description = 'A category'

    id = graphene.UUID()
    user_id = graphene.UUID()
    created_at = graphene.DateTime()
    display_name = graphene.String()
    expenses = graphene.List(
        ExpenseType, page=graphene.Int(), page_size=graphene.Int())

    def resolve_id(parent, info):
        return parent.category_id

    def resolve_user_id(parent, info):
        return parent.user_id

    def resolve_created_at(parent, info):
        return parent.created_at

    def resolve_display_name(parent, info):
        return parent.display_name

    def resolve_expenses(parent, info, page, page_size):
        offset = page * page_size
        return db.session.query(CategoryModel.expenses).offset(offset).limit(page_size)


class Query(graphene.ObjectType):
    my_categories = graphene.List(
        CategoryType, page=graphene.Int(), page_size=graphene.Int())
    category = graphene.Field(CategoryType, category_id=graphene.String())

    @jwt_required
    def resolve_my_categories(self, info, page, page_size):
        claims = get_jwt_claims()
        user_id = claims['id']

        offset = page * page_size
        return db.session.query(CategoryModel).filter_by(user_id=user_id).offset(offset).limit(page_size)

    @jwt_required
    def resolve_category(self, info, category_id):
        claims = get_jwt_claims()
        user_id = claims['id']

        category = db.session.query(CategoryModel).filter_by(
            category_id=category_id).first()
        if not category:
            raise GraphQLError('No item found')
        elif not category.user_id == user_id:
            raise GraphQLError('Not authorized')
        else:
            return category


schema = graphene.Schema(query=Query)
