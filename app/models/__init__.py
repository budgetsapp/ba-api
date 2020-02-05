from sqlalchemy import func
from app.extensions import db


class Category(db.Model):
    category_id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), nullable=False)
    display_name = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return "<Category(id='%s', display_name='%s', user_id='%s')>" % (self.category_id, self.display_name, self.user_id)


class Expense(db.Model):
    expense_id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36), nullable=False)
    amount = db.Column(db.Float(), nullable=False)
    description = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=func.now())
    category_id = db.Column(
        db.String(36), db.ForeignKey("category.category_id"))
    category = db.relationship(Category, backref=db.backref('expenses'))
