from tkinter import *
from PIL import ImageTk, Image

root = Tk ()
root.title ("We do coding yes")
root.iconbitmap('pewds_qmL_icon.ico')

frame = LabelFrame(root, text = "ヘロ エブライオン", fg="blue", bg="yellow", padx = 50, pady = 50)
frame.pack (padx = 25, pady = 25)

b = Button (frame, text = "アニク")
b2 = Button (frame, text = "アケー")
b.grid(row = 0, column = 0)
b2.grid(row = 1, column = 0)

root.mainloop()

