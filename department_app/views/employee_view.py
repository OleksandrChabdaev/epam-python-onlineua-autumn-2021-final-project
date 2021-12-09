from flask import redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, SelectField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from department_app import app, db
from department_app.models.department import Department
from department_app.models.employee import Employee
from department_app.service.employee_service import EmployeeServices


class EmployeeForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    department = SelectField(choices=[department.name for department in Department.query.all()])
    birthdate = DateField('Birthdate', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    submit = SubmitField('Submit')

    @classmethod
    def update_departments_list(cls):
        cls.department = SelectField(choices=[department.name for department in Department.query.all()])


class SearchForm(FlaskForm):
    date_from = DateField('Birthdate From', validators=[DataRequired()])
    date_to = DateField('Birthdate To', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/employees/', methods=['GET', 'POST'])
def show_employees():
    employees = EmployeeServices.get_all()
    return render_template('employees.html', employees=employees)


@app.route('/employee/<int:employee_id>', methods=['GET', 'POST'])
def show_employee(employee_id):
    employee = EmployeeServices.get_by_id(employee_id)
    return render_template('employee.html', employee=employee)


@app.route('/search/', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        date_from = form.date_from.data
        date_to = form.date_to.data
        employees = EmployeeServices.get_by_birthdate(date_from, date_to)
        return render_template('employees.html', employees=employees)
    return render_template('search.html', form=form)


@app.route('/employees/add/', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        dep = Department.query.filter_by(name=form.department.data).first()
        EmployeeServices.add(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            birthdate=form.birthdate.data,
            department_id=dep.id,
            salary=form.salary.data
        )
        return redirect(url_for('show_employees'))
    return render_template('add_employee.html', form=form)


@app.route('/employees/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    form = EmployeeForm(obj=employee)
    if form.validate_on_submit():
        dep = Department.query.filter_by(name=form.department.data).first()
        EmployeeServices.update(
            employee_id=employee_id,
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            birthdate=form.birthdate.data,
            department_id=dep.id,
            salary=form.salary.data
        )
        return redirect(url_for('show_employees'))
    form.first_name.data = employee.first_name
    form.last_name.data = employee.last_name
    form.birthdate.data = employee.birthdate
    form.department.data = Department.query.filter_by(id=employee.department_id).first().name
    form.salary.data = employee.salary
    return render_template('edit_employee.html', form=form, employee=employee)


@app.route('/employees/delete/<int:employee_id>', methods=['GET', 'POST'])
def delete_employee(employee_id):
    EmployeeServices.delete(employee_id=employee_id)
    return redirect(url_for('show_employees'))
