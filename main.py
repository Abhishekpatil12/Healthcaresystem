import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import pymongo


def GButton_316_command():
    client = pymongo.MongoClient('mongodb://localhost:27017')

    mydb = client['hospital']

    col = mydb["login"]

    x1 = list(col.find())
    print(x1)
    x = str(x1)
    a = x.find("Username")
    a = a + 12;

    b = x.find("Password")
    b = b - 4
    user = x[a:b]
    print(user)

    a = x.find("Password")
    a = a + 12;
    print("a",a)

    b = x.find("}")
    b = b - 1
    print(b)
    passw = x[a:b]
    print(passw)

    us = e.get()
    print(us)

    pa = GLineEdit_916.get()
    print(pa)

    if (us == user and pa == passw):
        messagebox.showinfo("showinfo", "Login successful")
        exec(open("afterlogin.py").read())
    else:
        messagebox.showinfo("showinfo", "Login unsuccessful")
        print("HEllo")



flag=1
if flag==1:
        root = tk.Tk()
        #setting title
        root.title("Welcome Admin")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_868=tk.Label(root)
        GLabel_868["bg"] = "#19191a"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_868["font"] = ft
        GLabel_868["fg"] = "#01aaed"
        GLabel_868["justify"] = "center"
        GLabel_868["text"] = "Hospital Managment System"
        GLabel_868.place(x=100,y=40,width=413,height=53)

        GLabel_387=tk.Label(root)
        GLabel_387["bg"] = "#0b0b0b"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_387["font"] = ft
        GLabel_387["fg"] = "#01aaed"
        GLabel_387["justify"] = "center"
        GLabel_387["text"] = "Username"
        GLabel_387.place(x=100,y=190,width=144,height=39)

        GLabel_875=tk.Label(root)
        GLabel_875["bg"] = "#080808"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_875["font"] = ft
        GLabel_875["fg"] = "#01aaed"
        GLabel_875["justify"] = "center"
        GLabel_875["text"] = "Password"
        GLabel_875.place(x=100,y=270,width=146,height=48)

        e = tk.Entry(root)
        e["bg"] = "#0c0c0c"
        e["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        e["font"] = ft
        e["fg"] = "#01aaed"
        e["justify"] = "center"
        e["text"] = ""
        e.place(x=330,y=190,width=185,height=41)

        GLineEdit_916=tk.Entry(root)
        GLineEdit_916["bg"] = "#0b0b0b"
        GLineEdit_916["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_916["font"] = ft
        GLineEdit_916["fg"] = "#01aaed"
        GLineEdit_916["justify"] = "center"
        GLineEdit_916["text"] = ""
        GLineEdit_916.place(x=330,y=270,width=185,height=43)

        GMessage_18 = tk.Message(root)
        GMessage_18["bg"] = "#000000"
        ft = tkFont.Font(family='Times', size=14)
        GMessage_18["font"] = ft
        GMessage_18["fg"] = "#01aaed"
        GMessage_18["justify"] = "center"
        GMessage_18["text"] = ""
        GMessage_18.place(x=190, y=110, width=240, height=43)

        GButton_316=tk.Button(root, command=GButton_316_command)
        GButton_316["bg"] = "#100f0f"
        ft = tkFont.Font(family='Times',size=16)
        GButton_316["font"] = ft
        GButton_316["fg"] = "#01aaed"
        GButton_316["justify"] = "center"
        GButton_316["text"] = "Login"
        GButton_316.place(x=220,y=370,width=155,height=60)
        root.mainloop()
