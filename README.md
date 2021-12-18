# Department App

[![Build Status](https://app.travis-ci.com/OleksandrChabdaev/epam-python-onlineua-autumn-2021-final-project.svg?token=qu38tUNAjjD9AzqYnRJQ&branch=master)](https://app.travis-ci.com/OleksandrChabdaev/epam-python-onlineua-autumn-2021-final-project)
[![Coverage Status](https://coveralls.io/repos/github/OleksandrChabdaev/epam-python-onlineua-autumn-2021-final-project/badge.svg?branch=master)](https://coveralls.io/github/OleksandrChabdaev/epam-python-onlineua-autumn-2021-final-project?branch=master)
## Description

Simple web application for managing departments and employees. It uses RESTful web service to perform CRUD operations.
The web application allows:
- display a list of departments and the average salary (calculated automatically) for these departments;
- display a list of employees in the departments with an indication of the salary for each employee and search fields
to search for employees born in the period between dates;
- change (add / edit / delete) the above data.

## Build project

Install requirements:
```
pip install -r requirements.txt
```
Set environment variables MYSQL_USER, MYSQL_PASSWORD, MYSQL_SERVER, MYSQL_DATABASE.

Run project:
```
python wsgi.py
```

## Web application

Show departments:
```
http://127.0.0.1:5000/
http://127.0.0.1:5000/departments
```
Show department:
```
http://127.0.0.1:5000/department/<id>
```
Add department:
```
http://127.0.0.1:5000/departments/add
```
Edit department:
```
http://127.0.0.1:5000/department/edit/<id>
```
Show employees:
```
http://127.0.0.1:5000/employees
```
Show employee:
```
http://127.0.0.1:5000/employee/<id>
```
Search employees:
```
localhost:5000/search
```
Add employee:
```
http://127.0.0.1:5000/employees/add
```
Edit employee:
```
http://127.0.0.1:5000/employee/edit/<id>
```

## Web service API

Show departments:
```
curl http://127.0.0.1:5000/api/departments
```
Show department:
```
curl http://127.0.0.1:5000/api/department/<id>
```
Add department:
```
curl -d "name=<name>" http://127.0.0.1:5000/api/departments
```
Edit department:
```
curl -X PUT -d "name=<name>" http://127.0.0.1:5000/api/department/<id>
```
Delete department:
```
curl -X DELETE http://127.0.0.1:5000/api/department/<id>
```
Show employees:
```
curl http://127.0.0.1:5000/api/employees
```
Show employee:
```
curl http://127.0.0.1:5000/api/employee/<id>
```
Search employees:
```
curl http://127.0.0.1:5000/api/employees/search?date_from=<%Y/%m/%d>^&date_to=<%Y/%m/%d>
```
Add employee:
```
curl -d "first_name=<first_name>&last_name=<last_name>&department=<department_name>&birthdate=<%Y/%m/%d>&salary=<salary>" http://127.0.0.1:5000/api/employees
```
Edit employee:
```
curl -X PUT -d "first_name=<first_name>&last_name=<last_name>&department=<department_name>&birthdate=<%Y/%m/%d>&salary=<salary>" http://127.0.0.1:5000/api/employee/<id>
```
Delete employee:
```
curl -X DELETE http://127.0.0.1:5000/api/employee/<id>
```
