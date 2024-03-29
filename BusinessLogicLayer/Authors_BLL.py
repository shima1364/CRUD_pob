from DataAccessLayer.Authors_DAL import Author_DAL_Class
from Model.AuthorsModel import AuthorsModel_Class

class Author_BLL_Class:
    def __init__(self):
        pass

    def getAuthorList(self):
       self.AuthorsDAL= Author_DAL_Class()
       return self.AuthorsDAL.retrieveAuthors()

    def registerAuthor(self, author: AuthorsModel_Class):
        AuthorDALObject = Author_DAL_Class()
        AuthorDALObject.registerEmployee_DAL(author)