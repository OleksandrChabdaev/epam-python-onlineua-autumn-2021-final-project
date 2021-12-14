"""
Defines employee REST API.
"""
# pylint: disable=cyclic-import
from datetime import datetime
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from department_app.models.department import Department
from department_app.service.department_service import DepartmentServices
from department_app.service.employee_service import EmployeeServices


class EmployeeSearchApi(Resource):
    """
    Employee search API.
    """

    @staticmethod
    def get():
        """
        GET request handler for employee search API.
        :return: employee list json representation or error message and status code
        """
        parser = reqparse.RequestParser()
        parser.add_argument('date_from')
        parser.add_argument('date_to')
        args = parser.parse_args()
        try:
            date_from = datetime.strptime(args['date_from'], '%Y/%m/%d')
            date_to = datetime.strptime(args['date_to'], '%Y/%m/%d')
        except (ValueError, TypeError):
            return make_response({'message': 'Incorrect date'}, 400)
        employees = EmployeeServices.get_by_birthdate(date_from, date_to)
        return jsonify([EmployeeServices.to_dict(employee.id) for employee in employees])


class EmployeeListApi(Resource):
    """
    Employee list API.
    """

    @staticmethod
    def get():
        """
        GET request handler for employee list API.
        :return: employee list json representation
        """
        employees = EmployeeServices.get_all()
        return jsonify([EmployeeServices.to_dict(employee.id) for employee in employees])

    @staticmethod
    def post():
        """
        POST request handler for employee list API.
        :return: employee list json representation or error message and status code
        """
        parser = reqparse.RequestParser()
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        parser.add_argument('department')
        parser.add_argument('birthdate')
        parser.add_argument('salary')
        args = parser.parse_args()
        first_name = args['first_name']
        last_name = args['last_name']
        department = args['department']
        birthdate = args['birthdate']
        salary = args['salary']
        if not (first_name and last_name and department and birthdate and salary):
            return make_response({'message': 'Incorrect request'}, 400)
        try:
            birthdate = datetime.strptime(birthdate, '%Y/%m/%d')
        except ValueError:
            return make_response({'message': 'Incorrect birthdate'}, 400)
        dep = Department.query.filter_by(name=department).first()
        if not dep:
            return make_response({'message': 'Incorrect department'}, 400)
        try:
            salary = int(salary)
        except ValueError:
            return make_response({'message': 'Incorrect salary'}, 400)
        EmployeeServices.add(
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            department_id=dep.id,
            salary=salary
        )
        return jsonify({
            'first_name': first_name,
            'last_name': last_name,
            'birthdate': datetime.strftime(birthdate, '%Y-%m-%d'),
            'department': department,
            'salary': salary
        },
            201
        )


class EmployeeApi(Resource):
    """
    Employee API.
    """

    @staticmethod
    def get(employee_id):
        """
        GET request handler for employee API.
        :param employee_id: employee id
        :return: employee json representation or error message and status code
        """
        try:
            return jsonify(EmployeeServices.to_dict(employee_id))
        except AttributeError:
            return make_response({'message': 'Employee not found'}, 404)

    @staticmethod
    def put(employee_id):
        """
        PUT request handler for employee API.
        :param employee_id: employee id
        :return: employee json representation or error message and status code
        """
        employee = EmployeeServices.get_by_id(employee_id)
        if not employee:
            return make_response({'message': 'Employee not found'}, 404)
        department_name = DepartmentServices.get_by_id(employee.department_id).name
        parser = reqparse.RequestParser()
        parser.add_argument('first_name')
        parser.add_argument('last_name')
        parser.add_argument('department')
        parser.add_argument('birthdate')
        parser.add_argument('salary')
        args = parser.parse_args()
        first_name = args['first_name'] if args['first_name'] else None
        last_name = args['last_name'] if args['last_name'] else None
        department = args['department'] if args['department'] else department_name
        try:
            birthdate = datetime.strptime(args['birthdate'], '%Y/%m/%d') \
                if args['birthdate'] else None
        except ValueError:
            return make_response({'message': 'Incorrect birthdate'}, 400)
        salary = args['salary'] if args['salary'] else employee.salary
        dep = Department.query.filter_by(name=department).first()
        if not dep:
            return make_response({'message': 'Incorrect department'}, 400)
        try:
            salary = int(salary)
        except ValueError:
            return make_response({'message': 'Incorrect salary'}, 400)
        EmployeeServices.update(
            employee_id=employee_id,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            department_id=dep.id,
            salary=salary
        )
        return jsonify(EmployeeServices.to_dict(employee.id), 201)

    @staticmethod
    def delete(employee_id):
        """
        DELETE request handler for employee API.
        :param employee_id: employee id
        :return: message and status code
        """
        if not EmployeeServices.get_by_id(employee_id):
            return make_response({'message': 'Department not found'}, 404)
        EmployeeServices.delete(employee_id)
        return make_response({'message': 'Department has been successfully deleted'}, 204)
