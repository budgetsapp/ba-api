class Config:
    DEBUG = False
    TESTING = False
    DATABASE_URL = 'sqlite:///:memory:'


class ProdConfig(Config):
    DATABASE_URL = 'mysql://user@localhost/db'


class DevConfig(Config):
    DEBUG = True
    DATABASE_URL = 'db_dev/budgetsapp.sqlite'


class TestConfig(Config):
    TESTING = True
