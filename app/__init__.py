import os

from flask import Flask
from .api import categories

config = {
    'dev': 'app.config.DevConfig',
    'prod': 'app.config.ProdConfig',
    'test': 'app.config.TestConfig'
}


def create_app():
    config_name = os.getenv('FLASK_CONFIG', 'dev')
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config[config_name])
    app.register_blueprint(categories.categories_api)

    # ensure the db_dev folder exists
    try:
        os.makedirs('db_dev')
    except OSError:
        pass

    from .db import setup
    setup.init_app(app)

    return app
