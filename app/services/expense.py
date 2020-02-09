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


def get_expenses_by_category(category_id, first, offset):
    # TODO: how to get expenses from CategoryModel? It raises an error
    # db.session.query(CategoryModel.expenses).offset(offset).limit(first)
    return db.session.query(ExpenseModel).filter_by(category_id=category_id).offset(offset).limit(first)


def get_expenses_total_by_category(category_id):
    return db.session.query(ExpenseModel).filter_by(category_id=category_id).count()


def get_expense_by_id(expense_id):
    return db.session.query(ExpenseModel).filter_by(
        expense_id=expense_id).first()


def delete_expense(expense_id):
    db.session.query(ExpenseModel).filter_by(expense_id=expense_id).delete()
    db.session.commit()
