from tkinter import *
from .EmployeeFormModule import EmployeeFormClass
from .AuthorsFormModule import AuthorFormClass
from .SalesTable import SaleFormClass
from .TitleFormModule import TitleFormClass
from .StorFormModule import StorFormClass


class ShareFormClass:
    def mainFormLoad(self, fname, lname):
        shareFormObject = Tk()
        shareFormObject.title('Main Form')
        shareFormObject.geometry('400x400')
        shareFormObject.iconbitmap('images/mainIcon.ico')
        shareFormObject.resizable(0, 0)
        x = int(shareFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(shareFormObject.winfo_screenheight() / 2 - 400 / 2)
        shareFormObject.geometry('+{}+{}'.format(x, y))

        def employeeFormLoad():
            shareFormObject.destroy()
            employeeFormObject = EmployeeFormClass()
            employeeFormObject.employeeCRUDFormload()

        def authorFormLoad():
            shareFormObject.destroy()
            authorFormObject = AuthorFormClass()
            authorFormObject.authorFormload()

        def salesFormLoad():
            shareFormObject.destroy()
            salesFormObject = SaleFormClass()
            salesFormObject.salesFormload()

        def titleFormLoad():
            shareFormObject.destroy()
            titleFormObject = TitleFormClass()
            titleFormObject.TitleFormload()

        def storFormLoad():
            shareFormObject.destroy()
            storFormObject = StorFormClass()
            storFormObject.storFormload()



        # def employeeTableLoad():
        # mainFormObject.destroy()
        # Create a new window or frame to display the retrieved data
        #    employeeTableObject = EmployeeTableClass()
        # Example: Create a new window
        #   employeeTableWindow = Toplevel(employeeTableObject)
        #  employeeTableWindow.title('Employee Table')
        # Add code to display the retrieved data in the new window

        lblWelcomeMessage = Label(shareFormObject, text=f'Welcome {fname} {lname}')
        lblWelcomeMessage.grid(row=0, column=1, padx=10, pady=10)

        btnEmployeeCRUD = Button(shareFormObject, text='Employee CRUD', command=employeeFormLoad)
        btnEmployeeCRUD.grid(row=1, column=0, padx=20, pady=20)

        btnAuthorCRUD = Button(shareFormObject, text='Author CRUD', command=authorFormLoad)
        btnAuthorCRUD.grid(row=2, column=0, padx=20, pady=20)

        btnSales = Button(shareFormObject, text='Sales', command=salesFormLoad)
        btnSales.grid(row=3, column=0, padx=20, pady=20)

        btnTitle = Button(shareFormObject, text='Title', command=titleFormLoad)
        btnTitle.grid(row=4, column=0, padx=20, pady=20)

        btnStor = Button(shareFormObject, text='Stor', command=storFormLoad)
        btnStor.grid(row=5, column=0, padx=20, pady=20)
        shareFormObject.mainloop()