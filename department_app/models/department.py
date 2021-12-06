from department_app import db


class Department(db.Model):

    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    employees = db.relationship(
        'Employee', cascade="all,delete", backref=db.backref('department', lazy=True), lazy=True
    )

    def __init__(self, name, employees=None):
        self.name = name
        self.employees = employees if employees else []

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'employees': [employee.to_dict() for employee in self.employees]
        }

    def __repr__(self):
        return f'Department: {self.name}'
