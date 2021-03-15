from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title ("WEWEWEW")
root.iconbitmap("pewds_qmL_icon.ico")

def open ():
    global my_img
    top = Toplevel()
    top.title ("miniOn")
    top.iconbitmap("pewds_qmL_icon.ico")
    my_img = ImageTk.PhotoImage(Image.open("gamba/anomaly1.jpg"))
    my_label = Label (top, image=my_img).pack()
    btn2 = Button (top, text = "Bye Minion!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", command = top.destroy).pack()

btn = Button(root, text = "Click me to see minion!!!!!!", command = open).pack()

root.mainloop()
