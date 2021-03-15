from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk ()
root.title ("My weather app")
root.iconbitmap("pewds_qmL_icon.ico")
root.geometry("400x40")

#[{"DateObserved":"2020-12-05 ","HourObserved":3,"LocalTimeZone":"CST","ReportingArea":"Austin","StateCode":"TX","Latitude":30.267,"Longitude":-97.734,"ParameterName":"O3","AQI":11,"Category":{"Number":1,"Name":"Good"}},
#{"DateObserved":"2020-12-05 ","HourObserved":3,"LocalTimeZone":"CST","ReportingArea":"Austin","StateCode":"TX","Latitude":30.267,"Longitude":-97.734,"ParameterName":"PM2.5","AQI":103,"Category":{"Number":3,"Name":"Unhealthy for Sensitive Groups"}}]
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=78736&distance=42&API_KEY=E3FF01A3-B9A2-4315-957B-A78A2E1C049E

# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=42069&distance=69&API_KEY=E3FF01A3-B9A2-4315-957B-A78A2E1C049E

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=78736&distance=42&API_KEY=E3FF01A3-B9A2-4315-957B-A78A2E1C049E")
    api = json.loads (api_request.content)
    city = api[1]['ReportingArea']
    quality = api[1]['AQI']
    category = api[1]['Category']['Name']

# colour in hexa copied from inspect element
# --color-super-light-grey: #e3e3e3; --color-card-border-grey: #E0E0E0; --color-silver: #C0C0C0; --color-light-grey: #D5D5D5; --color-solid-grey: #808080; --color-dark-blue: #167fac; 
# --color-aqi-green: #00e400; --color-aqi-yellow: #ffff00; --color-aqi-orange: #ff7e00; --color-aqi-red: #ff0000; --color-aqi-purple: #99004c; --color-aqi-maroon: #7e0023;

    if category == "Good":
        weather_color = "#00e400"
    elif category == "Moderate":
        weather_color = "#ffff00"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color = "#ff7e00"
    elif category == "Unhealthy":
        weather_color = "#ff0000"
    elif category == "Very Unhealthy":
        weather_color = "#99004c"
    elif category == "Hazardous":
        weather_color = "#7e0023"

    root.configure (background=weather_color)
    
    myLabel = Label(root, text=city + ", Air Quality = " + str(quality) + " / Category = " + category, font=("Patrick Hand", 16), background =weather_color)
    myLabel.pack()
except Exception as e:
    api = "Error..."

root.mainloop()
