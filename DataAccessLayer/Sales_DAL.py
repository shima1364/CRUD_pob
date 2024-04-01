import pyodbc
from Model.saleModel import SaleModel_Class



class Sales_DAL_Class:
    def __init__(self):
        pass

    def AddSale_DAL(self, order: SaleModel_Class):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[AddingToSalesList] ?,?,?,?,?,?'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText,
                           (order.stor_id, order.ord_num, order.ord_date, order.qty, order.payterms
                            , order.title_id))
            connection.commit()


    def retrieveSales(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[RetrieveSales]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()
        return rows
    def retrieveTitlesNames(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[TitlesInfo]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()

        return rows

    def retrieveStoresNames(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[StoresInfo]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()

        return rows