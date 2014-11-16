# config.py

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):

    # main Config
    SECRET_KEY = 'my_precious'
    DEBUG = False
    WTF_CSRF_ENABLED = True

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'from@example.com'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        basedir, 'data-test.sqlite')
    WTF_CSRF_ENABLED = False


class StagingConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass
