import os
import multiprocessing

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

APPLICATION_URL = '127.0.0.1:8080'

GUNICORN_WORKERS = 1 + 2 * multiprocessing.cpu_count()

YANDEX_API_KEY = 'trnsl.1.1.20170403T222405Z.1a6631e72a70e4fb.15c01339efa02e0f694fde310b862d823374538c'


class BaseConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://iqoptions:12345@127.0.0.1/backoffice'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


CONFIG = BaseConfig
