import uuid
from datetime import datetime
from app.models import Expense as ExpenseModel, Category as CategoryModel
from app.services import category as category_service
from app.extensions import db


def create_expense(user_id, category_id, amount, description):
    category = category_service.get_category_by_id(category_id)
    expense = ExpenseModel(
        expense_id=str(uuid.uuid4()),
        user_id=user_id,
        amount=amount,
        description=description,
        created_at=datetime.utcnow(),
    )
    category.expenses.append(expense)
    db.session.add(category)
    db.session.commit()
    return expense
