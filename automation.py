from runpy import _TempModule
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import time, os, requests
api_key = 'UNNAMED'

city_input = input("What city would you like to know the weather forecast for: ")
weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=metric&APPID={api_key}')
weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])
feels_like = round(weather_data.json()['main']['feels_like'])
tempmax = round(weather_data.json()['main']['temp_max'])
tempmin = round(weather_data.json()['main']['temp_min'])
if weather_data.json()['cod'] == '404':
    print("City not found.")
if feels_like == temp:
    print(f"The weather for {city_input} is {weather}, and the temperature is {temp} degrees celsius. ")
else:
    print(f"The weather for {city_input} is {weather}, and the temperature is {temp} degrees celsius. However, the temperature feels like {feels_like} degrees celsius. ")

