import graphene
from .category import Query as CategoryQuery, Mutation as CategoryMutation
from .expense import Query as ExpenseQuery, Mutation as ExpenseMutation


class Query(
        ExpenseQuery,
        CategoryQuery,
        # end with this one
        graphene.ObjectType):
    pass


class Mutation(
        ExpenseMutation,
        CategoryMutation,
        # end with this one
        graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
