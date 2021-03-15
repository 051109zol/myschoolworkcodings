from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.configure (background='green')
root.geometry("390x545")

e = Entry(root, width=40, borderwidth=20, fg = "blue", bg = "yellow")
e.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky = W+E)

#e.insert(0, "Enter the number = ")

def button_click(number):
    #e.delete (0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete (0, END)

def button_equal():
    second_number = e.get()
    e.delete (0, END)

    if math == "addition":
        e.insert (0, f_num + int(second_number))

    if math == "substraction":
        e.insert (0, f_num - int(second_number))

    if math == "multiplication":
        e.insert (0, f_num * int(second_number))

    if math == "division":
        e.insert (0, f_num / int(second_number))
    
def button_minus():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete (0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete (0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete (0, END)
    
# Define Buttons

button_1 = Button(root, text= "1", padx = 40, pady = 20, command=lambda: button_click(1), fg = "green", bg = "pink")
button_2 = Button(root, text= "2", padx = 40, pady = 20, command=lambda: button_click(2), fg = "green", bg = "pink")
button_3 = Button(root, text= "3", padx = 40, pady = 20, command=lambda: button_click(3), fg = "green", bg = "pink")
button_4 = Button(root, text= "4", padx = 40, pady = 20, command=lambda: button_click(4), fg = "green", bg = "pink")
button_5 = Button(root, text= "5", padx = 40, pady = 20, command=lambda: button_click(5), fg = "green", bg = "pink")
button_6 = Button(root, text= "6", padx = 40, pady = 20, command=lambda: button_click(6), fg = "green", bg = "pink")
button_7 = Button(root, text= "7", padx = 40, pady = 20, command=lambda: button_click(7), fg = "green", bg = "pink")
button_8 = Button(root, text= "8", padx = 40, pady = 20, command=lambda: button_click(8), fg = "green", bg = "pink")
button_9 = Button(root, text= "9", padx = 40, pady = 20, command=lambda: button_click(9), fg = "green", bg = "pink")
button_0 = Button(root, text= "0", padx = 40, pady = 20, command=lambda: button_click(0), fg = "green", bg = "pink")
button_add = Button(root, text= "+", padx = 40, pady = 20, command = button_add, fg = "yellow", bg = "blue")
button_equal = Button(root, text= "=", pady = 20, command = button_equal, fg = "white", bg = "purple")
button_clear = Button(root, text= "Clear", pady = 20, command = button_clear, fg = "white", bg = "purple")

button_minus = Button(root, text= "-", padx = 41, pady = 20, command = button_minus, fg = "yellow", bg = "blue")
button_multiply = Button(root, text= "x", padx = 42, pady = 20, command = button_multiply, fg = "yellow", bg = "blue")
button_divide = Button(root, text= "÷", padx = 42, pady = 20, command = button_divide, fg = "yellow", bg = "blue")

# Put the button on the screen

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1,columnspan=2, sticky = W+E)
button_3.grid(row = 3, column = 3)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1,columnspan=2, sticky = W+E)
button_6.grid(row = 2, column = 3)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1,columnspan=2, sticky = W+E)
button_9.grid(row = 1, column = 3)

button_0.grid(row = 4, column = 0,columnspan=4, sticky = W+E)
button_clear.grid(row = 5, column = 0, sticky = W+E, columnspan = 4)
button_add.grid(row = 9, column = 0)
button_equal.grid(row = 6, column = 0, sticky = W+E, columnspan = 4)

button_minus.grid(row = 9, column = 1)
button_multiply.grid(row = 9, column = 2)
button_divide.grid(row = 9, column = 3)

root.mainloop()
