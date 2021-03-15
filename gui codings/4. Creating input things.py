from tkinter import *

root = Tk()

#Making the input box
e = Entry(root, width=50, borderwidth=10, fg = "blue", bg = "yellow")
e.pack()

#Make things we write in input displayed in the output (e.get())
def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.pack()

myButton = Button(root, text= "Enter your Name", padx=50, pady=75, command=myClick, fg="blue", bg="yellow")
myButton.pack ()

root.mainloop()
