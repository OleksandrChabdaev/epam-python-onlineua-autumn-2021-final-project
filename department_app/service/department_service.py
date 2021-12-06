from department_app import db
from department_app.models.department import Department


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
            db.session.add(department)
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
    def delete(department):
        db.session.delete(department)
        db.session.commit()
