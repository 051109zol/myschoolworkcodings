from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk ()
root.title ("We do coding yes")
root.iconbitmap('C:/Users/user/Desktop/Zaid/hw/ask/3011/gui codings/pewds_qmL_icon.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.showinfo("This is my Popup!", "Hellow world")
    Label (root, text=response).pack()
    #if response == "yes":
    #    Label (root, text = "Yes you click").pack()
    #else :
    #    Label (root, text = "No you click").pack()

Button(root, text = "POPUP", command = popup).pack()

root.mainloop()
