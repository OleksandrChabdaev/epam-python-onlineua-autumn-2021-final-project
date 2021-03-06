"""
Defines employee web application view.
"""
# pylint: disable=cyclic-import
from datetime import datetime
import requests
from flask import redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from department_app import app

HOST = 'http://127.0.0.1:5000/'


class EmployeeForm(FlaskForm):
    """
    User form to manage employees.
    """

    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    department = SelectField(choices=[''])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    submit = SubmitField('Submit')

    @classmethod
    def update_departments_list(cls):
        """
        Updates department list from database.
        :return: None
        """
        url = f'{HOST}api/departments'
        departments = requests.get(url).json()
        cls.department = SelectField(choices=[department['name'] for department in departments])


class SearchForm(FlaskForm):
    """
    User form to search employees.
    """
    date_from = DateField('Birthdate From', validators=[DataRequired()])
    date_to = DateField('Birthdate To', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/employees/', methods=['GET'])
def show_employees():
    """
    Returns rendered template to show all employees.
    :return: rendered template to show all employees
    """
    url = f'{HOST}api/employees'
    employees = requests.get(url).json()
    return render_template('employees.html', employees=employees)


@app.route('/employee/<int:employee_id>', methods=['GET'])
def show_employee(employee_id):
    """
    Returns rendered template to show employee.
    :param employee_id: employee id
    :return: rendered template to show employee
    """
    url = f'{HOST}api/employee/{employee_id}'
    employee = requests.get(url).json()
    return render_template('employee.html', employee=employee)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    """
    Returns rendered template to search employees.
    :return: rendered template to search employees
    """
    form = SearchForm()
    if form.validate_on_submit():
        date_from = datetime.strftime(form.date_from.data, '%Y/%m/%d')
        date_to = datetime.strftime(form.date_to.data, '%Y/%m/%d')
        url = f'{HOST}api/employees/search'
        querystring = {'date_from': date_from, 'date_to': date_to}
        employees = requests.get(url, params=querystring).json()
        return render_template('employees.html', employees=employees)
    return render_template('search.html', form=form)


@app.route('/employees/add/', methods=['GET', 'POST'])
def add_employee():
    """
    Returns rendered template to add employee.
    :return: rendered template to add employee
    """
    EmployeeForm.update_departments_list()
    form = EmployeeForm()
    if form.validate_on_submit():
        url = f'{HOST}api/employees'
        requests.post(url, data={
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'birthdate': datetime.strftime(form.birthdate.data, '%Y/%m/%d'),
            'department': form.department.data,
            'salary': form.salary.data
        }).json()
        return redirect(url_for('show_employees'))
    return render_template('add_employee.html', form=form)


@app.route('/employees/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    """
    Returns rendered template to edit employee.
    :param employee_id: employee id
    :return: rendered template to edit employee
    """
    url = f'{HOST}api/employee/{employee_id}'
    employee = requests.get(url).json()
    EmployeeForm.update_departments_list()
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        url = f'{HOST}api/employee/{employee_id}'
        requests.put(url, data={
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'birthdate': datetime.strftime(form.birthdate.data, '%Y/%m/%d'),
            'department': form.department.data,
            'salary': form.salary.data
        }).json()
        return redirect(url_for('show_employees'))
    form.first_name.data = employee['first_name']
    form.last_name.data = employee['last_name']
    form.birthdate.data = datetime.strptime(employee['birthdate'], '%Y-%m-%d')
    form.department.data = employee['department']
    form.salary.data = employee['salary']
    return render_template('edit_employee.html', form=form, employee=employee)


@app.route('/employees/delete/<int:employee_id>', methods=['GET'])
def delete_employee(employee_id):
    """
    Returns rendered template to delete employee.
    :param employee_id: employee id
    :return: rendered template to delete employee
    """
    url = f'{HOST}api/employee/{employee_id}'
    requests.delete(url)
    return redirect(url_for('show_employees'))
