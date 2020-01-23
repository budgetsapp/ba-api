from sqlalchemy import Column, String
from app.db import db


class Category(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    user_id = db.Column(db.String(36))
    name = db.Column(db.String(20))

    def __repr__(self):
        return "<Category(id='%s', name='%s', user_id='%s')>" % (self.id, self.name, self.user_id)
