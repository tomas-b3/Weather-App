import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")


user_input = input("Enter a city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")

print(weather_data.json())

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = weather_data.json()['main']['humidity']

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºC")
    print(f"Humidity in {user_input} is: {humidity}%")
