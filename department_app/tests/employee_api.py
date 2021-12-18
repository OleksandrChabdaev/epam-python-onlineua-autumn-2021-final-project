"""
Defines test cases for employee API.
"""
import json
import unittest
from department_app import app

HOST = 'http://127.0.0.1:5000'
client = app.test_client()


class EmployeeApiTests(unittest.TestCase):
    """
    Employee API test cases.
    """

    def test_1_get_search_api(self):
        """
        Tests to search employees with birthdate in mentioned period.
        :return: None
        """
        with client:
            response = client.get(
                f'{HOST}/api/employees/search'
            )
            employees = json.loads(response.data)
            self.assertEqual(employees['message'], 'Incorrect date')
            response = client.get(
                f'{HOST}/api/employees/search?date_from=2000/01/01&date_to=2005/12/31'
            )
            employees = json.loads(response.data)
            self.assertEqual(len(employees), 5)

    def test_2_get_list_api(self):
        """
        Tests to get all employees.
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/employees')
            employees = json.loads(response.data)
            self.assertEqual(len(employees), 9)

    def test_3_post_list_api(self):
        """
        Tests to add employee.
        :return: None
        """
        with client:
            response = client.post(f'{HOST}/api/employees')
            employees = json.loads(response.data)
            self.assertEqual(employees['message'], 'Incorrect request')
            response = client.post(f'{HOST}/api/employees', data={
                'first_name': 'First Name 10',
                'last_name': 'Last Name 10',
                'birthdate': '2000/13/32',
                'department': 'Dep_1',
                'salary': '10000'
            })
            employees = json.loads(response.data)
            self.assertEqual(employees['message'], 'Incorrect birthdate')
            response = client.post(f'{HOST}/api/employees', data={
                'first_name': 'First Name 10',
                'last_name': 'Last Name 10',
                'birthdate': '2000/01/21',
                'department': 'Dep_4',
                'salary': '10000'
            })
            employees = json.loads(response.data)
            self.assertEqual(employees['message'], 'Incorrect department')
            response = client.post(f'{HOST}/api/employees', data={
                'first_name': 'First Name 10',
                'last_name': 'Last Name 10',
                'birthdate': '2000/01/21',
                'department': 'Dep_1',
                'salary': 'salary'
            })
            employees = json.loads(response.data)
            self.assertEqual(employees['message'], 'Incorrect salary')
            response = client.post(f'{HOST}/api/employees', data={
                'first_name': 'First Name 10',
                'last_name': 'Last Name 10',
                'birthdate': '2000/01/21',
                'department': 'Dep_1',
                'salary': '10000'
            })
            employees = json.loads(response.data)
            self.assertEqual(employees[0]['first_name'], 'First Name 10')

    def test_4_get_api(self):
        """
        Tests to get employee.
        :return: None
        """
        with client:
            response = client.get(f'{HOST}/api/employee/1')
            employee = json.loads(response.data)
            self.assertEqual(employee['first_name'], 'First Name 1')
            response = client.get(f'{HOST}/api/employee/11')
            employee = json.loads(response.data)
            self.assertEqual(employee['message'], 'Employee not found')

    def test_5_put_api(self):
        """
        Tests to edit employee.
        :return: None
        """
        with client:
            response = client.put(f'{HOST}/api/employee/11', data={
                'salary': '20000'
            })
            employee = json.loads(response.data)
            self.assertEqual(employee['message'], 'Employee not found')
            response = client.put(f'{HOST}/api/employee/10', data={
                'birthdate': '2000/13/32',
            })
            employee = json.loads(response.data)
            self.assertEqual(employee['message'], 'Incorrect birthdate')
            response = client.put(f'{HOST}/api/employee/10', data={
                'department': 'Dep_4',
            })
            employee = json.loads(response.data)
            self.assertEqual(employee['message'], 'Incorrect department')
            response = client.put(f'{HOST}/api/employee/10', data={
                'salary': 'salary'
            })
            employee = json.loads(response.data)
            self.assertEqual(employee['message'], 'Incorrect salary')
            response = client.put(f'{HOST}/api/employee/10', data={
                'first_name': 'First Name 11',
                'last_name': 'Last Name 11',
                'birthdate': '2001/02/22',
                'department': 'Dep_2',
                'salary': '20000'
            })
            employee = json.loads(response.data)
            self.assertEqual(employee[0]['first_name'], 'First Name 11')

    def test_6_delete_api(self):
        """
        Tests to delete employee.
        :return: None
        """
        with client:
            client.delete(f'{HOST}/api/employee/10')
            message = 'Employee has been successfully deleted'
            self.assertEqual(message, 'Employee has been successfully deleted')
            response = client.delete(f'{HOST}/api/employee/11')
            department = json.loads(response.data)
            self.assertEqual(department['message'], 'Employee not found')
