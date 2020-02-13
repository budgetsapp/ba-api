import os


class Config:
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def JWT_SECRET_KEY(self):
        return os.getenv("JWT_SECRET_KEY", None)


class ProdConfig(Config):
    pass


class LocalConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///C:\\Users\\Vadim\\Documents\\db\\budgetsapp.sqlite'


class DevDockerConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////usr/db/budgetsapp.sqlite'
