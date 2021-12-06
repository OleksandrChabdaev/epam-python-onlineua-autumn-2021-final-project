import os.path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.debug = True
app.config.from_object(Config)
db = SQLAlchemy(app)

# from .rest import init_api
# init_api()
# from .views import init_views
# init_views()
from .models import employee
from .models import department

migrate = Migrate(app, db, directory=os.path.join('department_app', 'migrations'))
