
import tkinter as tk
import tkinter.font as tkFont
from tkinter import  *
from  tkinter import ttk
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017')

mydb = client['hospital']

col = mydb["Doctor"]

list1=[]
x = list(col.find())

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

#list2 = [['abhi','patil','co'],['roman','reigns','co'],['seth','rollins','lkj']]

win = Tk()

frn = Frame(win)
frn.pack(side=tk.LEFT,padx=20)

tv = ttk.Treeview(frn,columns=(1,2,3,4,5,6,7,8),show="headings",height="5")

tv.pack()


tv.heading(1,text="Name")
tv.heading(2,text="Specialization")
tv.heading(3,text="City")
tv.heading(4,text="Phone")
tv.heading(5,text="Email")
tv.heading(6,text="Experience")
tv.heading(7,text="Hospital")

for i in range(len(x)):

    tv.insert('','end',values=list2[i])

win.title("Doctor Data")
#win.geometry("650x500")
#win.resizable(False,False)
win.mainloop()






