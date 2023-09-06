import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

# load env variable and get api key
load_dotenv()
api_key = os.getenv('API_KEY')

# define a data class to represent weather data
@dataclass
class WeatherData:
    main: str               # condition
    description: str        # description
    icon: str               # icon code
    temperature: int        # temperature in fahrenheit 

# function to fetch lat and lon coords for given location
def get_lat_lon(city_name, state_code, country_code, API_key):
    response = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    # get lat and lon from API response
    data = response[0]
    lat, lon = data.get('lat'), data.get('lon')
    return lat, lon

# function to fetch current weather from the API response
def get_current_weather(lat, lon, API_key):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=imperial').json()
    # extract weather related inforrmation 
    data = WeatherData(
        main = response.get('weather')[0].get('main'),
        description = response.get('weather')[0].get('description'),
        icon = response.get('weather')[0].get('icon'),
        temperature = int(response.get('main').get('temp'))
    )

    return data

# main function to get weather data 
def main(city_name, state_code, country_name):
    lat, lon = get_lat_lon(city_name, state_code, country_name, api_key)
    weather_data = get_current_weather(lat, lon, api_key)
    return weather_data


