import graphene
from .category.schema import Query as CategoryQuery
from .expense.schema import Query as ExpenseQuery


class Query(
        ExpenseQuery,
        CategoryQuery,
        # NOTE: end with this one
        graphene.ObjectType):
    pass


# class Mutation(
#         # NOTE: end with this one
#         graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)  # , mutation=Mutation)
