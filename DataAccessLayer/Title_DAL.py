import pyodbc
from Model.Title_Model import TitleModel_Class


class Title_DAL_Class:
    def __init__(self):
        pass

    def registerTitle_DAL(self, title: TitleModel_Class):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[AddTitle] ?,?,?,?,?,?,?,?,?,?'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText,
                           (title.title_id, title.title, title.type, title.pub_id, title.price
                            , title.advance, title.royalty, title.ytd_sales, title.notes, title.pubdate))
            connection.commit()


    def retrieveTitles(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = '[dbo].[RetrieveTitles]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()
        return rows
