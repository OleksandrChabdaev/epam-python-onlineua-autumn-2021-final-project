"""
Initializes web application and web service.
"""
import os.path
from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config

secret_key = config('SECRET_KEY')

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = secret_key
app.config.from_object(Config)
api = Api(app)
db = SQLAlchemy(app)

from .rest import init_api
init_api()
from .views import department_view, employee_view
from .models import employee, department

migrate = Migrate(app, db, directory=os.path.join('department_app', 'migrations'))
