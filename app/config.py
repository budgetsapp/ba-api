import os


class Config:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/db'


class DevConfig(Config):

    def __init__(self):
        self.root = os.path.abspath(os.path.join(os.path.dirname(
            __file__), '..'))

    FLASK_ENV = 'development'
    DEBUG = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        uri = 'sqlite:///{}\\db_dev\\budgetsapp.sqlite'.format(self.root)
        print(uri)
        return uri


class TestConfig(Config):
    TESTING = True
