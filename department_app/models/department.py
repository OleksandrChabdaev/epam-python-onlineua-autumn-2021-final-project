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

    def __repr__(self):
        return f'Department: {self.name}'
