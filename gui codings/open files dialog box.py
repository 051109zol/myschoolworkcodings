from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk ()
root.title ("We do coding yes")
root.iconbitmap("pewds_qmL_icon.ico")

#root.filename = filedialog.askopenfilename(initialdir = "/gui codings/gamba", title = "Select a file", filetypes = (("JPG FILES", "*.jpg"), ("ALL FILES", "*.*")))
#my_label = Label (root, text = root.filename).pack()
#my_image = ImageTk.PhotoImage (Image.open(root.filename))
#my_image_label = Label (image = my_image).pack()

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir = "/gui codings/gamba", title = "Select a file", filetypes = (("JPG FILES", "*.jpg"), ("ALL FILES", "*.*")))
    my_label = Label (root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage (Image.open(root.filename))
    my_image_label = Label (image = my_image).pack()
    
my_btn = Button (root, text = "Open File", command = open).pack()

root.mainloop()
