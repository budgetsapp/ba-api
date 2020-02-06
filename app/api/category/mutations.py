from graphql import GraphQLError
import graphene
from flask_jwt_extended import jwt_required, get_jwt_claims

from .types import CategoryType
from app.services import category as category_service


class CreateCategoryMutation(graphene.Mutation):
    class Arguments:
        display_name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @jwt_required
    def mutate(self, info, display_name):
        claims = get_jwt_claims()
        user_id = claims['id']

        category = category_service.create_category(user_id, display_name)
        # Notice we return an instance of this mutation
        return CreateCategoryMutation(category=category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()
