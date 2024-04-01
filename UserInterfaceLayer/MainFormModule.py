from tkinter import *
from .EmployeeFormModule import EmployeeFormClass
from .AuthorsFormModule import AuthorFormClass
from .SalesTable import SaleFormClass
from .TitleFormModule import TitleFormClass
from .StorFormModule import StorFormClass


class MainFormClass:
    def mainFormLoad(self, fname, lname):
        mainFormObject = Tk()
        mainFormObject.title('Main Form')
        mainFormObject.geometry('400x400')
        mainFormObject.iconbitmap('images/mainIcon.ico')
        mainFormObject.resizable(0, 0)
        x = int(mainFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(mainFormObject.winfo_screenheight() / 2 - 400 / 2)
        mainFormObject.geometry('+{}+{}'.format(x, y))

        def employeeFormLoad():
          #  mainFormObject.destroy()
            employeeFormObject = EmployeeFormClass()
            employeeFormObject.employeeCRUDFormload()

        def authorFormLoad():
           # mainFormObject.destroy()
            authorFormObject = AuthorFormClass()
            authorFormObject.authorFormload()

        def salesFormLoad():
          #  mainFormObject.destroy()
            salesFormObject = SaleFormClass()
            salesFormObject.salesFormload()

        def titleFormLoad():
          #  mainFormObject.destroy()
            titleFormObject = TitleFormClass()
            titleFormObject.TitleFormload()

        def storFormLoad():
          #  mainFormObject.destroy()
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

        lblWelcomeMessage = Label(mainFormObject, text=f'Welcome {fname} {lname}')
        lblWelcomeMessage.grid(row=0, column=1, padx=10, pady=10)

        btnEmployeeCRUD = Button(mainFormObject, text='Employee CRUD', command=employeeFormLoad)
        btnEmployeeCRUD.grid(row=1, column=0, padx=20, pady=20)

        btnAuthorCRUD = Button(mainFormObject, text='Author CRUD', command=authorFormLoad)
        btnAuthorCRUD.grid(row=2, column=0, padx=20, pady=20)

        btnSales = Button(mainFormObject, text='Sales', command=salesFormLoad)
        btnSales.grid(row=3, column=0, padx=20, pady=20)

        btnTitle = Button(mainFormObject, text='Title', command=titleFormLoad)
        btnTitle.grid(row=4, column=0, padx=20, pady=20)

        btnStor = Button(mainFormObject, text='Stor', command=storFormLoad)
        btnStor.grid(row=5, column=0, padx=20, pady=20)
        mainFormObject.mainloop()

