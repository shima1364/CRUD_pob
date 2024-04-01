from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from BusinessLogicLayer.Authors_BLL import Author_BLL_Class
from Model.AuthorsModel import AuthorsModel_Class


class AuthorFormClass:
    def __init__(self):
        pass

    def authorFormload(self):
        authorFormObject = Tk()
        authorFormObject.title('Author Form')
        authorFormObject.geometry('700x735')
        authorFormObject.configure(bg='#cff5ff')
        authorFormObject.iconbitmap('images/employeeIcon.ico')
        authorFormObject.resizable(0, 0)
        x = int(authorFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(authorFormObject.winfo_screenheight() / 2 - 400 / 2)
        authorFormObject.geometry('+{}+{}'.format(x, y))

        def authorRegister():
            au_id = txtau_id.get()
            firstName = txtfirstName.get()
            lastName = txtlastName.get()
            phone = txtphone.get()
            address = txtaddress.get()
            city = txtcity.get()
            state = txtstate.get()
            zip = txtzip.get()
            contract = txtcontract.get()

            AuthorModel_Object = AuthorsModel_Class(au_id=au_id, au_lname=lastName, au_fname=firstName, phone=phone,
                                                    address=address
                                                    , city=city, state=state, zip=zip, contract=contract)

            Author_BLL_Object = Author_BLL_Class()
            Author_BLL_Object.registerAuthor(AuthorModel_Object)
            resetForm()

        def resetForm():
            for widget in authorFormObject.winfo_children():
                if isinstance(widget, ttk.Entry) or isinstance(widget, DateEntry):
                    widget.delete(0, END)

        def retrieve_data():

            AuthorRetrieve_BLL_Object = Author_BLL_Class()
            data = AuthorRetrieve_BLL_Object.getAuthorList()
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
                values = (row[0], row[2], row[1])
                tree.insert("", "end", values=values)


        lblau_id = Label(authorFormObject, text='au_id: ')
        lblau_id.grid(row=0, column=0, padx=10, pady=10)
        txtau_id = StringVar()
        entau_id = ttk.Entry(authorFormObject, width=40, textvariable=txtau_id)
        entau_id.grid(row=0, column=1, padx=10, pady=10)

        lblfirstName = Label(authorFormObject, text='FirstName: ')
        lblfirstName.grid(row=1, column=0, padx=10, pady=10)
        txtfirstName = StringVar()
        entfirstName = ttk.Entry(authorFormObject, width=40, textvariable=txtfirstName)
        entfirstName.grid(row=1, column=1, padx=10, pady=10)

        lbllastName = Label(authorFormObject, text='lastName: ')
        lbllastName.grid(row=3, column=0, padx=10, pady=10)
        txtlastName = StringVar()
        entlastName = ttk.Entry(authorFormObject, width=40, textvariable=txtlastName)
        entlastName.grid(row=3, column=1, padx=10, pady=10)

        lblphone = Label(authorFormObject, text='phone: ')
        lblphone.grid(row=2, column=0, padx=10, pady=10)
        txtphone = IntVar()
        entphone = ttk.Entry(authorFormObject, width=40, textvariable=txtphone)
        entphone.grid(row=2, column=1, padx=10, pady=10)

        lbladdress = Label(authorFormObject, text='address: ')
        lbladdress.grid(row=4, column=0, padx=10, pady=10)
        txtaddress = StringVar()
        entaddress = ttk.Entry(authorFormObject, width=40, textvariable=txtaddress)
        entaddress.grid(row=4, column=1, padx=10, pady=10)

        lblcity = Label(authorFormObject, text='city: ')
        lblcity.grid(row=5, column=0, padx=10, pady=10)
        txtcity = StringVar()
        entcity = ttk.Entry(authorFormObject, width=40, textvariable=txtcity)
        entcity.grid(row=5, column=1, padx=10, pady=10)

        lblstate = Label(authorFormObject, text='state: ')
        lblstate.grid(row=6, column=0, padx=10, pady=10)
        txtstate = StringVar()
        entstate = ttk.Entry(authorFormObject, width=40, textvariable=txtstate)
        entstate.grid(row=6, column=1, padx=10, pady=10)

        lblzip = Label(authorFormObject, text='zip: ')
        lblzip.grid(row=7, column=0, padx=10, pady=10)
        txtzip = IntVar()
        entzip = ttk.Entry(authorFormObject, width=36, textvariable=txtzip)
        entzip.grid(row=7, column=1, padx=10, pady=10)

        lblcontract = Label(authorFormObject, text='contract: ')
        lblcontract.grid(row=8, column=0, padx=10, pady=10)
        txtcontract = StringVar()
        entcontract = ttk.Entry(authorFormObject, width=40, textvariable=txtcontract)
        entcontract.grid(row=8, column=1, padx=10, pady=10)

        btnAuthorRegister = ttk.Button(authorFormObject, text='Author Register... ', width=20,
                                       command=authorRegister)
        btnAuthorRegister.grid(row=9, column=1, padx=10, pady=20, sticky='e')

        btnResetForm = ttk.Button(authorFormObject, text='ResetForm', width=16, command=resetForm)
        btnResetForm.grid(row=9, column=1, padx=10, pady=20, sticky='w')

        tree = ttk.Treeview(authorFormObject, columns=(
            'Author ID', 'First Name', 'Last Name'), show='headings')
        tree.heading('Author ID', text='Author ID')
        tree.heading('First Name', text='First Name')
        tree.heading('Last Name', text='Last Name')
        tree.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

        btnRefresh = ttk.Button(authorFormObject, text='Refresh Table', width=16, command=populate_treeview)
        btnRefresh.grid(row=11)
        populate_treeview()



        authorFormObject.mainloop()
