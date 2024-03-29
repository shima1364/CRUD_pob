from DataAccessLayer.EmployeeCRUD_DAL import EmployeeCRUD_DAL_Class
from Model.EmployeeModel import EmployeeModel_Class

class EmployeeCRUD_BLL_Class:
    def __init__(self):
        pass

    def getEmployeeList(self):
       self.EmployeeDAL = EmployeeCRUD_DAL_Class()
       return self.EmployeeDAL.retrieveAllEmployees()

    def registerEmployee(self, employee: EmployeeModel_Class):
        EmployeeCRUD_DAL_Object = EmployeeCRUD_DAL_Class()
        EmployeeCRUD_DAL_Object.registerEmployee_DAL(employee)
