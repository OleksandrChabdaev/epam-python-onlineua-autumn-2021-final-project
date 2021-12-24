"""
Defines test cases for department view.
"""
import unittest
from unittest.mock import patch
from department_app import app


class DepartmentViewTests(unittest.TestCase):
    """
    Department view test cases.
    """
    client = app.test_client()

    def test_1_show_departments(self):
        """
        Tests departments view.
        :return: None
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            response = self.client.get('/departments/')
            self.assertEqual(response.status_code, 200)

    def test_2_show_department(self):
        """
        Tests department view.
        :return: None
        """
        with patch('requests.get') as mock_request:
            mock_request.return_value.status_code = 200
            response = self.client.get('/department/1')
            self.assertEqual(response.status_code, 200)

    def test_3_delete_department(self):
        """
        Tests delete department view.
        :return: None
        """
        with patch('requests.delete') as mock_request:
            mock_request.return_value.status_code = 302
            response = self.client.get('/departments/delete/1')
            self.assertEqual(response.status_code, 302)
