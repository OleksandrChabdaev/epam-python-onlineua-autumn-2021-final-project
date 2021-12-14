import unittest
from department_app.tests.department import DepartmentModelTests
from department_app.tests.department_service import DepartmentServiceTests
from department_app.tests.employee import EmployeeModelTests
from department_app.tests.employee_service import EmployeeServiceTests

if __name__ == '__main__':
    appTestSuite = unittest.TestSuite()
    appTestSuite.addTest(unittest.makeSuite(DepartmentModelTests))
    appTestSuite.addTest(unittest.makeSuite(DepartmentServiceTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeModelTests))
    appTestSuite.addTest(unittest.makeSuite(EmployeeServiceTests))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(appTestSuite)
