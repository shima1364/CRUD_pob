from DataAccessLayer.Sales_DAL import Sales_DAL_Class
from Model.saleModel import SaleModel_Class


class Sales_BLL_Class:
    def __init__(self):
        pass

    def getSalesList(self):
        sales_DAL_Object = Sales_DAL_Class()
        return sales_DAL_Object.retrieveSales()

    def registerSales(self, sales: SaleModel_Class):
        sales_DAL_Object = Sales_DAL_Class()
        sales_DAL_Object.AddSale_DAL(sales)

    def getStoresNames(self):
        self.SalesDLL = Sales_DAL_Class()
        return self.SalesDLL.retrieveStoresNames()

    def getTitlesNames(self):
        self.SalesDLL = Sales_DAL_Class()
        return self.SalesDLL.retrieveTitlesNames()
