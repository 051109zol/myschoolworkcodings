from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title ("We do coding yes")
root.iconbitmap('pewds_qmL_icon.ico')

#pizza= StringVar()
#pizza.set("Peperoni")

MODES = [
    ("Peperoni", "Peperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Peperoni")

for text, mode in MODES :
    Radiobutton (root, text = text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel1 = Label(root, text = value)
    myLabel1.pack()

#Radiobutton(root, text = "Option 1", variable=r, value = "1", command = lambda : clicked (r.get())).pack()
#Radiobutton(root, text = "Option2", variable=r, value = "2", command = lambda : clicked (r.get())).pack()

#myLabel1 = Label(root, text = pizza.get()).pack()

myButton = Button(root, text = "Click Me!", command = lambda : clicked (pizza.get())).pack()

root.mainloop()
