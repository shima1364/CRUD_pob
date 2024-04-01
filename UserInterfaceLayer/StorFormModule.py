from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from BusinessLogicLayer.Stor_BLL import Stor_BLL_Class
from Model.StorModel import StorModel_Class


class StorFormClass:
    def __init__(self):
        pass

    def storFormload(self):
        storFormObject = Tk()
        storFormObject.title('Stor Form')
        storFormObject.geometry('700x735')
        storFormObject.configure(bg='#cff5ff')
        storFormObject.iconbitmap('images/employeeIcon.ico')
        storFormObject.resizable(0, 0)
        x = int(storFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(storFormObject.winfo_screenheight() / 2 - 400 / 2)
        storFormObject.geometry('+{}+{}'.format(x, y))

        def storRegister():
            stor_id = txtstor_id.get()
            stor_name = txtstor_name.get()
            stor_address = txtstor_address.get()
            city = txtcity.get()
            state = txtstate.get()
            zip = txtzip.get()

            StorModel_Object = StorModel_Class(stor_id=stor_id, stor_name=stor_name, stor_address=stor_address,
                                               city=city, state=state, zip=zip)

            Stor_BLL_Object = Stor_BLL_Class()
            Stor_BLL_Object.registerStor(StorModel_Object)
            resetForm()

        def resetForm():
            for widget in storFormObject.winfo_children():
                if isinstance(widget, ttk.Entry) or isinstance(widget, DateEntry):
                    widget.delete(0, END)

        def retrieve_data():

            Stor_BLL_Object = Stor_BLL_Class()
            data = Stor_BLL_Object.getStoresList()
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
                values = (row[1], row[2], row[3])
                tree.insert("", "end", values=values)

        lblstor_id = Label(storFormObject, text='stor_id: ')
        lblstor_id.grid(row=0, column=0, padx=10, pady=10)
        txtstor_id = IntVar()
        entstor_id = ttk.Entry(storFormObject, width=40, textvariable=txtstor_id)
        entstor_id.grid(row=0, column=1, padx=10, pady=10)

        lblstor_name = Label(storFormObject, text='stor_name: ')
        lblstor_name.grid(row=1, column=0, padx=10, pady=10)
        txtstor_name = StringVar()
        entstor_name = ttk.Entry(storFormObject, width=40, textvariable=txtstor_name)
        entstor_name.grid(row=1, column=1, padx=10, pady=10)

        lblstor_address = Label(storFormObject, text='stor_address: ')
        lblstor_address.grid(row=2, column=0, padx=10, pady=10)
        txtstor_address = StringVar()
        entstor_address = ttk.Entry(storFormObject, width=40, textvariable=txtstor_address)
        entstor_address.grid(row=2, column=1, padx=10, pady=10)

        lblcity = Label(storFormObject, text='city: ')
        lblcity.grid(row=3, column=0, padx=10, pady=10)
        txtcity = StringVar()
        entcity = ttk.Entry(storFormObject, width=40, textvariable=txtcity)
        entcity.grid(row=3, column=1, padx=10, pady=10)

        lblstate = Label(storFormObject, text='state: ')
        lblstate.grid(row=4, column=0, padx=10, pady=10)
        txtstate = StringVar()
        entstate = ttk.Entry(storFormObject, width=40, textvariable=txtstate)
        entstate.grid(row=4, column=1, padx=10, pady=10)

        lblzip = Label(storFormObject, text='zip: ')
        lblzip.grid(row=5, column=0, padx=10, pady=10)
        txtzip = IntVar()
        entzip = ttk.Entry(storFormObject, width=40, textvariable=txtzip)
        entzip.grid(row=5, column=1, padx=10, pady=10)

        btnStorRegister = ttk.Button(storFormObject, text='Stor Register... ', width=20,
                                     command=storRegister)
        btnStorRegister.grid(row=10, column=1, padx=10, pady=20, sticky='e')

        btnResetForm = ttk.Button(storFormObject, text='ResetForm', width=16, command=resetForm)
        btnResetForm.grid(row=10, column=1, padx=10, pady=20, sticky='w')

        tree = ttk.Treeview(storFormObject, columns=(
            'Name', 'Address', 'City'), show='headings')
        tree.heading('Name', text='Name')
        tree.heading('Address', text='Address')
        tree.heading('City', text='City')
        tree.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

        btnRefresh = ttk.Button(storFormObject, text='Refresh Table', width=16, command=populate_treeview)
        btnRefresh.grid(row=12, column=1, padx=10, pady=20)

        populate_treeview()

        storFormObject.mainloop()
