import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_claims

from app.models import Expense as ExpenseModel


class ExpenseType(SQLAlchemyObjectType):
    class Meta:
        model = ExpenseModel


class Query(graphene.ObjectType):
    my_expenses = graphene.List(
        ExpenseType, page=graphene.Int(), page_size=graphene.Int())

    @jwt_required
    def resolve_my_expenses(self, info, page, page_size):
        claims = get_jwt_claims()
        user_id = claims['id']

        offset = page * page_size
        expense_query = ExpenseType.get_query(info)
        return expense_query.filter_by(user_id=user_id).offset(offset).limit(page_size)


schema = graphene.Schema(query=Query)
