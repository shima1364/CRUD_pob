from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from UserInterfaceLayer.MainFormModule import MainFormClass

def main():
    mainFormObject = Tk()
    mainFormObject.title('Main Form')
    mainFormObject.geometry('400x400')
    mainFormObject.iconbitmap('images/mainIcon.ico')
    mainFormObject.resizable(0, 0)
    x = int(mainFormObject.winfo_screenwidth() / 2 - 400 / 2)
    y = int(mainFormObject.winfo_screenheight() / 2 - 400 / 2)
    mainFormObject.geometry('+{}+{}'.format(x, y))

    mainForm = MainFormClass()
    mainForm.mainFormLoad(mainFormObject, "John", "Doe")

    mainFormObject.mainloop()

if __name__ == "__main__":
    main()