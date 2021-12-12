from department_app import db
from department_app.models.department import Department
from department_app.models.employee import Employee


class EmployeeServices:

    @staticmethod
    def get_all():
        return Employee.query.all()

    @staticmethod
    def get_all_for_department(department_id):
        return Employee.query.filter_by(department_id=department_id).all()

    @staticmethod
    def get_by_id(employee_id):
        return Employee.query.filter_by(id=employee_id).first()

    @staticmethod
    def get_by_birthdate(date_from, date_to):
        return Employee.query.filter(Employee.birthdate.between(date_from, date_to)).all()

    @staticmethod
    def add(first_name, last_name, birthdate, department_id, salary):
        employee = Employee(
            first_name=first_name,
            last_name=last_name,
            department=department_id,
            birthdate=birthdate,
            salary=salary
        )
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def update(employee_id, first_name=None, last_name=None, birthdate=None, department_id=None, salary=None):
        employee = Employee.query.get_or_404(employee_id)
        if first_name:
            employee.first_name = first_name
        if last_name:
            employee.last_name = last_name
        if birthdate:
            employee.birthdate = birthdate
        if department_id:
            employee.department_id = department_id
        if salary:
            employee.salary = salary
        db.session.add(employee)
        db.session.commit()

    @staticmethod
    def delete(employee_id):
        employee = Employee.query.get_or_404(employee_id)
        db.session.delete(employee)
        db.session.commit()

    @staticmethod
    def to_dict(employee_id):
        employee = EmployeeServices.get_by_id(employee_id)
        return {
            'id': employee.id,
            'first_name': employee.first_name,
            'last_name': employee.last_name,
            'department': Department.query.get_or_404(employee.department_id).name,
            'birthdate': employee.birthdate.strftime('%Y-%m-%d'),
            'salary': employee.salary
        }