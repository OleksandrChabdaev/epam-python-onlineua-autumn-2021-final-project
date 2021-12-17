"""
Defines test cases for employee view.
"""
import unittest
from department_app import app


class EmployeeViewTests(unittest.TestCase):
    """
    Employee view test cases.
    """
    client = app.test_client()

    def test_1_show_employees(self):
        """
        Tests employees view.
        :return: None
        """
        response = self.client.get('/employees/')
        self.assertEqual(response.status_code, 200)

    def test_2_show_employee(self):
        """
        Tests employee view.
        :return: None
        """
        response = self.client.get('/employee/1')
        self.assertEqual(response.status_code, 200)
