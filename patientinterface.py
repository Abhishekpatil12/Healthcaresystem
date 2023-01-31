import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import pymongo
import tkinter as tk
import tkinter.font as tkFont
from tkinter import  *
from  tkinter import ttk
import pymongo


def GButton_364_command():
    exec(open("patient.py").read())

def GButton_390_command():
    exec(open("patient.py").read())


def GButton_426_command():
        client = pymongo.MongoClient('mongodb://localhost:27017')

        mydb = client['hospital']

        col = mydb["Doctor"]

        spec  = GLineEdit_994.get()
        city =  GLineEdit_362.get()

        record = {"Specialization":spec,
                  "City":city}

        x = list(col.find(record))

        list2 = []

        print(x)

        for i in range(len(x)):
                list1 = []
                ss = str(x[i])
                a = ss.find("Name")
                a = a + 8;

                b = ss.find("Specialization")
                b = b - 4
                list1.append(ss[a:b])

                a = ss.find("Specialization")
                a = a + 18;

                b = ss.find("City")
                b = b - 4
                list1.append(ss[a:b])

                a = ss.find("City")
                a = a + 8;

                b = ss.find("Phone")
                b = b - 4
                list1.append(ss[a:b])

                a = ss.find("Phone")
                a = a + len("Phone") + 4;

                b = ss.find("Email")
                b = b - 5
                list1.append(ss[a:b])

                a = ss.find("Email")
                a = a + len("Email") + 4;

                b = ss.find("Experience")
                b = b - 4
                list1.append(ss[a:b])

                a = ss.find("Experience")
                a = a + len("Experience") + 4;

                b = ss.find("Hospital")
                b = b - 4
                list1.append(ss[a:b])

                a = ss.find("Hospital")
                a = a + len("Hospital") + 4;

                b = ss.find("}")
                b = b - 1
                list1.append(ss[a:b])

                list2.append(list1)

        # list2 = [['abhi','patil','co'],['roman','reigns','co'],['seth','rollins','lkj']]

        win = Tk()

        frn = Frame(win)
        frn.pack(side=tk.LEFT, padx=20)

        tv = ttk.Treeview(frn, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="5")

        tv.pack()

        tv.heading(1, text="Name")
        tv.heading(2, text="Specialization")
        tv.heading(3, text="City")
        tv.heading(4, text="Phone")
        tv.heading(5, text="Email")
        tv.heading(6, text="Experience")
        tv.heading(7, text="Hospital")

        for i in range(len(x)):
                tv.insert('', 'end', values=list2[i])

        win.title("Doctor Data")
        # win.geometry("650x500")
        # win.resizable(False,False)
        win.mainloop()


flag=1

if flag==1:

        root = tk.Tk()
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_364=tk.Button(root)
        GButton_364["bg"] = "#0e0e0e"
        ft = tkFont.Font(family='Times',size=14)
        GButton_364["font"] = ft
        GButton_364["fg"] = "#01aaed"
        GButton_364["justify"] = "center"
        GButton_364["text"] = "Register"
        GButton_364.place(x=210,y=70,width=151,height=57)
        GButton_364["command"] = GButton_364_command

        GButton_426=tk.Button(root)
        GButton_426["bg"] = "#111111"
        ft = tkFont.Font(family='Times',size=14)
        GButton_426["font"] = ft
        GButton_426["fg"] = "#01aaed"
        GButton_426["justify"] = "center"
        GButton_426["text"] = "Show Doctors"
        GButton_426.place(x=210,y=340,width=152,height=56)
        GButton_426["command"] = GButton_426_command

        GLabel_171=tk.Label(root)
        GLabel_171["bg"] = "#141313"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_171["font"] = ft
        GLabel_171["fg"] = "#01aaed"
        GLabel_171["justify"] = "center"
        GLabel_171["text"] = "Enter Speciality"
        GLabel_171.place(x=100,y=170,width=143,height=38)

        GLineEdit_994=tk.Entry(root)
        GLineEdit_994["bg"] = "#0f0e0e"
        GLineEdit_994["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_994["font"] = ft
        GLineEdit_994["fg"] = "#01aaed"
        GLineEdit_994["justify"] = "center"
        GLineEdit_994["text"] = ""
        GLineEdit_994.place(x=310,y=170,width=221,height=41)

        GButton_390=tk.Button(root)
        GButton_390["bg"] = "#252424"
        ft = tkFont.Font(family='Times',size=14)
        GButton_390["font"] = ft
        GButton_390["fg"] = "#01aaed"
        GButton_390["justify"] = "center"
        GButton_390["text"] = "Enter City"
        GButton_390.place(x=100,y=240,width=142,height=38)
        GButton_390["command"] = GButton_390_command

        GLineEdit_362=tk.Entry(root)
        GLineEdit_362["bg"] = "#0c0c0c"
        GLineEdit_362["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_362["font"] = ft
        GLineEdit_362["fg"] = "#01aaed"
        GLineEdit_362["justify"] = "center"
        GLineEdit_362["text"] = ""
        GLineEdit_362.place(x=310,y=240,width=220,height=40)






        root.mainloop()
