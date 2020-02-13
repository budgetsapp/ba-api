import os
from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView
from flask_jwt_extended import JWTManager, get_jwt_identity

from .extensions import db
from app import cli
from app.api import schema


config = {
    "dev-docker": "app.config.DevDockerConfig",
    'local': 'app.config.LocalConfig',
    'prod': 'app.config.ProdConfig',
}

app = Flask(__name__, instance_relative_config=True)
jwt = JWTManager(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.add_url_rule(
    '/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))


def create_app():
    config_name = os.getenv('FLASK_CONFIG', 'local')

    # app.config.from_object(config[config_name])
    from werkzeug.utils import import_string
    config_object = import_string(config[config_name])()
    app.config.from_object(config_object)
    print('===> Config name', config_name)
    print('===> SQLALCHEMY_DATABASE_URI',
          config_object.SQLALCHEMY_DATABASE_URI)

    db.init_app(app)
    cli.init_cli_commands(app)

    return app
