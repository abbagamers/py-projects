import datetime
from runpy import _TempModule
from ssl import ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY
import time, os, requests
from apifile import *
api_key = api
t=datetime.date.today()

#api stored in another file
city_input = input("What city would you like to know the weather forecast for: ")
weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=metric&APPID={api_key}')
cod = weather_data.json()['cod']
more_lines = [city_input, cod]
if cod != 200:
    with open('errors\log.txt', 'a') as f:
     f.write('\n'.join(more_lines))
     quit()
weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])
feels_like = round(weather_data.json()['main']['feels_like'])
tempmax = round(weather_data.json()['main']['temp_max'])
tempmin = round(weather_data.json()['main']['temp_min'])

if feels_like == temp:
    print(f"The weather for {city_input} is {weather}, and the temperature is {temp} degrees celsius. ")
else:
    print(f"The weather for {city_input} is {weather}, and the temperature is {temp} degrees celsius. However, the temperature feels like {feels_like} degrees celsius. ")
mm_question = input('Would you like to see the min and max temperatures? (y/n):')

if mm_question == 'y' or mm_question == 'Y':
    print(f"The minimum temperature for {city_input} is {tempmin}, and the maximum temperature for {city_input} is {tempmax}. ")
else:
    quit()
print(weather_data.json())
