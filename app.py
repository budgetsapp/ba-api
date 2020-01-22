from flask import Flask
from flask_graphql import GraphQLView

from src.models.base import db_session
from src.schema.schema import schema

# TODO: #1 graphiql is True for dev only
app = Flask(__name__)
app.debug = True
app.add_url_rule(
    '/api', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
