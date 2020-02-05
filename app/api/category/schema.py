import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Category as CategoryModel, Expense as ExpenseModel


class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (relay.Node, )


class CategoryConnection(relay.Connection):
    class Meta:
        node = Category


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_categories = SQLAlchemyConnectionField(CategoryConnection)


schema = graphene.Schema(query=Query)
