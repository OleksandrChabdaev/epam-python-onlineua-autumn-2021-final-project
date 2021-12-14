"""
Defines test cases for department service.
"""
import unittest
from department_app.service.department_service import DepartmentServices


class DepartmentServiceTests(unittest.TestCase):
    """
    Department service test cases.
    """

    def test_1_get_all(self):
        """
        Tests to get all departments.
        :return: None
        """
        self.assertEqual(len(DepartmentServices.get_all()), 3)

    def test_2_get_by_id(self):
        """
        Tests to get department by id.
        :return: None
        """
        self.assertEqual(DepartmentServices.get_by_id(1).id, 1)

    def test_3_add(self):
        """
        Tests to add department.
        :return: None
        """
        DepartmentServices.add('Dep_4')
        self.assertEqual(len(DepartmentServices.get_all()), 4)

    def test_4_update(self):
        """
        Tests to update department.
        :return: None
        """
        DepartmentServices.update(4, 'Dep_4')
        self.assertEqual(DepartmentServices.get_by_id(4).name, 'Dep_4')

    def test_5_get_average_salary(self):
        """
        Tests to get department average salary.
        :return: None
        """
        department = DepartmentServices.get_by_id(1)
        avg_salary = DepartmentServices.get_average_salary(department)
        self.assertEqual(avg_salary, 2000)

    def test_6_delete(self):
        """
        Tests to delete department.
        :return: None
        """
        DepartmentServices.delete(4)
        self.assertEqual(len(DepartmentServices.get_all()), 3)

    def test_7_to_dict(self):
        """
        Tests department dictionary representation.
        :return: None
        """
        department = DepartmentServices.to_dict(1)
        self.assertEqual(department['id'], 1)
        self.assertEqual(department['name'], 'Dep_1')
        self.assertEqual(department['employees_count'], 3)
        self.assertEqual(department['average_salary'], 2000)
        self.assertEqual(len(department['employees']), 3)
