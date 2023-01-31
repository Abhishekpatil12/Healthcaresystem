import tkinter as tk
import tkinter.font as tkFont



def GButton_609_command():
    exec(open("deleterecoed.py").read())


def GButton_786_command():
    exec(open("adddoctor.py").read())


def GButton_451_command():
    exec(open("showpatientdetails.py").read())


def GButton_1_command():
    exec(open("showdoctordetail.py").read())


flag=1

if flag==1:

        root = tk.Tk()
        #setting title
        root.title("Choose Option")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)



        GButton_609=tk.Button(root)
        GButton_609["activebackground"] = "#1d5fa2"
        GButton_609["activeforeground"] = "#1b1919"
        GButton_609["bg"] = "#1b1919"
        ft = tkFont.Font(family='Times',size=14)
        GButton_609["font"] = ft
        GButton_609["fg"] = "#146bbf"
        GButton_609["justify"] = "center"
        GButton_609["text"] = "Delete"
        GButton_609.place(x=210,y=120,width=185,height=43)
        GButton_609["command"] = GButton_609_command

        GButton_786=tk.Button(root)
        GButton_786["activebackground"] = "#1e90ff"
        GButton_786["activeforeground"] = "#111010"
        GButton_786["bg"] = "#1c1a1a"
        ft = tkFont.Font(family='Times',size=14)
        GButton_786["font"] = ft
        GButton_786["fg"] = "#1e90ff"
        GButton_786["justify"] = "center"
        GButton_786["text"] = "Add Doctor"
        GButton_786.place(x=210,y=170,width=185,height=43)
        GButton_786["command"] = GButton_786_command

        GButton_451=tk.Button(root)
        GButton_451["bg"] = "#121212"
        ft = tkFont.Font(family='Times',size=14)
        GButton_451["font"] = ft
        GButton_451["fg"] = "#1e90ff"
        GButton_451["justify"] = "center"
        GButton_451["text"] = "Show Patient Details"
        GButton_451["relief"] = "raised"
        GButton_451.place(x=210,y=220,width=185,height=43)
        GButton_451["command"] = GButton_451_command

        GButton_1=tk.Button(root,command=GButton_1_command)
        GButton_1["activebackground"] = "#1e90ff"
        GButton_1["bg"] = "#181515"
        ft = tkFont.Font(family='Times',size=14)
        GButton_1["font"] = ft
        GButton_1["fg"] = "#1e90ff"
        GButton_1["justify"] = "center"
        GButton_1["text"] = "Show Doctor Details"
        GButton_1["relief"] = "raised"
        GButton_1.place(x=210,y=270,width=185,height=43)

        root.mainloop()





