from tkinter import *
from .EmployeeFormModule import EmployeeFormClass
from .AuthorsFormModule import AuthorFormClass
from .SalesTable import SaleFormClass
from .TitleFormModule import TitleFormClass
from .StorFormModule import StorFormClass
from tkinter import ttk

class MainFormClass:
    def mainFormLoad(self, fname, lname):
        mainFormObject = Tk()
        mainFormObject.title('Main Form')
        mainFormObject.geometry('500x600')
        mainFormObject.iconbitmap('images/mainIcon.ico')
        mainFormObject.resizable(0, 0)

        # Calculate the center position
        x = int(mainFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(mainFormObject.winfo_screenheight() / 2 - 400 / 2)
        mainFormObject.geometry('+{}+{}'.format(x, y))

        # Function to center the window
        def center_window(window):
            window.update_idletasks()
            width = window.winfo_width()
            height = window.winfo_height()
            x_pos = (window.winfo_screenwidth() // 2) - (width // 2)
            y_pos = (window.winfo_screenheight() // 2) - (height // 2)
            window.geometry('{}x{}+{}+{}'.format(width, height, x_pos, y_pos))

        # Apply custom styles to buttons
        style = ttk.Style()
        style.configure("Main.TButton", font=("Helvetica", 12), foreground="black", background="#d9d9d9", padx=20, pady=10)

        def employeeFormLoad():
            employeeFormObject = EmployeeFormClass()
            employeeFormObject.employeeCRUDFormload()

        def authorFormLoad():
            authorFormObject = AuthorFormClass()
            authorFormObject.authorFormload()

        def salesFormLoad():
            salesFormObject = SaleFormClass()
            salesFormObject.salesFormload()

        def titleFormLoad():
            titleFormObject = TitleFormClass()
            titleFormObject.TitleFormload()

        def storFormLoad():
            storFormObject = StorFormClass()
            storFormObject.storFormload()

        lblWelcomeMessage = Label(mainFormObject, text=f'Welcome {fname} {lname}')
        lblWelcomeMessage.grid(row=0, padx=10, pady=10, columnspan=2)
        employeeCRUD = PhotoImage(file='images/Employee_icon.png')
        btnEmployeeCRUD = ttk.Button(mainFormObject, text='Employee CRUD', command=employeeFormLoad, style="Main.TButton", image=employeeCRUD)
        btnEmployeeCRUD.grid(row=1, column=0, padx=20, pady=20, sticky='we')
        author_icon = PhotoImage(file='images/author_icon.png')
        btnAuthorCRUD = ttk.Button(mainFormObject, text='Author CRUD', command=authorFormLoad, style="Main.TButton", image=author_icon)
        btnAuthorCRUD.grid(row=1, column=1, padx=20, pady=20, sticky='we')
        sale_Icon = PhotoImage(file='images/Sales_icon.png')
        btnSales = ttk.Button(mainFormObject, text='Sales', command=salesFormLoad, style="Main.TButton", image=sale_Icon)
        btnSales.grid(row=2, column=0, padx=20, pady=20, sticky='we')
        title_Icon = PhotoImage(file='images/Titles_icon.png')
        btnTitle = ttk.Button(mainFormObject, text='Title', command=titleFormLoad, style="Main.TButton",image=title_Icon)
        btnTitle.grid(row=2, column=1, padx=20, pady=20, sticky='we')
        store_Icon = PhotoImage(file='images/Store_icon.png')
        btnStor = ttk.Button(mainFormObject, text='Stor', command=storFormLoad, style="Main.TButton", image=store_Icon)
        btnStor.grid(row=3, column=0, padx=20, pady=20, columnspan=2, sticky='we')

        # Center the window after widgets are added
        center_window(mainFormObject)

        mainFormObject.mainloop()

