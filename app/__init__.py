import os
from flask import Flask
from flask_cors import CORS

from .extensions import db
from app import cli


config = {
    'dev': 'app.config.DevConfig',
    'prod': 'app.config.ProdConfig',
    'test': 'app.config.TestConfig'
}

app = Flask(__name__, instance_relative_config=True)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


def create_app():
    config_name = os.getenv('FLASK_CONFIG', 'dev')

    # app.config.from_object(config[config_name])
    from werkzeug.utils import import_string
    config_object = import_string(config[config_name])()
    app.config.from_object(config_object)

    db.init_app(app)
    cli.init_cli_commands(app)

    return app
