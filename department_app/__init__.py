"""
Initializes web application and web service.
"""
# pylint: disable=wrong-import-position
import logging
import os
import sys
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import Config

load_dotenv()
secret_key = os.environ.get('SECRET_KEY')

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

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')
file_handler = logging.FileHandler(filename='department_app.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)
logger = app.logger
# pylint: disable=no-member
logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)
werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)
