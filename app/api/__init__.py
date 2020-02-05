import graphene
from .category.schema import Query as CategoryQuery


class Query(
        CategoryQuery,
        # NOTE: end with this one
        graphene.ObjectType):
    pass


# class Mutation(
#         # NOTE: end with this one
#         graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)  # , mutation=Mutation)
