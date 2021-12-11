from department_app import db
from department_app.models.department import Department
from department_app.service.employee_service import EmployeeServices


class DepartmentServices:

    @staticmethod
    def get_all():
        return Department.query.all()

    @staticmethod
    def get_by_id(department_id):
        return Department.query.filter_by(id=department_id).first()

    @staticmethod
    def add(name):
        department = Department(name)
        db.session.add(department)
        db.session.commit()

    @staticmethod
    def update(department_id, name=None):
        if name:
            department = Department.query.get_or_404(department_id)
            department.name = name
            db.session.commit()

    @staticmethod
    def get_average_salary(department):
        average_salary = 0
        if department.employees:
            for employee in department.employees:
                average_salary += employee.salary
            average_salary /= len(department.employees)
        return round(average_salary, 2)

    @staticmethod
    def delete(department_id):
        department = Department.query.get_or_404(department_id)
        db.session.delete(department)
        db.session.commit()

    @staticmethod
    def to_dict(department_id):
        department = DepartmentServices.get_by_id(department_id)
        return {
            'id': department.id,
            'name': department.name,
            'employees_count': len(department.employees),
            'average_salary': DepartmentServices.get_average_salary(department),
            'employees': [EmployeeServices.to_dict(employee.id) for employee in department.employees]
        }
