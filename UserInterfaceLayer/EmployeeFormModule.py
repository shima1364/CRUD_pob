from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from BusinessLogicLayer.EmployeeCRUD_BLL import EmployeeCRUD_BLL_Class
from Model.EmployeeModel import EmployeeModel_Class


class EmployeeFormClass:
    def __init__(self):
        pass

    def employeeCRUDFormload(self):
        employeeFormObject = Tk()
        employeeFormObject.title('Employee Form')
        employeeFormObject.geometry('1000x735')
        employeeFormObject.configure(bg='#cff5ff')
        employeeFormObject.iconbitmap('images/employeeIcon.ico')
        employeeFormObject.resizable(0, 0)
        x = int(employeeFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(employeeFormObject.winfo_screenheight() / 2 - 400 / 2)
        employeeFormObject.geometry('+{}+{}'.format(x, y))

        def employeeRegister():
            emp_id = txtemp_id.get()
            firstName = txtfirstName.get()
            minit = txtminit.get()
            lastName = txtlastName.get()
            job_id = txtjob_id.get()
            job_lvl = txtjob_lvl.get()
            pub_id = txtpub_id.get()
            hire_date = txthiredate.get()

            EmployeeModel_Object = EmployeeModel_Class(emp_id=emp_id, fname=firstName, minit=minit,
                                                       lname=lastName,
                                                       job_id=job_id, job_lvl=job_lvl, pub_id=pub_id,
                                                       hire_date=hire_date)

            EmployeeCRUD_BLL_Object = EmployeeCRUD_BLL_Class()
            EmployeeCRUD_BLL_Object.registerEmployee(EmployeeModel_Object)
            resetForm()

        def resetForm():
            for widget in employeeFormObject.winfo_children():
                if isinstance(widget, ttk.Entry) or isinstance(widget, DateEntry):
                    widget.delete(0, END)

        def retrieve_data():

            EmployeeRetrieve_BLL_Object = EmployeeCRUD_BLL_Class()
            data = EmployeeRetrieve_BLL_Object.getEmployeeList()
            return data

            # Function to populate the treeview widget with retrieved data

        def populate_treeview():
            #   # Retrieve data from the database
            data = retrieve_data()
            # Clear existing treeview data
            for row in tree.get_children():
                tree.delete(row)
            # Insert retrieved data into the treeview
            for row in data:
                values = (row[0], row[1], row[3])
                tree.insert("", "end", values=values)

        # Create the main Tkinter window
        #  def create_gui(self):
        #     employeeTableObject = Tk()
        #    employeeTableObject.title('Employee Table')
        #    employeeTableObject.geometry('400x400')
        #   employeeTableObject.iconbitmap('images/employeeIcon.ico')
        #  employeeTableObject.resizable(0, 0)
        # x = int(employeeTableObject.winfo_screenwidth() / 2 - 400 / 2)
        # y = int(employeeTableObject.winfo_screenheight() / 2 - 400 / 2)
        # employeeTableObject.geometry('+{}+{}'.format(x, y))

        # Create a Treeview widget
        # self.tree = ttk.Treeview(employeeTableObject, columns=(
        #   'Employee ID', 'First Name', 'Last Name', 'Job ID', 'Job Level', 'Pub ID', 'Hire Date'))
        # self.tree.heading('#0', text='Index')
        # self.tree.heading('#1', text='Employee ID')
        # self.tree.heading('#2', text='First Name')
        # self.tree.heading('#3', text='Last Name')
        # self.tree.heading('#4', text='Job ID')
        # self.tree.heading('#5', text='Job Level')
        # self.tree.heading('#6', text='Pub ID')
        # self.tree.heading('#7', text='Hire Date')
        # self.tree.pack(expand=True, fill='both')

        # Button to retrieve and display data
        # retrieve_button = ttk.Button(employeeTableObject, text="Retrieve Data", command=self.populate_treeview)
        # retrieve_button.pack(pady=10)

        lblemp_id = Label(employeeFormObject, text='emp_id: ')
        lblemp_id.grid(row=0, column=0, padx=10, pady=10)
        txtemp_id = StringVar()
        entemp_id = ttk.Entry(employeeFormObject, width=40, textvariable=txtemp_id)
        entemp_id.grid(row=0, column=1, padx=10, pady=10)

        lblfirstName = Label(employeeFormObject, text='FirstName: ')
        lblfirstName.grid(row=1, column=0, padx=10, pady=10)
        txtfirstName = StringVar()
        entfirstName = ttk.Entry(employeeFormObject, width=40, textvariable=txtfirstName)
        entfirstName.grid(row=1, column=1, padx=10, pady=10)

        lblminit = Label(employeeFormObject, text='minit: ')
        lblminit.grid(row=2, column=0, padx=10, pady=10)
        txtminit = StringVar()
        entminit = ttk.Entry(employeeFormObject, width=40, textvariable=txtminit)
        entminit.grid(row=2, column=1, padx=10, pady=10)

        lbllastName = Label(employeeFormObject, text='lastName: ')
        lbllastName.grid(row=3, column=0, padx=10, pady=10)
        txtlastName = StringVar()
        entlastName = ttk.Entry(employeeFormObject, width=40, textvariable=txtlastName)
        entlastName.grid(row=3, column=1, padx=10, pady=10)

        lbljob_id = Label(employeeFormObject, text='job_id: ')
        lbljob_id.grid(row=4, column=0, padx=10, pady=10)
        txtjob_id = IntVar()
        entjob_id = ttk.Entry(employeeFormObject, width=40, textvariable=txtjob_id)
        entjob_id.grid(row=4, column=1, padx=10, pady=10)

        lbljob_lvl = Label(employeeFormObject, text='job_lvl: ')
        lbljob_lvl.grid(row=5, column=0, padx=10, pady=10)
        txtjob_lvl = IntVar()
        entjob_lvl = ttk.Entry(employeeFormObject, width=40, textvariable=txtjob_lvl)
        entjob_lvl.grid(row=5, column=1, padx=10, pady=10)

        lblpub_id = Label(employeeFormObject, text='pub_id: ')
        lblpub_id.grid(row=6, column=0, padx=10, pady=10)
        txtpub_id = IntVar()
        entpub_id = ttk.Entry(employeeFormObject, width=40, textvariable=txtpub_id)
        entpub_id.grid(row=6, column=1, padx=10, pady=10)

        lblhiredate = Label(employeeFormObject, text='hiredate: ')
        lblhiredate.grid(row=7, column=0, padx=10, pady=10)
        txthiredate = StringVar()
        enthiredate = DateEntry(employeeFormObject, width=36, textvariable=txthiredate)
        enthiredate.grid(row=7, column=1, padx=10, pady=10)

        btnEmployeeRegister = ttk.Button(employeeFormObject, text='Employee Register... ', width=20,
                                         command=employeeRegister)
        btnEmployeeRegister.grid(row=8, column=1, padx=10, pady=20, sticky='e')

        btnResetForm = ttk.Button(employeeFormObject, text='ResetForm', width=16, command=resetForm)
        btnResetForm.grid(row=8, column=1, padx=10, pady=20, sticky='w')

        tree = ttk.Treeview(employeeFormObject, columns=(
            'Employee ID', 'First Name', 'Last Name'), show='headings')
        tree.heading('Employee ID', text='Employee ID')
        tree.heading('First Name', text='First Name')
        tree.heading('Last Name', text='Last Name')
        tree.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

        btnRefresh = ttk.Button(employeeFormObject, text='Refresh Table', width=16, command=populate_treeview)
        btnRefresh.grid(row=10, column=1, padx=10, pady=20)

        populate_treeview()

        employeeFormObject.mainloop()

