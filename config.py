import os


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'postgres://Lukasz:pass:@localhost:5000'


class DevConfig(Config):
    DEBUG = True
    DATABASE_URI = os.getenv('DEV_DATABASE_URI', '')


class ProdConfig(Config):
    DATABASE_URI = os.getenv('PROD_DATABASE_URI', '')


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
