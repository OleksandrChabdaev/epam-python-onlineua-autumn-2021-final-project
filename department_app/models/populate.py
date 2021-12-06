from datetime import date
from department_app import db
from .department import Department
from .employee import Employee
from department_app.service.department_service import DepartmentServices
from department_app.service.employee_service import EmployeeServices


class Populate:

    @staticmethod
    def populate():
        db.drop_all()
        db.create_all()
        department_1 = Department('Dep_1')
        department_2 = Department('Dep_2')
        department_3 = Department('Dep_3')
        employee_1 = Employee('First Name 1', 'Last Name 1', date(2001, 1, 11), department_1.id, 1000)
        employee_2 = Employee('First Name 2', 'Last Name 2', date(2002, 2, 12), department_2.id, 2000)
        employee_3 = Employee('First Name 3', 'Last Name 3', date(2003, 3, 13), department_3.id, 3000)
        department_1.employees = [employee_1]
        department_2.employees = [employee_2]
        department_3.employees = [employee_3]
        db.session.add(department_1)
        db.session.add(department_2)
        db.session.add(department_3)
        db.session.add(employee_1)
        db.session.add(employee_2)
        db.session.add(employee_3)
        db.session.commit()
        db.session.close()

        print(DepartmentServices.get_all())
        print(DepartmentServices.get_by_id(1))
        DepartmentServices.add('Dep_4')
        print(DepartmentServices.get_all())
        DepartmentServices.update(2)
        print(DepartmentServices.get_all())
        DepartmentServices.update(2, 'Dep_5')
        print(DepartmentServices.get_all())
        print(DepartmentServices.get_average_salary(Department.query.get(1)))
        DepartmentServices.delete(Department.query.get(1))
        print(DepartmentServices.get_all())
        print(EmployeeServices.get_all())
        print(EmployeeServices.get_all_for_department(3))
        EmployeeServices.add('First Name 4', 'Last Name 4', date(2004, 4, 14), Department.query.get(3), 4000)
        print(EmployeeServices.get_all())
        print(EmployeeServices.get_all_for_department(3))
        print(DepartmentServices.get_average_salary(Department.query.get(3)))
        print(EmployeeServices.get_by_id(2))
        print(EmployeeServices.get_by_birthdate(date(2003, 3, 13), date(2004, 4, 14)))
        EmployeeServices.update(2, first_name='First Name 5', last_name='Last Name 5')
        print(EmployeeServices.get_all_for_department(2))
        EmployeeServices.update(2, department_id=4)
        print(EmployeeServices.get_all_for_department(2))
        print(EmployeeServices.get_all_for_department(4))
        EmployeeServices.delete(Employee.query.get(4))
        print(EmployeeServices.get_all())
        print()


if __name__ == '__main__':
    Populate.populate()
