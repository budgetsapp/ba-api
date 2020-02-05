import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Category as CategoryModel


class CategoryType(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel
        interfaces = (relay.Node, )


class CategoryConnection(relay.Connection):
    class Meta:
        node = CategoryType


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_categories = SQLAlchemyConnectionField(CategoryConnection)

    category = graphene.Field(CategoryType, category_id=graphene.String())

    def resolve_category(self, info, category_id):
        query = CategoryType.get_query(info)
        return query.filter(CategoryModel.category_id == category_id).first()


schema = graphene.Schema(query=Query)
