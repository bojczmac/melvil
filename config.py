from os import getenv


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = ''


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        getenv('DB_ENGINE'),
        getenv('POSTGRES_USER'),
        getenv('POSTGRES_PASSWORD'),
        getenv('DB_HOST'),
        getenv('DB_PORT'),
        getenv('POSTGRES_PASSWORD')
    )


class ProdConfig(Config):
    DATABASE_URI = getenv('PROD_DATABASE_URI', '')
