import graphene

from app.models import Category as CategoryModel
from app.models import Expense as ExpenseModel
from app.extensions import db
import app.api.expense.types as ExpenseTypes
from app.services import expense as expense_category


class CategoryType(graphene.ObjectType):
    class Meta:
        description = 'A category'

    id = graphene.ID()
    user_id = graphene.ID()
    created_at = graphene.DateTime()
    display_name = graphene.String()
    expenses = graphene.List(
        lambda: ExpenseTypes.ExpenseType, first=graphene.Int(), offset=graphene.Int())
    expenses_total = graphene.Int()

    def resolve_id(parent, info):
        return parent.category_id

    def resolve_user_id(parent, info):
        return parent.user_id

    def resolve_created_at(parent, info):
        return parent.created_at

    def resolve_display_name(parent, info):
        return parent.display_name

    def resolve_expenses(parent, info, first, offset):
        return expense_category.get_expenses_by_category(parent.category_id, first, offset)

    def resolve_expenses_total(parent, info):
        return expense_category.get_expenses_total_by_category(parent.category_id)
