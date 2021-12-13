"""
Defines employee model.
"""
from department_app import db


class Employee(db.Model):
    """
    Employee model.
    """

    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    birthdate = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer)

    def __init__(self, first_name, last_name, birthdate, department=None, salary=0):
        """
        Constructor.
        :param first_name: employee first name
        :param last_name: employee last name
        :param birthdate: employee birthdate
        :param department: employee department id
        :param salary: employee salary
        """
        self.first_name = first_name
        self.last_name = last_name
        self.department_id = department
        self.birthdate = birthdate
        self.salary = salary

    def __repr__(self):
        """
        Returns employee string representation.
        :return: employee string representation
        """
        return f'Employee: {self.first_name}, {self.last_name}, {self.department}, {self.birthdate}, {self.salary}'
