from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title ("Using Icons Images, and Exit Buttons")
root.iconbitmap("pewds_qmL_icon.ico")

my_img = ImageTk.PhotoImage(Image.open("gamba/anomaly1.jpg"))
my_label = Label(image = my_img)
my_label.pack()

button_quit = Button (root, text = "End Program", fg="blue", bg="yellow", padx=50, pady=75, command = root.quit)
button_quit.pack()

root.mainloop()
