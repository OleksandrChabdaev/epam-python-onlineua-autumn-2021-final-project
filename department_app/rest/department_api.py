"""
Defines department REST API.
"""
# pylint: disable=cyclic-import
from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from department_app.models.department import Department
from department_app.service.department_service import DepartmentServices


class DepartmentListApi(Resource):
    """
    Department list API.
    """

    @staticmethod
    def get():
        """
        GET request handler for department list API.
        :return: department list json representation
        """
        departments = DepartmentServices.get_all()
        return jsonify([DepartmentServices.to_dict(department.id) for department in departments])

    @staticmethod
    def post():
        """
        POST request handler for department list API.
        :return: department json representation or error message and status code
        """
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        name = args['name']
        if not name:
            return make_response({'message': 'Incorrect request'}, 400)
        for department in DepartmentServices.get_all():
            if name == department.name:
                return make_response({'message': 'Department already exists'}, 406)
        DepartmentServices.add(name)
        department = Department.query.filter_by(name=name).first()
        return jsonify(DepartmentServices.to_dict(department.id), 201)


class DepartmentApi(Resource):
    """
    Department API.
    """

    @staticmethod
    def get(department_id):
        """
        GET request handler for department API.
        :param department_id: department id
        :return: department json representation or error message and status code
        """
        try:
            department = DepartmentServices.get_by_id(department_id)
            return jsonify(DepartmentServices.to_dict(department.id))
        except AttributeError:
            return make_response({'message': 'Department not found'}, 404)

    @staticmethod
    def put(department_id):
        """
        PUT request handler for department API.
        :param department_id: department id
        :return: department json representation or error message and status code
        """
        if not DepartmentServices.get_by_id(department_id):
            return make_response({'message': 'Department not found'}, 404)
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        args = parser.parse_args()
        name = args['name']
        if not name:
            return make_response({'message': 'Incorrect request'}, 400)
        for department in DepartmentServices.get_all():
            if name == department.name:
                return make_response({'message': 'Department already exists'}, 406)
        DepartmentServices.update(department_id=department_id, name=name)
        return jsonify(DepartmentServices.to_dict(department_id), 201)

    @staticmethod
    def delete(department_id):
        """
        DELETE request handler for department API.
        :param department_id: department id
        :return: message and status code
        """
        if not DepartmentServices.get_by_id(department_id):
            return make_response({'message': 'Department not found'}, 404)
        DepartmentServices.delete(department_id)
        return make_response({'message': 'Department has been successfully deleted'}, 204)
