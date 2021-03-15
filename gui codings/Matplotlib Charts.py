from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk ()
root.title ("We do coding yes")
root.iconbitmap("pewds_qmL_icon.ico")
root.geometry("400x200")

#learn more about this i dono how to set custom amon this only random 00000
#https://matplotlib.org/3.3.3/index.html

def graph():
    house_prices = np.random.normal(2000, 250, 50)
    plt.polar(house_prices)
    plt.show()

my_button = Button (root, text = "You want see Graph men ?", command = graph)
my_button.pack()

root.mainloop()
