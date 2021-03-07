import requests
import os
from pprint import pprint
from states_and_months import months

key = os.environ.get('CLIMATE_KEY')

url = 'https://api.meteostat.net/v2/point/climate'

"""This is the only function in this module that should be called from other modules"""
def get_weather_data(latitude, longitude, month):
    month_int = _get_month_int(month.upper())
    response = _climate_api_call(latitude, longitude)
    climate = _extract_data(response, month_int)
    return climate
    
    
def _get_month_int(month):
    month_int = months[month]
    return month_int


def _climate_api_call(latitude, longitude):
    params = {'lat' : latitude, 'lon' : longitude}
    headers={'x-api-key': key}
    response = requests.get(url, params=params, headers=headers).json()
    return response


def _extract_data(response, month):
    data = response['data']
    climate_for_month = data[month - 1]
    precipitation = climate_for_month['prcp']
    avg_temp = _convert_celsius_to_fahrenheit(climate_for_month['tavg'])
    max_temp = _convert_celsius_to_fahrenheit(climate_for_month['tmax'])
    min_temp = _convert_celsius_to_fahrenheit(climate_for_month['tmin'])
    sun_exposure = climate_for_month['tsun']

    climate = {'precipitation':precipitation, 'avg_temp':avg_temp, 'max_temp':max_temp, 
               'min_temp':min_temp, 'sun_exposure':sun_exposure}
    return climate


def _convert_celsius_to_fahrenheit(temp):
    return (temp * 1.8) + 32



# Testing module usage
pprint(get_weather_data(28, -81, 'November'))