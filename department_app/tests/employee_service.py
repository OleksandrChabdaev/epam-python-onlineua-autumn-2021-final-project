"""
Defines test cases for employee service.
"""
import unittest
from datetime import datetime
from department_app.service.employee_service import EmployeeServices


class EmployeeServiceTests(unittest.TestCase):
    """
    Employee service test cases.
    """

    def test_1_get_all(self):
        """
        Tests to get all employees.
        :return: None
        """
        self.assertEqual(len(EmployeeServices.get_all()), 9)

    def test_2_get_all_for_department(self):
        """
        Tests to get all employees for the department.
        :return: None
        """
        self.assertEqual(len(EmployeeServices.get_all_for_department(1)), 3)

    def test_3_get_by_id(self):
        """
        Tests to get employee by id.
        :return: None
        """
        self.assertEqual(EmployeeServices.get_by_id(1).first_name, 'First Name 1')

    def test_4_get_by_birthdate(self):
        """
        Tests to get employee with birthdate in mentioned period.
        :return: None
        """
        date_from = datetime.strptime('2001/01/11', '%Y/%m/%d')
        date_to = datetime.strptime('2005/05/15', '%Y/%m/%d')
        self.assertEqual(len(EmployeeServices.get_by_birthdate(date_from, date_to)), 4)

    def test_5_add(self):
        """
        Tests to add employee.
        :return: None
        """
        EmployeeServices.add(
            first_name='First Name 10',
            last_name='Last Name 10',
            department_id=1,
            birthdate=datetime.strptime('2000/01/15', '%Y/%m/%d').date(),
            salary=10000
        )
        self.assertEqual(len(EmployeeServices.get_all()), 10)

    def test_6_update(self):
        """
        Tests to update employee.
        :return: None
        """
        birthdate = datetime.strptime('2001/02/13', '%Y/%m/%d').date()
        EmployeeServices.update(
            employee_id=10,
            first_name='First Name 11',
            last_name='Last Name 11',
            department_id=1,
            birthdate=birthdate,
            salary=20000
        )
        self.assertEqual(EmployeeServices.get_by_id(10).first_name, 'First Name 11')
        self.assertEqual(EmployeeServices.get_by_id(10).last_name, 'Last Name 11')
        self.assertEqual(EmployeeServices.get_by_id(10).department_id, 1)
        self.assertEqual(EmployeeServices.get_by_id(10).birthdate, birthdate)
        self.assertEqual(EmployeeServices.get_by_id(10).salary, 20000)

    def test_7_delete(self):
        """
       Tests to delete employee.
        :return: None
        """
        EmployeeServices.delete(10)
        self.assertEqual(len(EmployeeServices.get_all()), 9)

    def test_8_to_dict(self):
        """
        Tests employee dictionary representation.
        :return: None
        """
        employee = EmployeeServices.to_dict(1)
        self.assertEqual(employee['first_name'], 'First Name 1')
        self.assertEqual(employee['last_name'], 'Last Name 1')
        self.assertEqual(employee['department'], 'Dep_1')
        self.assertEqual(employee['birthdate'], '2001-01-11')
        self.assertEqual(employee['salary'], 1000)
