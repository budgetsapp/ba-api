import graphene
from .category import Query as CategoryQuery, Mutation as CategoryMutation
from .expense.schema import Query as ExpenseQuery


class Query(
        ExpenseQuery,
        CategoryQuery,
        # NOTE: end with this one
        graphene.ObjectType):
    pass


class Mutation(
        CategoryMutation,
        # NOTE: end with this one
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
