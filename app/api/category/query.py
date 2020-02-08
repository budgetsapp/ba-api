from sqlalchemy import func
from graphql import GraphQLError
import graphene
from flask_jwt_extended import jwt_required, get_jwt_claims

from .types import CategoryType
from app.models import Category as CategoryModel
from app.extensions import db


class Query(graphene.ObjectType):
    my_categories = graphene.List(
        CategoryType, first=graphene.Int(), offset=graphene.Int())
    search_my_categories = graphene.List(
        CategoryType, query=graphene.String())
    category = graphene.Field(CategoryType, id=graphene.ID())
    my_categories_total = graphene.Int()

    @jwt_required
    def resolve_my_categories(self, info, first, offset):
        claims = get_jwt_claims()
        user_id = claims['id']

        return db.session.query(CategoryModel).filter_by(user_id=user_id).offset(offset).limit(first)

    @jwt_required
    def resolve_search_my_categories(self, info, query):
        claims = get_jwt_claims()
        user_id = claims['id']
        LIMIT = 100

        return db.session.query(CategoryModel).filter_by(user_id=user_id).filter(func.lower(CategoryModel.display_name).contains(func.lower(query))).limit(LIMIT)

    @jwt_required
    def resolve_my_categories_total(self, info):
        claims = get_jwt_claims()
        user_id = claims['id']

        return db.session.query(CategoryModel).filter_by(user_id=user_id).count()

    @jwt_required
    def resolve_category(self, info, id):
        claims = get_jwt_claims()
        user_id = claims['id']

        category = db.session.query(CategoryModel).filter_by(
            category_id=id).first()
        if not category:
            raise GraphQLError('No item found')
        elif not category.user_id == user_id:
            raise GraphQLError('Not authorized')
        else:
            return category
