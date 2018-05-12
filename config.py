from os import getenv


class Config(object):
    DEBUG = False
    TESTING = True
    DATABASE_URI = ''


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(getenv('DB_ENGINE'), getenv('DB_USER'), getenv('DB_PASSWORD'), getenv('DB_HOST'), getenv('DB_PORT'), getenv('DB_NAME'))

class ProdConfig(Config):
    DATABASE_URI = getenv('PROD_DATABASE_URI', '')
