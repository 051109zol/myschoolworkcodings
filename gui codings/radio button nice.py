from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title ("We do coding yes")
root.iconbitmap('pewds_qmL_icon.ico')

r = StringVar()
r.set("*****")

myLabel2 = Label (root, text = "You gud mate ?").pack()

def clicked(value):
    myLabel1 = Label(root, text = value)
    myLabel1.pack()

Radiobutton(root, text = "YES =)", variable=r, value = "Nice", command = lambda : clicked (r.get())).pack()
Radiobutton(root, text = "No =(", variable=r, value = "Get some help", command = lambda : clicked (r.get())).pack()

myLabel1 = Label(root, text = r.get())
myLabel1.pack()

root.mainloop()
