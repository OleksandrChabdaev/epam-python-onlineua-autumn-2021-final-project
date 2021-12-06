from decouple import config

user = config('MYSQL_USER')
password = config('MYSQL_PASSWORD')
server = config('MYSQL_SERVER')
database = config('MYSQL_DATABASE')


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{user}:{password}@{server}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
