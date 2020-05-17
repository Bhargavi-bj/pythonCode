# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:17:29 2020

@author: Bhargavi
"""

import requests
import json

url = "http://api.openweathermap.org/data/2.5/weather?appid=dfd08836f69e222c49d7cd5f316b9eee&q="
city = input("Enter city name:")

new_url = url + city

json_data = requests.get(new_url).json()
temp_obtained = json_data['main']['temp']
data_obtained = json_data['weather'][0]['description']
humidity_obtained = json_data['main']['humidity']
wind_speed = json_data['wind']['speed']
long_data = json_data['coord']['lon']
lat_data = json_data['coord']['lat']
print("")
print("The co-ordinates are: ",lat_data,"N ",long_data,"E")
print("The temperature is : ",temp_obtained," kelvin")
print("Weather: ",data_obtained)
print("Humidity: ",humidity_obtained)
print("Wind Speed:",wind_speed)
