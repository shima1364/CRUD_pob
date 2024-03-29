from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import pyodbc
from UserInterfaceLayer.MainFormModule import MainFormClass
from tkcalendar.dateentry import DateEntry
from babel import dates
from babel import numbers

loginFormObject = Tk()
loginFormObject.title('Login Form')
loginFormObject.geometry('400x160')
loginFormObject.iconbitmap('images/loginIcon.ico')
loginFormObject.resizable(0, 0)
x = int(loginFormObject.winfo_screenwidth() / 2 - 400 / 2)
y = int(loginFormObject.winfo_screenheight() / 2 - 160 / 2)
loginFormObject.geometry('+{}+{}'.format(x, y))


def checkLoginFunction():
    userName = txtUserName.get()
    password = txtPassword.get()

    connectionString = 'Driver={SQL Server};Server=localhost;Database=Sematec;Trusted_Connection=yes;'
    commandText = 'exec [dbo].[CheckLogin] ?,?'
    params = (userName, password)
    with pyodbc.connect(connectionString) as connection:
        cursor = connection.cursor()
        cursor.execute(commandText, params)
        row = cursor.fetchone()

    if row is not None:
        # msg.showinfo('Welcome', f'Welcome {row[2]} {row[3]}')
        loginFormObject.destroy()
        mainFormObject = MainFormClass()
        mainFormObject.mainFormLoad(fname=row[2], lname=row[3])


    else:
        msg.showerror('Error', 'UserName or Password is incorrect!!!')


# if userName.lower() =='admin' and password == 'admin':
#     msg.showinfo('Welcome','Welcome admin User')
# else:
#     msg.showerror('Error','Username or Password is incorrect !!!')


lblUserName = Label(loginFormObject, text='UserName: ')
lblUserName.grid(row=0, column=0, padx=10, pady=20)

txtUserName = StringVar()
entUserName = ttk.Entry(loginFormObject, width=40, textvariable=txtUserName)
entUserName.grid(row=0, column=1, padx=10, pady=20)

lblPassword = Label(loginFormObject, text='Password: ')
lblPassword.grid(row=1, column=0, padx=10, pady=0)

txtPassword = StringVar()
entPassword = ttk.Entry(loginFormObject, width=40, show='*', textvariable=txtPassword)
entPassword.grid(row=1, column=1, padx=10, pady=0)

btnLoginCheck = ttk.Button(loginFormObject, text='Login... ', width=20, command=checkLoginFunction)
btnLoginCheck.grid(row=2, column=1, padx=10, pady=20, sticky='e')

loginFormObject.mainloop()
