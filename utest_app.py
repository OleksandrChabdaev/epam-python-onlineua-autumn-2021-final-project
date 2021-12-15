"""
Initializes tests.
"""
import unittest
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from config import TestingConfig
from department_app.tests.department import DepartmentModelTests
from department_app.tests.department_service import DepartmentServiceTests
from department_app.tests.employee import EmployeeModelTests
from department_app.tests.employee_service import EmployeeServiceTests


if __name__ == '__main__':
    app = Flask(__name__)
    app.debug = True
    app.config['SECRET_KEY'] = 'SECRET_KEY'
    app.config.from_object(TestingConfig)
    api = Api(app)
    db = SQLAlchemy(app)

    appTestSuite = unittest.TestSuite()
    appTestSuite.addTest(unittest.makeSuite(DepartmentModelTests))
    appTestSuite.addTest(unittest.makeSuite(DepartmentServiceTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeModelTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeServiceTests))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(appTestSuite)
