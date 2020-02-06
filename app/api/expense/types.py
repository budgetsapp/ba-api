import graphene

import app.api.category.types as CategoryTypes


class ExpenseType(graphene.ObjectType):
    class Meta:
        description = 'An expense'

    id = graphene.UUID()
    user_id = graphene.UUID()
    amount = graphene.Float()
    description = graphene.String()
    created_at = graphene.DateTime()
    category = graphene.Field(lambda: CategoryTypes.CategoryType)

    def resolve_id(parent, info):
        return parent.expense_id

    def resolve_user_id(parent, info):
        return parent.user_id

    def resolve_amount(parent, info):
        return parent.amount

    def resolve_description(parent, info):
        return parent.description

    def resolve_created_at(parent, info):
        return parent.created_at

    def resolve_category(parent, info):
        return parent.category
