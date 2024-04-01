from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from BusinessLogicLayer.Sales_BLL import Sales_BLL_Class
from Model.saleModel import SaleModel_Class

class SaleFormClass:
    def __init__(self):
            self.stores_dict = {}
            self.titles_dict = {}
            self.txtstor_id = None
            self.txtord_num = None
            self.txtord_date = None
            self.txtqty = None
            self.txtpayterms = None
            self.txttitle_id = None

    def salesFormload(self):
        salesFormObject = Tk()
        salesFormObject.configure(bg='#cff5ff')
        salesFormObject.geometry('700x735')
        salesFormObject.iconbitmap('images/employeeIcon.ico')
        salesFormObject.resizable(0, 0)
        x = int(salesFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(salesFormObject.winfo_screenheight() / 2 - 400 / 2)
        salesFormObject.geometry('+{}+{}'.format(x, y))

        def saleRegister():
            stor_id = self.txtstor_id.get()
            ord_num = self.txtord_num.get()
            ord_date = self.txtord_date.get()
            qty = self.txtqty.get()
            payterms = self.txtpayterms.get()
            title_id = self.txttitle_id.get()

            SalesModel_Object = SaleModel_Class(stor_id=stor_id, ord_num=ord_num, ord_date=ord_date, qty=qty,
                                                payterms=payterms, title_id=title_id)

            Sales_BLL_Object = Sales_BLL_Class()
            Sales_BLL_Object.registerSales(SalesModel_Object)
            resetForm()

        def resetForm():
            for widget in salesFormObject.winfo_children():
                if isinstance(widget, ttk.Entry) or isinstance(widget, DateEntry):
                    widget.delete(0, END)



        def retrieve_storesNames():
            SalesRetrieve_BLL_Object = Sales_BLL_Class()
            storesNames = SalesRetrieve_BLL_Object.getStoresNames()
            return storesNames

        def retrieve_titlesName():
            SalesRetrieve_BLL_Object = Sales_BLL_Class()
            titlesName = SalesRetrieve_BLL_Object.getTitlesNames()
            return titlesName

        def on_store_selected(event):
            # Retrieve selected store name and set its ID
            selected_store_name = store_combo.get()
            self.txtstor_id.set(self.stores_dict[selected_store_name])

        def on_title_selected(event):
            # Retrieve selected title name and set its ID
            selected_title_name = title_combo.get()
            self.txttitle_id.set(self.titles_dict[selected_title_name])

        lblstor_id = Label(salesFormObject, text='stor_id: ')

        lblstor_id.grid(row=0, column=0, padx=10, pady=10)
        self.txtstor_id = StringVar()
        storesNamesObject = retrieve_storesNames()
        store_names = []
        for row in storesNamesObject:
            store_id, store_name = row
            self.stores_dict[store_name] = store_id
            store_names.append(store_name)
        store_combo = ttk.Combobox(salesFormObject, width=40, textvariable=self.txtstor_id, values=store_names)

        store_combo.grid(row=0, column=1, padx=10, pady=10)
        store_combo.bind("<<ComboboxSelected>>", on_store_selected)
        lblord_num = Label(salesFormObject, text='ord_num: ')

        lblord_num.grid(row=1, column=0, padx=10, pady=10)
        self.txtord_num = IntVar()
        entord_num = ttk.Entry(salesFormObject, width=40, textvariable=self.txtord_num)
        entord_num.grid(row=1, column=1, padx=10, pady=10)
        lblord_date = Label(salesFormObject, text='Order Date: ')  # Corrected label text

        lblord_date.grid(row=2, column=0, padx=10, pady=10)
        self.txtord_date = StringVar()
        entord_date = DateEntry(salesFormObject, width=40, textvariable=self.txtord_date)
        entord_date.grid(row=2, column=1, padx=10, pady=10)
        lblqty = Label(salesFormObject, text='qty: ')

        lblqty.grid(row=3, column=0, padx=10, pady=10)
        self.txtqty = IntVar()
        entqty = ttk.Entry(salesFormObject, width=40, textvariable=self.txtqty)
        entqty.grid(row=3, column=1, padx=10, pady=10)
        lblpayterms = Label(salesFormObject, text='payterms: ')

        lblpayterms.grid(row=4, column=0, padx=10, pady=10)
        self.txtpayterms = IntVar()
        entpayterms = ttk.Entry(salesFormObject, width=40, textvariable=self.txtpayterms)
        entpayterms.grid(row=4, column=1, padx=10, pady= 10)
        lbltitle_id = Label(salesFormObject, text='title_id: ')

        lbltitle_id.grid(row=5, column=0, padx=10, pady=10)
        self.txttitle_id = StringVar()
        titlesNamesObject = retrieve_titlesName()
        title_names = []
        for row in titlesNamesObject:
            title_id, title_name = row
            self.titles_dict[title_name] = title_id
            title_names.append(title_name)
        title_combo = ttk.Combobox(salesFormObject, width=40, textvariable=self.txttitle_id, values=title_names)

        title_combo.grid(row=5, column=1, padx=10, pady=10)
        title_combo.bind("<<ComboboxSelected>>", on_title_selected)
        btnSaleRegister = ttk.Button(salesFormObject, text='Register Sale', width=20, command=saleRegister)

        btnSaleRegister.grid(row=6, column=1, padx=10, pady=20, sticky='e')
        btnResetForm = ttk.Button(salesFormObject, text='Reset Form', width=16, command=resetForm)

        btnResetForm.grid(row=6, column=1, padx=10, pady=20, sticky='w')
        def retrieve_data():
            SalesRetrieve_BLL_Object = Sales_BLL_Class()
            data = SalesRetrieve_BLL_Object.getSalesList()
            return data

        def populate_treeview():
            data = retrieve_data()
            for row in tree.get_children():
                tree.delete(row)
            for row in data:
                values = (row[7], row[3], row[6], row[2])
                tree.insert("", "end", values=values)


        tree = ttk.Treeview(salesFormObject, columns=(
            'Title', 'Qty', 'Store Name', 'Order Date'), show='headings')
        tree.heading('#1', text='Title')
        tree.heading('#2', text='Qty')
        tree.heading('#3', text='Store Name')
        tree.heading('#4', text='Order Date')
        tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        btnRefresh = ttk.Button(salesFormObject, text='Refresh Table', width=16, command=populate_treeview)
        btnRefresh.grid(row=8,column=1, padx=10, pady=20)
        populate_treeview()



        salesFormObject.mainloop()

