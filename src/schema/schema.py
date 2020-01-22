from graphene import Schema
from .user import Query as UserQuery


schema = Schema(query=UserQuery)
