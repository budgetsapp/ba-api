import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from app.models import Category as CategoryModel


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

    get_category = graphene.Field(Category, category_id=graphene.String())

    def resolve_get_category(self, info, category_id):
        query = Category.get_query(info)
        return query.filter(CategoryModel.id == category_id).first()


schema = graphene.Schema(query=Query)
