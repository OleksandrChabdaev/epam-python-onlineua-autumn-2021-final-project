"""
Defines test cases for department API.
"""
import json
import unittest
from department_app import app

client = app.test_client()
HOST = 'http://127.0.0.1:5000'


class DepartmentApiTests(unittest.TestCase):
    """
    Department API test cases.
    """

    def test_1_get_list_api(self):
        """
        Tests to get all departments.
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/departments')
            departments = json.loads(response.data)
            self.assertEqual(len(departments), 3)

    def test_2_post_list_api(self):
        """
        Tests to add department.
        :return: None
        """
        with client:
            response = client.post(f'{HOST}/api/departments')
            departments = json.loads(response.data)
            self.assertEqual(departments['message'], 'Incorrect request')
            response = client.post(f'{HOST}/api/departments', data={'name': 'Dep_4'})
            departments = json.loads(response.data)
            self.assertEqual(departments[0]['name'], 'Dep_4')
            response = client.post(f'{HOST}/api/departments', data={'name': 'Dep_4'})
            departments = json.loads(response.data)
            self.assertEqual(departments['message'], 'Department already exists')

    def test_3_get_api(self):
        """
        Tests to get department.
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/department/1')
            department = json.loads(response.data)
            self.assertEqual(department['name'], 'Dep_1')
            response = client.get(f'{HOST}/api/department/5')
            department = json.loads(response.data)
            self.assertEqual(department['message'], 'Department not found')

    def test_4_put_api(self):
        """
        Tests to edit department.
        :return: None
        """
        with client:
            response = client.put(f'{HOST}/api/department/5', data={'name': 'Dep_5'})
            department = json.loads(response.data)
            self.assertEqual(department['message'], 'Department not found')
            response = client.put(f'{HOST}/api/department/4')
            department = json.loads(response.data)
            self.assertEqual(department['message'], 'Incorrect request')
            response = client.put(f'{HOST}/api/department/4', data={'name': 'Dep_5'})
            department = json.loads(response.data)
            self.assertEqual(department[0]['name'], 'Dep_5')
            response = client.put(f'{HOST}/api/department/4', data={'name': 'Dep_1'})
            department = json.loads(response.data)
            self.assertEqual(department['message'], 'Department already exists')

    def test_5_delete_api(self):
        """
        Tests to delete department.
        :return: None
        """
        with client:
            client.delete(f'{HOST}/api/department/4')
            message = 'Department has been successfully deleted'
            self.assertEqual(message, 'Department has been successfully deleted')
            response = client.delete(f'{HOST}/api/department/5')
            department = json.loads(response.data)
            self.assertEqual(department['message'], 'Department not found')
