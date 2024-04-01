from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from BusinessLogicLayer.Title_BLL import Title_BLL_Class
from Model.Title_Model import TitleModel_Class


class TitleFormClass:
    def __init__(self):
        pass

    def TitleFormload(self):
        TitleFormObject = Tk()
        TitleFormObject.title('Title Form')
        TitleFormObject.geometry('700x735')
        TitleFormObject.configure(bg='#cff5ff')
        TitleFormObject.iconbitmap('images/employeeIcon.ico')
        TitleFormObject.resizable(0, 0)
        x = int(TitleFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(TitleFormObject.winfo_screenheight() / 2 - 400 / 2)
        TitleFormObject.geometry('+{}+{}'.format(x, y))

        def titleRegister():
            title_id = txttitle_id.get()
            title = txttitle.get()
            type = txttype.get()
            pub_id = txtpub_id.get()
            price = txtprice.get()
            advance = txtadvance.get()
            royalty = txtroyalty.get()
            ytd_sales = txtytd_sales.get()
            notes = txtnotes.get()
            pubdate = txtpubdate.get()

            TitleModel_Object = TitleModel_Class(title_id=title_id, title=title, type=type, pub_id=pub_id, price=price, advance=advance,
                                                 royalty=royalty, ytd_sales=ytd_sales, notes=notes, pubdate=pubdate)

            Title_BLL_Object = Title_BLL_Class()
            Title_BLL_Object.registerTitle(TitleModel_Object)
            resetForm()

        def resetForm():
            for widget in TitleFormObject.winfo_children():
                if isinstance(widget, ttk.Entry) or isinstance(widget, DateEntry):
                    widget.delete(0, END)

        def retrieve_data():

            TitleRetrieve_BLL_Object = Title_BLL_Class()
            data = TitleRetrieve_BLL_Object.getTitlesList()
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

        lbltitle_id = Label(TitleFormObject, text='title_id: ')
        lbltitle_id.grid(row=0, column=0, padx=10, pady=10)
        txttitle_id = StringVar()
        enttitle_id = ttk.Entry(TitleFormObject, width=40, textvariable=txttitle_id)
        enttitle_id.grid(row=0, column=1, padx=10, pady=10)

        lbltitle = Label(TitleFormObject, text='title: ')
        lbltitle.grid(row=1, column=0, padx=10, pady=10)
        txttitle = StringVar()
        enttitle = ttk.Entry(TitleFormObject, width=40, textvariable=txttitle)
        enttitle.grid(row=1, column=1, padx=10, pady=10)

        lbltype = Label(TitleFormObject, text='type: ')
        lbltype.grid(row=2, column=0, padx=10, pady=10)
        txttype = StringVar()
        enttype = ttk.Entry(TitleFormObject, width=40, textvariable=txttype)
        enttype.grid(row=2, column=1, padx=10, pady=10)

        lblpub_id = Label(TitleFormObject, text='pub_id: ')
        lblpub_id.grid(row=3, column=0, padx=10, pady=10)
        txtpub_id = StringVar()
        entpub_id = ttk.Entry(TitleFormObject, width=40, textvariable=txtpub_id)
        entpub_id.grid(row=3, column=1, padx=10, pady=10)

        lblprice = Label(TitleFormObject, text='price: ')
        lblprice.grid(row=4, column=0, padx=10, pady=10)
        txtprice = DoubleVar()
        entprice = ttk.Entry(TitleFormObject, width=40, textvariable=txtprice)
        entprice.grid(row=4, column=1, padx=10, pady=10)

        lbladvance = Label(TitleFormObject, text='advance: ')
        lbladvance.grid(row=5, column=0, padx=10, pady=10)
        txtadvance = DoubleVar()
        entadvance = ttk.Entry(TitleFormObject, width=40, textvariable=txtadvance)
        entadvance.grid(row=5, column=1, padx=10, pady=10)

        lblroyalty = Label(TitleFormObject, text='royalty: ')
        lblroyalty.grid(row=6, column=0, padx=10, pady=10)
        txtroyalty = IntVar()
        entroyalty = ttk.Entry(TitleFormObject, width=40, textvariable=txtroyalty)
        entroyalty.grid(row=6, column=1, padx=10, pady=10)

        lblytd_sales = Label(TitleFormObject, text='ytd_sales: ')
        lblytd_sales.grid(row=7, column=0, padx=10, pady=10)
        txtytd_sales = IntVar()
        entytd_sales = ttk.Entry(TitleFormObject, width=36, textvariable=txtytd_sales)
        entytd_sales.grid(row=7, column=1, padx=10, pady=10)

        lblnotes = Label(TitleFormObject, text='notes: ')
        lblnotes.grid(row=8, column=0, padx=10, pady=10)
        txtnotes = StringVar()
        entnotes = ttk.Entry(TitleFormObject, width=36, textvariable=txtnotes)
        entnotes.grid(row=8, column=1, padx=10, pady=10)

        lblpubdate = Label(TitleFormObject, text='pubdate: ')
        lblpubdate.grid(row=9, column=0, padx=10, pady=10)
        txtpubdate = StringVar()
        entpubdate = DateEntry(TitleFormObject, width=36, textvariable=txtpubdate)
        entpubdate.grid(row=9, column=1, padx=10, pady=10)




        btnTitleRegister = ttk.Button(TitleFormObject, text='Title Register... ', width=20,
                                         command=titleRegister)
        btnTitleRegister.grid(row=10, column=1, padx=10, pady=20, sticky='e')

        btnResetForm = ttk.Button(TitleFormObject, text='ResetForm', width=16, command=resetForm)
        btnResetForm.grid(row=10, column=1, padx=10, pady=20, sticky='w')

        tree = ttk.Treeview(TitleFormObject, columns=(
            'Employee ID', 'First Name', 'Last Name'), show='headings')
        tree.heading('Employee ID', text='Employee ID')
        tree.heading('First Name', text='First Name')
        tree.heading('Last Name', text='Last Name')
        tree.grid(row=11, column=0, columnspan=3, padx=10, pady=10)

        btnRefresh = ttk.Button(TitleFormObject, text='Refresh Table', width=16, command=populate_treeview)
        btnRefresh.grid(row=12, column=1, padx=10, pady=20)

        populate_treeview()

        TitleFormObject.mainloop()
