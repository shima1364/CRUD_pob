from DataAccessLayer.Sales_DAL import Sales_DAL_Class


class Sales_BLL_Class:
    def __init__(self):
        pass

    def getSalesList(self):
       self.SalesDLL = Sales_DAL_Class()
       return self.SalesDLL.retrieveSales()

    #def registerEmployee(self, employee: EmployeeModel_Class):
    #    EmployeeCRUD_DAL_Object = EmployeeCRUD_DAL_Class()
    #    EmployeeCRUD_DAL_Object.registerEmployee_DAL(employee)