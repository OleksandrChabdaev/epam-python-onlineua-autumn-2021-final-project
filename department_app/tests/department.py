"""
Defines test cases for department model.
"""
import unittest
from department_app.models.department import Department


class DepartmentModelTests(unittest.TestCase):
    """
    Department model test cases.
    """

    def test_department(self):
        """
        Tests department model.
        :return: None
        """
        department = Department('Dep_4')
        self.assertEqual(repr(department), 'Department: Dep_4')
