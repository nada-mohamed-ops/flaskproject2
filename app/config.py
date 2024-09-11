import os
class Config:
    # wtf forms --> needs secret key
    # generate
    SECRET_KEY = os.urandom(32) # generate random key -> length 32
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://test:123@localhost:5432/library_project'


config_options = {
    "dev": DevelopmentConfig,
    "prd": ProductionConfig
}


