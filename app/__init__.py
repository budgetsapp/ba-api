import os

from flask import Flask
from .api import categories


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.register_blueprint(categories.categories_api)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE_PATH=os.path.join(app.instance_path, 'budgetapp.sqlite')
    )

    if test_config is None:
        # load the instance config, if it exist, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
