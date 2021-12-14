"""
Defines department model.
"""
# pylint: disable=cyclic-import
from department_app import db


class Department(db.Model):
    """
    Department model.
    """

    # pylint: disable=too-few-public-methods
    __tablename__ = 'departments'
    # pylint: disable=no-member
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    employees = db.relationship(
        'Employee', cascade="all,delete", backref=db.backref('department', lazy=True), lazy=True
    )

    def __init__(self, name, employees=None):
        """
        Constructor.
        :param name: department name
        :param employees: department employees
        """
        self.name = name
        self.employees = employees if employees else []

    def __repr__(self):
        """
        Returns department string representation.
        :return: department string representation
        """
        return f'Department: {self.name}'
