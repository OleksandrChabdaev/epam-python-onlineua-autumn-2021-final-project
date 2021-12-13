"""
Defines department service.
"""
from department_app import db
from department_app.models.department import Department
from department_app.service.employee_service import EmployeeServices


class DepartmentServices:
    """
    Department service.
    """

    @staticmethod
    def get_all():
        """
        Returns all departments from database.
        :return: list of all departments
        """
        return Department.query.all()

    @staticmethod
    def get_by_id(department_id):
        """
        Returns department from database.
        :param department_id: department_id
        :return: department
        """
        return Department.query.filter_by(id=department_id).first()

    @staticmethod
    def add(name):
        """
        Adds department to database.
        :param name: department name
        :return: None
        """
        department = Department(name)
        db.session.add(department)
        db.session.commit()

    @staticmethod
    def update(department_id, name=None):
        """
        Updates department in database.
        :param department_id: department id
        :param name: department name
        :return: None
        """
        if name:
            department = Department.query.get_or_404(department_id)
            department.name = name
            db.session.commit()

    @staticmethod
    def get_average_salary(department):
        """
        Returns department average salary
        :param department: department
        :return: department average salary
        """
        average_salary = 0
        if department.employees:
            for employee in department.employees:
                average_salary += employee.salary
            average_salary /= len(department.employees)
        return round(average_salary, 2)

    @staticmethod
    def delete(department_id):
        """
        Deletes department in database.
        :param department_id: department id
        :return: None
        """
        department = Department.query.get_or_404(department_id)
        db.session.delete(department)
        db.session.commit()

    @staticmethod
    def to_dict(department_id):
        """
        Returns department dictionary representation.
        :param department_id: department id
        :return: department dictionary representation
        """
        department = DepartmentServices.get_by_id(department_id)
        return {
            'id': department.id,
            'name': department.name,
            'employees_count': len(department.employees),
            'average_salary': DepartmentServices.get_average_salary(department),
            'employees': [EmployeeServices.to_dict(employee.id) for employee in department.employees]
        }
