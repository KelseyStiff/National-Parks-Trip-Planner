import requests
import os
from pprint import pprint
from states_and_months import months

key = os.environ.get('CLIMATE_KEY')

url = 'https://api.meteostat.net/v2/point/climate'

def get_weather_data(latitude, longitude, month):
    month_int = _get_month_int(month.upper())
    params = {'lat' : latitude, 'lon' : longitude}
    headers={'x-api-key': key}
    resp = requests.get(url, params=params, headers=headers).json()
    data = resp['data']
    climate_for_month = data[month_int - 1]
    return climate_for_month


def _get_month_int(month):
    month_int = months['month']



get_weather_data(44, -93, 12)