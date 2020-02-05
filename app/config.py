import os


class Config:
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def JWT_SECRET_KEY(self):
        return os.getenv("JWT_SECRET_KEY", None)


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/db'


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        uri = 'sqlite:///budgetsapp.sqlite'
        print(uri)
        return uri


class TestConfig(Config):
    TESTING = True
