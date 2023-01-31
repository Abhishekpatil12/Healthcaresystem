import tkinter as tk
import tkinter.font as tkFont
from tkinter import  *
from  tkinter import ttk
from tkinter import messagebox
import pymongo


def GButton_924_command():
    ide = GLineEdit_460.get()

    client = pymongo.MongoClient('mongodb://localhost:27017')

    mydb = client['hospital']

    col = mydb["Doctor"]

    myquery = {"_id" : int(ide)}

    col.delete_one(myquery)

    messagebox.showinfo("showinfo", "Element Deleted")



flag = 1

if flag == 1:
    root = tk.Tk()
    root.title("undefined")
    # setting window size
    width = 600
    height = 500
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    GLabel_821 = tk.Label(root)
    GLabel_821["bg"] = "#000000"
    ft = tkFont.Font(family='Times', size=14)
    GLabel_821["font"] = ft
    GLabel_821["fg"] = "#01aaed"
    GLabel_821["justify"] = "center"
    GLabel_821["text"] = "Enter ID"
    GLabel_821.place(x=120, y=130, width=140, height=44)

    GLineEdit_460 = tk.Entry(root)
    GLineEdit_460["bg"] = "#000000"
    GLineEdit_460["borderwidth"] = "1px"
    ft = tkFont.Font(family='Times', size=14)
    GLineEdit_460["font"] = ft
    GLineEdit_460["fg"] = "#01aaed"
    GLineEdit_460["justify"] = "center"
    GLineEdit_460["text"] = ""
    GLineEdit_460.place(x=320, y=130, width=142, height=43)

    GButton_924 = tk.Button(root)
    GButton_924["bg"] = "#0e0e0e"
    ft = tkFont.Font(family='Times', size=14)
    GButton_924["font"] = ft
    GButton_924["fg"] = "#01aaed"
    GButton_924["justify"] = "center"
    GButton_924["text"] = "Delete"
    GButton_924.place(x=240, y=230, width=125, height=43)
    GButton_924["command"] = GButton_924_command

    root.mainloop()
