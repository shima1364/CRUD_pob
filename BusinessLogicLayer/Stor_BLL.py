from DataAccessLayer.Stor_DAL import Stor_DAL_Class
from Model.StorModel import StorModel_Class


class Stor_BLL_Class:
    def __init__(self):
        pass

    def getStoresList(self):
        self.StorDAL = Stor_DAL_Class()
        return self.StorDAL.retrieveStores()

    def registerStor(self, stor: StorModel_Class):
        stor_DAL_Object = Stor_DAL_Class()
        stor_DAL_Object.registerStor_DAL(stor)
