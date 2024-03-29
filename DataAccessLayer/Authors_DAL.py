import pyodbc
from Model.AuthorsModel import AuthorsModel_Class


class Author_DAL_Class:
    def __init__(self):
        pass

    def registerEmployee_DAL(self, author=AuthorsModel_Class):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[RegisterAuthor] ?,?,?,?,?,?,?,?,?'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText,
                           (author.au_id, author.au_lname, author.au_fname, author.phone, author.address
                            , author.city, author.state, author.zip, author.contract))
            connection.commit()

    def retrieveAuthors(self):
        connectionString = 'Driver={SQL Server};Server=localhost;Database=pubs;Trusted_Connection=yes;'
        commandText = 'EXEC [dbo].[RetrieveAllAuthors]'
        with pyodbc.connect(connectionString) as connection:
            cursor = connection.cursor()
            cursor.execute(commandText)
            rows = cursor.fetchall()
        return rows
