from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from BusinessLogicLayer.Sales_BLL import Sales_BLL_Class
from Model.saleModel import SaleModel_Class



class SaleFormClass:
    def __init__(self):
        pass


    def salesFormload(self):
        salesFormObject = Tk()
        salesFormObject.configure(bg='#cff5ff')
        salesFormObject.geometry('1000x735')
        salesFormObject.iconbitmap('images/employeeIcon.ico')
        salesFormObject.resizable(0, 0)
        x = int(salesFormObject.winfo_screenwidth() / 2 - 400 / 2)
        y = int(salesFormObject.winfo_screenheight() / 2 - 400 / 2)
        salesFormObject.geometry('+{}+{}'.format(x, y))

        def saleRegister():
            stor_id = txtstor_id.get()
            ord_num = txtord_num.get()
            ord_date = txtord_date.get()
            qty = txtqty.get()
            payterms = txtpayterms.get()
            title_id = txttitle_id.get()

            SalesModel_Object = SaleModel_Class(stor_id=stor_id, ord_num=ord_num, ord_date=ord_date, qty=qty,
                                                payterms=payterms, title_id=title_id)

            Sales_BLL_Object = Sales_BLL_Class()
            Sales_BLL_Object.registerSales(SalesModel_Object)
            resetForm()

        def resetForm():
            for widget in salesFormObject.winfo_children():
                if isinstance(widget, ttk.Entry) or isinstance(widget, DateEntry):
                    widget.delete(0, END)

        def retrieve_data():
            SalesRetrieve_BLL_Object = Sales_BLL_Class()
            data = SalesRetrieve_BLL_Object.getSalesList()
            return data

        def retrieve_storesNames():
            SalesRetrieve_BLL_Object = Sales_BLL_Class()
            storesNames = SalesRetrieve_BLL_Object.getStoresNames()
            return storesNames

        def retrieve_titlesName():
            SalesRetrieve_BLL_Object = Sales_BLL_Class()
            titlesName = SalesRetrieve_BLL_Object.getTitlesNames()
            return titlesName

        def populate_treeview():
            data = retrieve_data()
            for row in tree.get_children():
                tree.delete(row)
            for row in data:
                tree.insert("", "end", values=row)

        lblstor_id = Label(salesFormObject, text='stor_id: ')
        lblstor_id.grid(row=0, column=0, padx=10, pady=10)
        txtstor_id = StringVar()
        storesNamesObject = retrieve_storesNames()
        storesNames = []
        for row in storesNamesObject:
            storesNames.append(row[0])
            txtstor_id.set(row[0])

        entstor_id = ttk.Combobox(salesFormObject, width=40, textvariable=txtstor_id, values=storesNames)
        entstor_id.grid(row=0, column=1, padx=10, pady=10)

        lblord_num = Label(salesFormObject, text='ord_num: ')
        lblord_num.grid(row=1, column=0, padx=10, pady=10)
        txtord_num = IntVar()
        entord_num = ttk.Entry(salesFormObject, width=40, textvariable=txtord_num)
        entord_num.grid(row=1, column=1, padx=10, pady=10)

        lblord_date = Label(salesFormObject, text='Order Date: ')  # Corrected label text
        lblord_date.grid(row=2, column=0, padx=10, pady=10)
        txtord_date = StringVar()
        entord_date = DateEntry(salesFormObject, width=40, textvariable=txtord_date)
        entord_date.grid(row=2, column=1, padx=10, pady=10)

        lblqty = Label(salesFormObject, text='qty: ')
        lblqty.grid(row=3, column=0, padx=10, pady=10)
        txtqty = IntVar()
        entqty = ttk.Entry(salesFormObject, width=40, textvariable=txtqty)
        entqty.grid(row=3, column=1, padx=10, pady=10)

        lblpayterms = Label(salesFormObject, text='payterms: ')
        lblpayterms.grid(row=4, column=0, padx=10, pady=10)
        txtpayterms = IntVar()
        entpayterms = ttk.Entry(salesFormObject, width=40, textvariable=txtpayterms)
        entpayterms.grid(row=4, column=1, padx=10, pady= 10)

        lbltitle_id = Label(salesFormObject, text='title_id: ')
        lbltitle_id.grid(row=5, column=0, padx=10, pady=10)
        txttitle_id = StringVar()
        titlesNamesObject = retrieve_titlesName()
        titlesNames = []
        for row in titlesNamesObject:
            titlesNames.append(row[0])
            txttitle_id.set(row[0])
        enttitle_id = ttk.Combobox(salesFormObject, width=40, textvariable=txttitle_id, values=titlesNames)
        enttitle_id.grid(row=5, column=1, padx=10, pady=10)

        btnSaleRegister = ttk.Button(salesFormObject, text='Register Sale', width=20, command=saleRegister)
        btnSaleRegister.grid(row=6, column=1, padx=10, pady=20, sticky='e')

        btnResetForm = ttk.Button(salesFormObject, text='Reset Form', width=16, command=resetForm)
        btnResetForm.grid(row=6, column=1, padx=10, pady=20, sticky='w')

        tree = ttk.Treeview(salesFormObject, columns=('Title', 'Qty', 'Store Name', 'Order Date'), show='headings')
        tree.heading('#1', text='Title')
        tree.heading('#2', text='Qty')
        tree.heading('#3', text='Store Name')
        tree.heading('#4', text='Order Date')
        tree.pack(expand=True, fill='both')
        tree.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

        btnRefresh = ttk.Button(salesFormObject, text='Refresh Table', width=16, command=populate_treeview)
        btnRefresh.grid(row=8, column=1, pady=10)

        populate_treeview()

        salesFormObject.mainloop()
