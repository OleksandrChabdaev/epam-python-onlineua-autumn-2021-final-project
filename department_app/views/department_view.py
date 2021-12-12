import requests
from flask import redirect, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from department_app import app

host = 'http://127.0.0.1:5000/'


class DepartmentForm(FlaskForm):
    name = StringField('Department name', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET'])
@app.route('/departments/', methods=['GET'])
def show_departments():
    url = f'{host}api/departments'
    departments = requests.get(url).json()
    return render_template('departments.html', departments=departments)


@app.route('/department/<int:department_id>', methods=['GET'])
def show_department(department_id):
    url = f'{host}api/department/{department_id}'
    department = requests.get(url).json()
    return render_template('department.html', department=department)


@app.route('/departments/add/', methods=['GET', 'POST'])
def add_department():
    form = DepartmentForm()
    if form.validate_on_submit():
        url = f'{host}api/departments'
        for dep in requests.get(url).json():
            if form.name.data == dep['name']:
                return redirect(url_for('add_department'))
        url = f'{host}api/departments'
        requests.post(url, data={'name': form.name.data}).json()
        return redirect(url_for('show_departments'))
    return render_template('add_department.html', form=form)


@app.route('/departments/edit/<int:department_id>', methods=['GET', 'POST'])
def edit_department(department_id):
    url = f'{host}api/department/{department_id}'
    department = requests.get(url).json()
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        url = f'{host}api/departments'
        for dep in requests.get(url).json():
            if form.name.data == dep['name']:
                return redirect(url_for('edit_department', department_id=department['id']))
        url = f'{host}api/department/{department_id}'
        requests.put(url, data={'name': form.name.data}).json()
        return redirect(url_for('show_departments'))
    form.name.data = department['name']
    return render_template('edit_department.html', form=form, department=department)


@app.route('/departments/delete/<int:department_id>', methods=['GET'])
def delete_department(department_id):
    url = f'{host}api/department/{department_id}'
    requests.delete(url)
    return redirect(url_for('show_departments'))
