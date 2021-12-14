"""
Populates database with departments and employees.
"""
from datetime import date
from department_app import db
from .department import Department
from .employee import Employee


class Populate:
    """
    Initialises and populates database with departments and employees.
    """

    # pylint: disable=too-few-public-methods
    @staticmethod
    def populate():
        """
        Creates tables and populates database with departments and employees.
        :return: None
        """
        db.drop_all()
        db.create_all()
        department_1 = Department('Dep_1')
        department_2 = Department('Dep_2')
        department_3 = Department('Dep_3')
        employee_1 = Employee('First Name 1', 'Last Name 1',
                              date(2001, 1, 11), department_1.id, 1000)
        employee_2 = Employee('First Name 2', 'Last Name 2',
                              date(2002, 2, 12), department_2.id, 2000)
        employee_3 = Employee('First Name 3', 'Last Name 3',
                              date(2003, 3, 13), department_3.id, 3000)
        employee_4 = Employee('First Name 4', 'Last Name 4',
                              date(2004, 4, 14), department_1.id, 4000)
        employee_5 = Employee('First Name 5', 'Last Name 5',
                              date(2005, 5, 15), department_2.id, 5000)
        employee_6 = Employee('First Name 6', 'Last Name 6',
                              date(2006, 6, 16), department_3.id, 6000)
        employee_7 = Employee('First Name 7', 'Last Name 7',
                              date(2007, 7, 17), department_1.id, 7000)
        employee_8 = Employee('First Name 8', 'Last Name 8',
                              date(2008, 8, 18), department_2.id, 8000)
        employee_9 = Employee('First Name 9', 'Last Name 9',
                              date(2009, 9, 19), department_3.id, 9000)
        department_1.employees = [employee_1, employee_2, employee_3]
        department_2.employees = [employee_4, employee_5, employee_6]
        department_3.employees = [employee_7, employee_8, employee_9]
        db.session.add(department_1)
        db.session.add(department_2)
        db.session.add(department_3)
        db.session.add(employee_1)
        db.session.add(employee_2)
        db.session.add(employee_3)
        db.session.add(employee_4)
        db.session.add(employee_5)
        db.session.add(employee_6)
        db.session.add(employee_7)
        db.session.add(employee_8)
        db.session.add(employee_9)
        db.session.commit()
        db.session.close()


if __name__ == '__main__':
    Populate.populate()
