"""
Defines test cases for department view.
"""
import unittest
import requests
from department_app import app
from department_app.views.department_view import DepartmentForm


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
        response = self.client.get('/departments/')
        self.assertEqual(response.status_code, 200)

    def test_2_show_department(self):
        """
        Tests department view.
        :return: None
        """
        response = self.client.get('/department/1')
        self.assertEqual(response.status_code, 200)

    # def test_3_add_department(self):
    #     """
    #     Tests add department view.
    #     :return: None
    #     """
    #     with self.client.get('/departments/add/') as c:
    #         form = DepartmentForm(name='Dep_1', submit=True)
    #         self.assertEqual(form.validate_on_submit(), True)
    #
    #
    #     response = self.client.get('/departments/add/')
    #     self.assertEqual(response.status_code, 200)
    #
    # def test_4_edit_department(self):
    #     """
    #     Tests edit department view.
    #     :return: None
    #     """
    #     # response = self.client.get('/department/edit')
    #     # self.assertEqual(response.status_code, 200)
    #     response = self.client.get('/departments/edit/1')
    #     self.assertEqual(response.status_code, 200)

    # def test_delete_department(self):
    #     """
    #     Tests delete department view.
    #     :return: None
    #     """
    #     # response = self.client.get('/department/delete')
    #     # self.assertEqual(response.status_code, 200)
    #     response = self.client.get('/departments/delete/1')
    #     self.assertEqual(response.status_code, 200)
