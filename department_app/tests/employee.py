"""
Defines test cases for employee model.
"""
import unittest
from datetime import datetime
from department_app.models.employee import Employee


class EmployeeModelTests(unittest.TestCase):
    """
    Employee model test cases.
    """

    def test_employee(self):
        """
        Tests employee model.
        :return: None
        """
        employee = Employee(
            first_name='First Name 10',
            last_name='Last Name 10',
            department=1,
            birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
            salary=10000
        )
        self.assertEqual(repr(employee), 'Employee: First Name 10, Last Name 10, None, 2000-01-15, 10000')
