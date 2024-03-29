from tkinter import *
from tkinter import ttk
from DataAccessLayer.EmployeeTable_DAL import EmployeeTable_DAL_Class


class EmployeeTableClass:
    def __init__(self):
        pass

    def retrieve_data(self):
        # Create an instance of the DAL class
        employee_dal = EmployeeTable_DAL_Class()
        # Retrieve data from the database
        data = employee_dal.retrieve_data()

        return data

    # Function to populate the treeview widget with retrieved data
    def populate_treeview(self):
        # Retrieve data from the database
        data = self.retrieve_data()
        # Clear existing treeview data
        for row in self.tree.get_children():
            self.tree.delete(row)
        # Insert retrieved data into the treeview
        for row in data:
            self.tree.insert('', 'end', values=row)

    # Create the main Tkinter window
    def create_gui(self):
        employeeTableObject = Tk()
        employeeTableObject.title('Employee Table')
        employeeTableObject.geometry('400x400')
        employeeTableObject.iconbitmap('images/employeeIcon.ico')
        employeeTableObject.resizable(0, 0)
        x = int(employeeTableObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(employeeTableObject.winfo_screenheight() / 2 - 400 / 2)
        employeeTableObject.geometry('+{}+{}'.format(x, y))

        # Create a Treeview widget
        self.tree = ttk.Treeview(employeeTableObject, columns=(
        'Employee ID', 'First Name', 'Last Name', 'Job ID', 'Job Level', 'Pub ID', 'Hire Date'))
        self.tree.heading('#0', text='Index')
        self.tree.heading('#1', text='Employee ID')
        self.tree.heading('#2', text='First Name')
        self.tree.heading('#3', text='Last Name')
        self.tree.heading('#4', text='Job ID')
        self.tree.heading('#5', text='Job Level')
        self.tree.heading('#6', text='Pub ID')
        self.tree.heading('#7', text='Hire Date')
        self.tree.pack(expand=True, fill='both')

        # Button to retrieve and display data
        retrieve_button = ttk.Button(employeeTableObject, text="Retrieve Data", command=self.populate_treeview)
        retrieve_button.pack(pady=10)

        # Start the Tkinter event loop
        employeeTableObject.mainloop()
