#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 00:50:37 2023

@author: sibaamani
"""

import tkinter as tk
import requests

API_KEY = "92429d11056343e53cff0928ad9fa729"

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    
    return temperature, description, icon

def get_icon(icon):
    url = f"http://openweathermap.org/img/wn/{icon}.png"
    response = requests.get(url)
    icon_data = response.content
    
    return icon_data

def get_color(description):
    if 'cloud' in description:
        return 'gray'
    elif 'rain' in description:
        return 'blue'
    elif 'sun' in description:
        return 'orange'
    else:
        return 'green'

def show_weather():
    city = entry.get()
    temperature, description, icon = get_weather(city)
    icon_data = get_icon(icon)
    color = get_color(description)
    
    image = tk.PhotoImage(data=icon_data)
    weather_label.configure(image=image)
    weather_label.image = image
    
    temperature_label.configure(text=f"Temperature: {temperature}°C")
    description_label.configure(text=f"Description: {description}", fg=color)

# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create the input field and search button
entry = tk.Entry(root)
entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=show_weather)
search_button.pack(pady=5)

# Create labels for displaying weather information
weather_label = tk.Label(root)
weather_label.pack()

temperature_label = tk.Label(root, font=("Arial", 20))
temperature_label.pack(pady=5)

description_label = tk.Label(root, font=("Arial", 14))
description_label.pack()

# Run the main window's event loop
root.mainloop()

