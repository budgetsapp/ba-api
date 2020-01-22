from sqlalchemy import create_engine
from sqlalchemy.orm import (
    scoped_session, sessionmaker, relationship, backref)
from sqlalchemy.ext.declarative import declarative_base

db_path = 'sqlite:///database.sqlite3'

engine = create_engine(db_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(
    autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

Base.query = db_session.query_property()
