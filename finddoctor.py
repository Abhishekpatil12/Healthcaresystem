import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
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

        GLabel_247=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_247["font"] = ft
        GLabel_247["fg"] = "#333333"
        GLabel_247["justify"] = "left"
        GLabel_247["text"] = "Speciality"
        GLabel_247.place(x=110,y=80,width=136,height=33)

        GLabel_910=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_910["font"] = ft
        GLabel_910["fg"] = "#333333"
        GLabel_910["justify"] = "center"
        GLabel_910["text"] = "City"
        GLabel_910.place(x=90,y=140,width=70,height=25)

        GLineEdit_413=tk.Entry(root)
        GLineEdit_413["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_413["font"] = ft
        GLineEdit_413["fg"] = "#333333"
        GLineEdit_413["justify"] = "center"
        GLineEdit_413["text"] = "Entry"
        GLineEdit_413.place(x=270,y=80,width=70,height=25)

        GLineEdit_29=tk.Entry(root)
        GLineEdit_29["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_29["font"] = ft
        GLineEdit_29["fg"] = "#333333"
        GLineEdit_29["justify"] = "center"
        GLineEdit_29["text"] = "Entry"
        GLineEdit_29.place(x=270,y=140,width=70,height=25)

        GButton_38=tk.Button(root)
        GButton_38["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_38["font"] = ft
        GButton_38["fg"] = "#000000"
        GButton_38["justify"] = "center"
        GButton_38["text"] = "Show"
        GButton_38.place(x=190,y=190,width=95,height=40)
        GButton_38["command"] = self.GButton_38_command

    def GButton_38_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
