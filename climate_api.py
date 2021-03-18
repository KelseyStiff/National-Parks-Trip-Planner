import requests
import os
from pprint import pprint
from states_and_months import months
from trip import Trip

key = os.environ.get('CLIMATE_KEY')

url = 'https://api.meteostat.net/v2/point/climate'

"""This is the only function in this module that should be called from other modules"""
def get_weather_data(trip):
    month_int = _get_month_int(trip.month.upper())
    response = _climate_api_call(trip.latitude, trip.longitude)
    trip_with_climate = _add_climate_data_to_trip(response, trip, month_int)
    return trip_with_climate
    
    
def _get_month_int(month):
    month_int = months[month]
    return month_int


def _climate_api_call(latitude, longitude):
    params = {'lat' : latitude, 'lon' : longitude}
    headers={'x-api-key': key}
    response = requests.get(url, params=params, headers=headers).json()
    return response


def _add_climate_data_to_trip(response, trip, month):
    data = response['data']
    climate_for_month = data[month - 1]
    precipitation = climate_for_month['prcp']
    avg_temp = _convert_celsius_to_fahrenheit(climate_for_month['tavg'])
    max_temp = _convert_celsius_to_fahrenheit(climate_for_month['tmax'])
    min_temp = _convert_celsius_to_fahrenheit(climate_for_month['tmin'])

    trip.precipitation = precipitation
    trip.avg_temp = round(avg_temp, 2)
    trip.max_temp = round(max_temp, 2)
    trip.min_temp = round(min_temp, 2)
    return trip


def _convert_celsius_to_fahrenheit(temp):
    return (temp * 1.8) + 32



# Testing module usage
trip = Trip(month='November', park_name='Random Park Name', park_city='Randomville', park_state='Randesota', 
            park_description='A random cool park.', latitude=25.761681, longitude=-80.191788)

print(get_weather_data(trip))
