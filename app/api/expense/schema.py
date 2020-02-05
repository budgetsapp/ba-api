import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Expense as ExpenseModel


class ExpenseType(SQLAlchemyObjectType):
    class Meta:
        model = ExpenseModel
        interfaces = (relay.Node, )


class ExpensesConnection(relay.Connection):
    class Meta:
        node = ExpenseType


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_expenses = SQLAlchemyConnectionField(ExpensesConnection)


schema = graphene.Schema(query=Query)
