from datetime import datetime
from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from department_app.models.department import Department
from department_app.service.department_service import DepartmentServices
from department_app.service.employee_service import EmployeeServices


class EmployeeSearchApi(Resource):

    @staticmethod
    def get():
        parser = reqparse.RequestParser()
        parser.add_argument('date_from')
        parser.add_argument('date_to')
        args = parser.parse_args()
        try:
            date_from = datetime.strptime(args['date_from'], '%Y-%m-%d').date()
            date_to = datetime.strptime(args['date_to'], '%Y-%m-%d').date()
        except (ValueError, TypeError):
            return make_response({'message': 'Incorrect date'}, 400)
        employees = EmployeeServices.get_by_birthdate(date_from, date_to)
        return jsonify([EmployeeServices.to_dict(employee.id) for employee in employees])


class EmployeeListApi(Resource):

    @staticmethod
    def get():
        employees = EmployeeServices.get_all()
        return jsonify([EmployeeServices.to_dict(employee.id) for employee in employees])

    @staticmethod
    def post():
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
        dep = Department.query.filter_by(name=department).first()
        if not dep:
            return make_response({'message': 'Incorrect department'}, 400)
        try:
            salary = int(salary)
        except ValueError:
            return make_response({'message': 'Incorrect salary'}, 400)
        try:
            EmployeeServices.add(
                first_name=first_name,
                last_name=last_name,
                birthdate=birthdate,
                department_id=dep.id,
                salary=salary
            )
        except:
            return make_response({'message': 'Incorrect birthdate'}, 400)
        return jsonify({
            'first_name': first_name,
            'last_name': last_name,
            'birthdate': birthdate,
            'department': department,
            'salary': salary
        },
            201
        )


class EmployeeApi(Resource):

    @staticmethod
    def get(employee_id):
        try:
            return jsonify(EmployeeServices.to_dict(employee_id))
        except AttributeError:
            return make_response({'message': 'Employee not found'}, 404)

    @staticmethod
    def put(employee_id):
        if not EmployeeServices.get_by_id(employee_id):
            return make_response({'message': 'Employee not found'}, 404)
        employee = EmployeeServices.get_by_id(employee_id)
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
        birthdate = args['birthdate'] if args['birthdate'] else None
        salary = args['salary'] if args['salary'] else employee.salary
        if not Department.query.filter_by(name=department).first():
            return make_response({'message': 'Incorrect department'}, 400)
        dep = Department.query.filter_by(name=department).first()
        try:
            salary = int(salary)
        except ValueError:
            return make_response({'message': 'Incorrect salary'}, 400)
        try:
            EmployeeServices.update(
                employee_id=employee_id,
                first_name=first_name,
                last_name=last_name,
                birthdate=birthdate,
                department_id=dep.id,
                salary=salary
            )
        except:
            return make_response({'message': 'Incorrect birthdate'}, 400)
        return jsonify(EmployeeServices.to_dict(employee.id), 201)

    @staticmethod
    def delete(employee_id):
        if not EmployeeServices.get_by_id(employee_id):
            return make_response({'message': 'Department not found'}, 404)
        EmployeeServices.delete(employee_id)
        return make_response({'message': 'Department has been successfully deleted'}, 204)
