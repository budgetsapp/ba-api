from graphene import (relay, ObjectType)
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from ..models.user import (User as UserModel)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interfaces = (relay.Node, )


class UserConnection(relay.Connection):
    class Meta:
        node = User


class Query(ObjectType):
    node = relay.Node.Field()
    all_users = SQLAlchemyConnectionField(UserConnection)
