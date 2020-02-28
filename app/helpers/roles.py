from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims
from graphql import GraphQLError


def roles_required(needRoles=[]):
    def roles_required(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            user_id = claims['id']
            userRoles = claims['roles']
            inter = list(set(userRoles) & set(needRoles))
            if len(inter) > 0:
                resolved_kwargs = {**kwargs, "user_id": user_id}
                return fn(*args, **resolved_kwargs)
            else:
                raise GraphQLError('No permissions')
        return wrapper
    return roles_required


admin_only = roles_required(['admin'])
user_only = roles_required(['user'])
