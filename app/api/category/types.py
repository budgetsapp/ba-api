import graphene

from app.models import Category as CategoryModel
from app.extensions import db
import app.api.expense.types as ExpenseTypes


class CategoryType(graphene.ObjectType):
    class Meta:
        description = 'A category'

    id = graphene.UUID()
    user_id = graphene.UUID()
    created_at = graphene.DateTime()
    display_name = graphene.String()
    expenses = graphene.List(
        lambda: ExpenseTypes.ExpenseType, first=graphene.Int(), offset=graphene.Int())

    def resolve_id(parent, info):
        return parent.category_id

    def resolve_user_id(parent, info):
        return parent.user_id

    def resolve_created_at(parent, info):
        return parent.created_at

    def resolve_display_name(parent, info):
        return parent.display_name

    def resolve_expenses(parent, info, first, offset):
        return db.session.query(CategoryModel.expenses).offset(offset).limit(first)
