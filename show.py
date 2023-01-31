import pymongo
import tkinter as tk
import tkinter.font as tkFont
from tkinter import  *
from  tkinter import ttk



client = pymongo.MongoClient('mongodb://localhost:27017')

mydb = client['Employee']

col = mydb["employeeinformation"]

list1=[]
x = list(col.find())

list2 = []

for i in range(len(x)):

        list1 = []
        ss = str(x[i])
        a = ss.find("firstname")
        a = a + 13;

        b = ss.find("lastname")
        b = b - 4
        list1.append(ss[a:b])

        a = ss.find("lastname")
        a = a + 12;

        b = ss.find("dep")
        b = b - 4
        list1.append(ss[a:b])

        a = ss.find("dep")
        a = a + 7;

        b = ss.find("}")
        b = b - 1
        list1.append(ss[a:b])

        list2.append(list1)

#list2 = [['abhi','patil','co'],['roman','reigns','co'],['seth','rollins','lkj']]

win = Tk()

frn = Frame(win)
frn.pack(side=tk.LEFT,padx=20)

tv = ttk.Treeview(frn,columns=(1,2,3,4),show="headings",height="5")

tv.pack()

tv.heading(1,text="ID")
tv.heading(2,text="Name")
tv.heading(3,text="Lastname")
tv.heading(4,text="department")

for i in range(len(x)):

    tv.insert('','end',values=list2[i])

win.title("Customer Data")
#win.geometry("650x500")
#win.resizable(False,False)
win.mainloop()






