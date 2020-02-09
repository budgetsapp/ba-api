from graphql import GraphQLError
import graphene
from flask_jwt_extended import jwt_required, get_jwt_claims

from .types import ExpenseType
from app.services import expense as expense_service


class CreateExpenseMutation(graphene.Mutation):
    class Arguments:
        category_id = graphene.ID(required=True)
        amount = graphene.Float(required=True)
        description = graphene.String()

    # The class attributes define the response of the mutation
    expense = graphene.Field(ExpenseType)

    @jwt_required
    def mutate(self, info, category_id, amount, description=""):
        claims = get_jwt_claims()
        user_id = claims['id']

        expense = expense_service.create_expense(
            user_id, category_id, amount, description)
        # Notice we return an instance of this mutation
        return CreateExpenseMutation(expense=expense)


class DeleteExpenseMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    # The class attributes define the response of the mutation
    expense = graphene.Field(ExpenseType)

    @jwt_required
    def mutate(self, info, id):
        claims = get_jwt_claims()
        user_id = claims['id']

        expense = expense_service.get_expense_by_id(id)

        if not expense:
            raise GraphQLError('No item found')
        elif not expense.user_id == user_id:
            raise GraphQLError('Not authorized')
        else:
            expense_service.delete_expense(id)
            return DeleteExpenseMutation(expense=expense)


class Mutation(graphene.ObjectType):
    create_expense = CreateExpenseMutation.Field()
    delete_expense = DeleteExpenseMutation.Field()
