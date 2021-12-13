"""
Defines department and employee REST API.
"""
from department_app import api
from . import department_api
from . import employee_api


def init_api():
    """
    Initializes REST API endpoints.
    :return: None
    """
    api.add_resource(
        department_api.DepartmentListApi,
        '/api/departments',
        strict_slashes=False
    )
    api.add_resource(
        department_api.DepartmentApi,
        '/api/department/<department_id>',
        strict_slashes=False
    )
    api.add_resource(
        employee_api.EmployeeListApi,
        '/api/employees',
        strict_slashes=False
    )
    api.add_resource(
        employee_api.EmployeeApi,
        '/api/employee/<employee_id>',
        strict_slashes=False
    )
    api.add_resource(
        employee_api.EmployeeSearchApi,
        '/api/employees/search',
        strict_slashes=False
    )
