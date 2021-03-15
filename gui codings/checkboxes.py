from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title ("We do coding yes")
root.iconbitmap("pewds_qmL_icon.ico")
root.geometry("400x400")

# Drop down boxes

def show():
    myLabel = Label ( root, text = clicked.get()).pack()
    
option = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set (option[0])

drop = OptionMenu (root, clicked, *option)
drop.pack()

myButton = Button ( root, text = "Show Selection", command = show).pack()

root.mainloop()
