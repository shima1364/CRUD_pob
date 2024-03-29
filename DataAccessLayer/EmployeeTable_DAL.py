import pyodbc



class EmployeeTable_DAL_Class:
    def __init__(self):
        pass

    def retrieveAllEmployees(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[RetrieveAllEmployees]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()
        return rows