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


class CategoryInput(graphene.InputObjectType):
    displayName = graphene.String(required=False)


class EditCategoryMutation(graphene.Mutation):
    class Arguments:
        category_input = CategoryInput(required=True)
        id = graphene.ID(required=True)

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @jwt_required
    def mutate(self, info, id, category_input=None):
        claims = get_jwt_claims()
        user_id = claims['id']

        category = category_service.get_category_by_id(id)

        if not category.user_id == user_id:
            raise GraphQLError('Not authorized')
        else:
            edited_category = category_service.edit_category(
                category, category_input)
            return CreateCategoryMutation(category=edited_category)


class DeleteCategoryMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    # The class attributes define the response of the mutation
    category = graphene.Field(CategoryType)

    @jwt_required
    def mutate(self, info, id):
        claims = get_jwt_claims()
        user_id = claims['id']

        category = category_service.get_category_by_id(id)

        if not category:
            raise GraphQLError('No item found')
        elif not category.user_id == user_id:
            raise GraphQLError('Not authorized')
        else:
            category_service.delete_category(id)
            return CreateCategoryMutation(category=category)


class Mutation(graphene.ObjectType):
    create_category = CreateCategoryMutation.Field()
    edit_category = EditCategoryMutation.Field()
    delete_category = DeleteCategoryMutation.Field()
