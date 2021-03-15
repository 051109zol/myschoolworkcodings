from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title ("Using Icons Images, and Exit Buttons")
root.iconbitmap("pewds_qmL_icon.ico")

my_img1 = ImageTk.PhotoImage(Image.open("gamba/anomaly1.jpg"))
my_img2= ImageTk.PhotoImage(Image.open("gamba/anomaly 2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("gamba/anomaly 3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("gamba/ANOMALY.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("gamba/big smoke.jpg"))
my_img6= ImageTk.PhotoImage(Image.open("gamba/SHREK.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("gamba/STING AKU YAHOO YAHOO.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7]

status = Label (root, text = " Image 1 of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E )

my_label = Label(image = my_img1)
my_label.grid ( row = 0, column = 0, columnspan = 3 )

def forward (image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label ( image = image_list [image_number-1] )
    button_forward = Button (root, text = ">>", fg="blue", bg="yellow", padx=5, pady=10, command = lambda: forward(image_number+1))
    button_back = Button (root, text = "<<", fg="blue", bg="yellow", padx=5, pady=10, command = lambda: back(image_number-1))

    if image_number == 7 :
        button_forward = Button (root, text = ">>", fg="blue", bg="yellow", padx=5, pady=10, state = DISABLED)
    
    my_label.grid ( row = 0, column = 0, columnspan = 3 )
    button_back.grid ( row = 1, column = 0 )
    button_forward.grid ( row = 1, column = 2 )

    status = Label (root, text = " Image " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E )
    status.grid ( row = 2, column = 0, columnspan = 3, sticky = W+E )
    
def back (image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label ( image = image_list [image_number-1] )
    button_forward = Button (root, text = ">>", fg="blue", bg="yellow", padx=5, pady=10, command = lambda: forward(image_number+1))
    button_back = Button (root, text = "<<", fg="blue", bg="yellow", padx=5, pady=10, command = lambda: back(image_number-1))
    
    if image_number == 1 :
        button_back = Button (root, text = "<<", fg="blue", bg="yellow", padx=5, pady=10, state = DISABLED)
        
    my_label.grid ( row = 0, column = 0, columnspan = 3 )
    button_back.grid ( row = 1, column = 0 )
    button_forward.grid ( row = 1, column = 2 )

    #Update status bar
    status = Label (root, text = " Image " + str(image_number) + " of " + str(len(image_list)), bd = 1, relief = SUNKEN, anchor = E )
    status.grid ( row = 2, column = 0, columnspan = 3, sticky = W+E )

button_back = Button (root, text = "<<", fg="blue", bg="yellow", padx=5, pady=10, command = back, state = DISABLED)
button_forward = Button (root, text = ">>", fg="blue", bg="yellow", padx=5, pady=10, command = lambda: forward(2)) 
button_quit = Button (root, text = "End Program", fg="blue", bg="yellow", padx=5, pady=10, command = root.quit)

button_back.grid ( row = 1, column = 0 )
button_quit.grid ( row = 1, column = 1 )
button_forward.grid ( row = 1, column = 2 , pady = 5)
status.grid ( row = 2, column = 0, columnspan = 3, sticky = W+E )

root.mainloop()
