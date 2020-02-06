import uuid
from datetime import datetime
from app.models import Category as CategoryModel
from app.extensions import db


def create_category(user_id, display_name):
    category = CategoryModel(category_id=str(uuid.uuid4()),
                             display_name=display_name,
                             created_at=datetime.utcnow(),
                             user_id=user_id)
    db.session.add(category)
    db.session.commit()
    return category
