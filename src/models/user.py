from sqlalchemy import (Column, String)

from .base import Base


class User(Base):
    __tablename__ = 'department'
    id = Column(String, primary_key=True)
    display_name = Column(String)
    email = Column(String)
