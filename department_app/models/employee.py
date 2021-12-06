from department_app import db
from .department import Department


class Employee(db.Model):

    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    birthdate = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer)

    def __init__(self, first_name, last_name, birthdate, department=None, salary=0):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.birthdate = birthdate
        self.salary = salary

    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'department': Department.query.get_or_404(self.department_id).name,
            'salary': self.salary,
            'birthdate': self.birthdate.strftime('%Y/%m/%d')
        }

    def __repr__(self):
        return f'Employee: {self.first_name}, {self.last_name}, {self.department}, {self.birthdate}, {self.salary}'
