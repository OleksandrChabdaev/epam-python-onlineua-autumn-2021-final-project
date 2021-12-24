"""
Defines test cases for employee view.
"""
import unittest
from unittest.mock import patch
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
        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            response = self.client.get('/employees/')
            self.assertEqual(response.status_code, 200)

    def test_2_show_employee(self):
        """
        Tests employee view.
        :return: None
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            response = self.client.get('/employee/1')
            self.assertEqual(response.status_code, 200)

    def test_3_delete_employee(self):
        """
        Tests delete employee view.
        :return: None
        """
        with patch('requests.delete') as mock_request:
            mock_request.return_value.status_code = 302
            response = self.client.get('/employees/delete/1')
            self.assertEqual(response.status_code, 302)
