import os
from dotenv import load_dotenv

load_dotenv()
user = os.environ.get('MYSQL_USER')
password = os.environ.get('MYSQL_PASSWORD')
server = os.environ.get('MYSQL_SERVER')
database = os.environ.get('MYSQL_DATABASE')
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{user}:{password}@{server}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'department_app', 'tests', 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
