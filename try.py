import tkinter as tk
import tkinter.font as tkFont


def GButton_907_command():
        print("command")


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

        GLabel_320=tk.Label(root)
        GLabel_320["bg"] = "#121111"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_320["font"] = ft
        GLabel_320["fg"] = "#1e90ff"
        GLabel_320["justify"] = "center"
        GLabel_320["text"] = "NAME"
        GLabel_320.place(x=110,y=60,width=130,height=30)

        GLabel_754=tk.Label(root)
        GLabel_754["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_754["font"] = ft
        GLabel_754["fg"] = "#1e90ff"
        GLabel_754["justify"] = "center"
        GLabel_754["text"] = "SPECIALIZATION "
        GLabel_754.place(x=110,y=120,width=170,height=30)

        GLabel_594=tk.Label(root)
        GLabel_594["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_594["font"] = ft
        GLabel_594["fg"] = "#1e90ff"
        GLabel_594["justify"] = "center"
        GLabel_594["text"] = "CITY"
        GLabel_594.place(x=110,y=180,width=130,height=30)

        GLabel_834=tk.Label(root)
        GLabel_834["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_834["font"] = ft
        GLabel_834["fg"] = "#1e90ff"
        GLabel_834["justify"] = "center"
        GLabel_834["text"] = "PHONE"
        GLabel_834.place(x=110,y=240,width=130,height=30)

        GLabel_393=tk.Label(root)
        GLabel_393["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_393["font"] = ft
        GLabel_393["fg"] = "#1e90ff"
        GLabel_393["justify"] = "center"
        GLabel_393["text"] = "EMAIL"
        GLabel_393.place(x=110,y=300,width=130,height=30)

        GLabel_983=tk.Label(root)
        GLabel_983["bg"] = "#121212"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_983["font"] = ft
        GLabel_983["fg"] = "#1e90ff"
        GLabel_983["justify"] = "center"
        GLabel_983["text"] = "EXPERIENCE"
        GLabel_983.place(x=110,y=360,width=130,height=30)

        GLabel_908=tk.Label(root)
        GLabel_908["bg"] = "#0d0c0c"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_908["font"] = ft
        GLabel_908["fg"] = "#1e90ff"
        GLabel_908["justify"] = "center"
        GLabel_908["text"] = "ID"
        GLabel_908.place(x=110,y=10,width=130,height=30)

        GLabel_300=tk.Label(root)
        GLabel_300["bg"] = "#000000"
        ft = tkFont.Font(family='Times',size=14)
        GLabel_300["font"] = ft
        GLabel_300["fg"] = "#1e90ff"
        GLabel_300["justify"] = "center"
        GLabel_300["text"] = "HOSPITAL"
        GLabel_300.place(x=110,y=410,width=130,height=30)

        GLineEdit_343=tk.Entry(root)
        GLineEdit_343["bg"] = "#181717"
        GLineEdit_343["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_343["font"] = ft
        GLineEdit_343["fg"] = "#1e90ff"
        GLineEdit_343["justify"] = "center"
        GLineEdit_343["text"] = ""
        GLineEdit_343.place(x=290,y=10,width=250,height=30)

        GLineEdit_878=tk.Entry(root)
        GLineEdit_878["bg"] = "#0e0d0d"
        GLineEdit_878["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_878["font"] = ft
        GLineEdit_878["fg"] = "#1e90ff"
        GLineEdit_878["justify"] = "center"
        GLineEdit_878["text"] = ""
        GLineEdit_878.place(x=290,y=60,width=250,height=30)

        GLineEdit_442=tk.Entry(root)
        GLineEdit_442["bg"] = "#0d0b0b"
        GLineEdit_442["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_442["font"] = ft
        GLineEdit_442["fg"] = "#1e90ff"
        GLineEdit_442["justify"] = "center"
        GLineEdit_442["text"] = ""
        GLineEdit_442.place(x=290,y=120,width=250,height=30)

        GLineEdit_765=tk.Entry(root)
        GLineEdit_765["bg"] = "#000000"
        GLineEdit_765["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_765["font"] = ft
        GLineEdit_765["fg"] = "#1e90ff"
        GLineEdit_765["justify"] = "center"
        GLineEdit_765["text"] = ""
        GLineEdit_765.place(x=290,y=180,width=250,height=30)

        GLineEdit_481=tk.Entry(root)
        GLineEdit_481["bg"] = "#000000"
        GLineEdit_481["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_481["font"] = ft
        GLineEdit_481["fg"] = "#1e90ff"
        GLineEdit_481["justify"] = "center"
        GLineEdit_481["text"] = ""
        GLineEdit_481.place(x=290,y=240,width=250,height=30)

        GLineEdit_219=tk.Entry(root)
        GLineEdit_219["bg"] = "#000000"
        GLineEdit_219["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_219["font"] = ft
        GLineEdit_219["fg"] = "#1e90ff"
        GLineEdit_219["justify"] = "center"
        GLineEdit_219["text"] = ""
        GLineEdit_219.place(x=290,y=300,width=250,height=30)

        GLineEdit_377=tk.Entry(root)
        GLineEdit_377["bg"] = "#000000"
        GLineEdit_377["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_377["font"] = ft
        GLineEdit_377["fg"] = "#1e90ff"
        GLineEdit_377["justify"] = "center"
        GLineEdit_377["text"] = ""
        GLineEdit_377.place(x=290,y=360,width=250,height=30)

        GLineEdit_999=tk.Entry(root)
        GLineEdit_999["bg"] = "#000000"
        GLineEdit_999["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        GLineEdit_999["font"] = ft
        GLineEdit_999["fg"] = "#1e90ff"
        GLineEdit_999["justify"] = "center"
        GLineEdit_999["text"] = ""
        GLineEdit_999.place(x=290,y=410,width=250,height=30)

        GButton_907=tk.Button(root)
        GButton_907["bg"] = "#0e0d0d"
        ft = tkFont.Font(family='Times',size=14)
        GButton_907["font"] = ft
        GButton_907["fg"] = "#1e90ff"
        GButton_907["justify"] = "center"
        GButton_907["text"] = "ADD DOCTOR"
        GButton_907.place(x=220,y=470,width=150,height=30)
        GButton_907["command"] = GButton_907_command





        root.mainloop()