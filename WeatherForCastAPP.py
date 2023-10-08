

from tkinter import font
import requests
import tkinter as tk
from tkinter.font import Font

API_KEY = "2b1da4b62d994fb8bfb172510230410"



def get_weather():
    city = entry.get()
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        result_label.config(text="City not found.", font=a)
        return

    temperature = data['current']['temp_c']
    humidity = data['current']['humidity']
    wind_speed = data['current']['wind_kph']
    description = data['current']['condition']['text']

    result_label.config(text=f"Temperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} km/h\nDescription: {description}", font =a)

# Create the GUI
window = tk.Tk()
window.title("Weather Forecast APP")
window.geometry("300x400")

# Configure Poppins font
a = font.Font(family="Poppins", size=10)


# Set Poppins font for labels and entry
label = tk.Label(window, text="Enter City :", font=a)
label.pack(pady=10)

entry = tk.Entry(window, font=a)
entry.pack()

button = tk.Button(window, text="Get Weather Report", command=get_weather, font=a , bg="#4CAF50", fg="black")
button.pack()

result_label = tk.Label(window, text="", font=a )
result_label.pack()

Credit_label = tk.Label(window, text="Code By Vijaya Kumar Annam", wraplength=250 , pady= 50,
                        font=Font(family='Poppins', size=12, weight='bold'), fg="black")
Credit_label.pack()

window.mainloop()


#Code by Vijaya Kumar