import pyodbc



class Sales_DAL_Class:
    def __init__(self):
        pass

   # def registerEmployee_DAL(self, employee: EmployeeModel_Class):
   #     connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
   #     commandText = 'EXEC [dbo].[RegisterEmployee] ?,?,?,?,?,?,?,?'
   #     with pyodbc.connect(connectionString) as connection:
   #         cursor = connection.cursor()
   #         cursor.execute(commandText,
   #                        (employee.emp_id, employee.firstName, employee.minit, employee.lastName, employee.job_id
   #                         , employee.job_lvl, employee.pub_id, employee.hire_date))
   #         connection.commit()


    def retrieveAllEmployees(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[RetrieveSales]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()
        return rows