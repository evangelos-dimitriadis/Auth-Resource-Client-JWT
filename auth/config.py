import os
from dotenv import load_dotenv

CURRENT_PATH = os.getcwd()

load_dotenv(os.path.join(CURRENT_PATH, '/.env'))


class Config:
    LOGS_FILE = os.path.join(CURRENT_PATH, 'log')
    APP_SECRET_KEY = os.getenv('APP_SECRET_KEY') or 'so_secret'

    @staticmethod
    def init_app(app):
        pass


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}
