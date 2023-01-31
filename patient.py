import tkinter as tk
import tkinter.font as tkFont
import pymongo
from tkinter import messagebox


def GButton_536_command():
    client = pymongo.MongoClient('mongodb://localhost:27017')

    mydb = client['hospital']

    col = mydb["Doctor"]

    information = mydb.patient

    ide = GLineEdit_905.get()
    name = GLineEdit_983.get()
    email = GLineEdit_79.get()
    phone = GLineEdit_459.get()
    age = GLineEdit_976.get()
    city = GLineEdit_734.get()

    record = {"_id": int(ide),
              "Name": name,
              "Phone":phone,
              "City": city,
              "Email": email,
              "Age": age,
              "Password": "abc"}

    information.insert_one(record)

    messagebox.showinfo("showinfo", "Element added")

flag=1

if flag==1:

        root = tk.Tk()
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_225=tk.Label(root)
        GLabel_225["bg"] = "#070707"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_225["font"] = ft
        GLabel_225["fg"] = "#1e90ff"
        GLabel_225["justify"] = "center"
        GLabel_225["text"] = "ID"
        GLabel_225.place(x=100,y=60,width=90,height=30)

        GLineEdit_905=tk.Entry(root)
        GLineEdit_905["bg"] = "#0b0b0b"
        GLineEdit_905["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_905["font"] = ft
        GLineEdit_905["fg"] = "#1e90ff"
        GLineEdit_905["justify"] = "center"
        GLineEdit_905["text"] = ""
        GLineEdit_905.place(x=300,y=60,width=250,height=30)

        GLabel_317=tk.Label(root)
        GLabel_317["bg"] = "#121212"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_317["font"] = ft
        GLabel_317["fg"] = "#1e90ff"
        GLabel_317["justify"] = "center"
        GLabel_317["text"] = "NAME"
        GLabel_317.place(x=100,y=120,width=90,height=30)

        GLineEdit_983=tk.Entry(root)
        GLineEdit_983["bg"] = "#0b0b0b"
        GLineEdit_983["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_983["font"] = ft
        GLineEdit_983["fg"] = "#1e90ff"
        GLineEdit_983["justify"] = "center"
        GLineEdit_983["text"] = ""
        GLineEdit_983.place(x=300,y=120,width=250,height=30)

        GLabel_329=tk.Label(root)
        GLabel_329["bg"] = "#070707"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_329["font"] = ft
        GLabel_329["fg"] = "#1e90ff"
        GLabel_329["justify"] = "center"
        GLabel_329["text"] = "PHONE"
        GLabel_329.place(x=100,y=180,width=90,height=30)

        GLineEdit_459=tk.Entry(root)
        GLineEdit_459["bg"] = "#0a0a0a"
        GLineEdit_459["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_459["font"] = ft
        GLineEdit_459["fg"] = "#1e90ff"
        GLineEdit_459["justify"] = "center"
        GLineEdit_459["text"] = ""
        GLineEdit_459.place(x=300,y=180,width=250,height=30)

        GLabel_344=tk.Label(root)
        GLabel_344["bg"] = "#121212"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_344["font"] = ft
        GLabel_344["fg"] = "#1e90ff"
        GLabel_344["justify"] = "center"
        GLabel_344["text"] = "CITY"
        GLabel_344.place(x=100,y=240,width=90,height=30)

        GLineEdit_734=tk.Entry(root)
        GLineEdit_734["bg"] = "#1a1818"
        GLineEdit_734["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_734["font"] = ft
        GLineEdit_734["fg"] = "#1e90ff"
        GLineEdit_734["justify"] = "center"
        GLineEdit_734["text"] = ""
        GLineEdit_734.place(x=300,y=240,width=250,height=30)

        GLabel_200=tk.Label(root)
        GLabel_200["bg"] = "#0f0f10"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_200["font"] = ft
        GLabel_200["fg"] = "#1e90ff"
        GLabel_200["justify"] = "center"
        GLabel_200["text"] = "EMAIL"
        GLabel_200.place(x=100,y=300,width=90,height=30)

        GLineEdit_79=tk.Entry(root)
        GLineEdit_79["bg"] = "#161617"
        GLineEdit_79["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_79["font"] = ft
        GLineEdit_79["fg"] = "#1e90ff"
        GLineEdit_79["justify"] = "center"
        GLineEdit_79["text"] = ""
        GLineEdit_79.place(x=300,y=300,width=250,height=30)

        GLabel_74=tk.Label(root)
        GLabel_74["bg"] = "#070707"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_74["font"] = ft
        GLabel_74["fg"] = "#1e90ff"
        GLabel_74["justify"] = "center"
        GLabel_74["text"] = "AGE"
        GLabel_74.place(x=100,y=360,width=90,height=30)

        GLineEdit_976=tk.Entry(root)
        GLineEdit_976["bg"] = "#100e0e"
        GLineEdit_976["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_976["font"] = ft
        GLineEdit_976["fg"] = "#1e90ff"
        GLineEdit_976["justify"] = "center"
        GLineEdit_976["text"] = ""
        GLineEdit_976.place(x=300,y=360,width=250,height=30)

        GButton_536=tk.Button(root)
        GButton_536["bg"] = "#070707"
        ft = tkFont.Font(family='Times',size=14)
        GButton_536["font"] = ft
        GButton_536["fg"] = "#1e90ff"
        GButton_536["justify"] = "center"
        GButton_536["text"] = "ADD PATIENT"
        GButton_536.place(x=170,y=430,width=180,height=30)
        GButton_536["command"] = GButton_536_command


        root.mainloop()