from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk ()
root.title ("My weather app")
root.iconbitmap("pewds_qmL_icon.ico")
root.geometry("400x40")
root.configure (background = 'green')

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=42069&distance=69&API_KEY=E3FF01A3-B9A2-4315-957B-A78A2E1C049E

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=42069&distance=69&API_KEY=E3FF01A3-B9A2-4315-957B-A78A2E1C049E")
    api = json.loads (api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
except Exception as e:
    api = "Error..."

# 4 : 58
myLabel = Label(root, text=city + ", Air Quality = " + str(quality) + " / Category = " + category, font=("Patrick Hand", 16), background = "green")
myLabel.pack()

root.mainloop()
