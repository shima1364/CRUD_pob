from DataAccessLayer.Title_DAL import Title_DAL_Class
from Model.Title_Model import TitleModel_Class


class Title_BLL_Class:
    def __init__(self):
        pass

    def getTitlesList(self):
        self.TitleDAL = Title_DAL_Class()
        return self.TitleDAL.retrieveTitles()

    def registerEmployee(self, title: TitleModel_Class):
        Title_DAL_Object = Title_DAL_Class()
        Title_DAL_Object.registerTitle_DAL(title)
