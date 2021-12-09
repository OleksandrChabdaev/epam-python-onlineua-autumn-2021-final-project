from flask import redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from department_app import app
from department_app.models.department import Department
from department_app.service.department_service import DepartmentServices
from department_app.service.employee_service import EmployeeServices
from department_app.views.employee_view import EmployeeForm


class DepartmentForm(FlaskForm):
    name = StringField('Department name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
@app.route('/departments/', methods=['GET', 'POST'])
def show_departments():
    departments = DepartmentServices.get_all()
    return render_template('departments.html', departments=departments)


@app.route('/department/<int:department_id>', methods=['GET', 'POST'])
def show_department(department_id):
    department = DepartmentServices.get_by_id(department_id)
    employees = EmployeeServices.get_all_for_department(department_id)
    return render_template('department.html', department_name=department.name, employees=employees)


@app.route('/departments/add/', methods=['GET', 'POST'])
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        for dep in DepartmentServices.get_all():
            if form.name.data == dep.name:
                return redirect(url_for('add_department'))
        DepartmentServices.add(name=form.name.data)
        EmployeeForm.update_departments_list()
        return redirect(url_for('show_departments'))
    return render_template('add_department.html', form=form)


@app.route('/departments/edit/<int:department_id>', methods=['GET', 'POST'])
def edit_department(department_id):
    department = Department.query.get_or_404(department_id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        for dep in DepartmentServices.get_all():
            if form.name.data == dep.name:
                return redirect(url_for('edit_department', department_id=department.id))
        DepartmentServices.update(department_id=department_id, name=form.name.data)
        EmployeeForm.update_departments_list()
        return redirect(url_for('show_departments'))
    form.name.data = department.name
    return render_template('edit_department.html', form=form, department=department)


@app.route('/departments/delete/<int:department_id>', methods=['GET', 'POST'])
def delete_department(department_id):
    DepartmentServices.delete(department_id=department_id)
    EmployeeForm.update_departments_list()
    return redirect(url_for('show_departments'))
