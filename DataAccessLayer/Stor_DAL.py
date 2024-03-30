import pyodbc
from Model.StorModel import StorModel_Class


class Stor_DAL_Class:
    def __init__(self):
        pass

    def registerStor_DAL(self, stor: StorModel_Class):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[AddStore] ?,?,?,?,?,?'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText,
                           (stor.stor_id, stor.stor_name, stor.stor_address, stor.city, stor.state
                            , stor.zip))
            connection.commit()


    def retrieveStores(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = '[dbo].[RetrieveStores]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()
        return rows
