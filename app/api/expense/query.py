import graphene
from flask_jwt_extended import jwt_required, get_jwt_claims

from app.models import Expense as ExpenseModel
from .types import ExpenseType
from app.extensions import db


class Query(graphene.ObjectType):
    my_expenses = graphene.List(
        ExpenseType, first=graphene.Int(), offset=graphene.Int())
    my_expenses_total = graphene.Int()

    @jwt_required
    def resolve_my_expenses(self, info, first, offset):
        claims = get_jwt_claims()
        user_id = claims['id']

        return db.session.query(ExpenseModel).filter_by(user_id=user_id).offset(offset).limit(first)

    @jwt_required
    def resolve_my_expenses_total(self, info):
        claims = get_jwt_claims()
        user_id = claims['id']

        return db.session.query(ExpenseModel).filter_by(user_id=user_id).count()
