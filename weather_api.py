import requests
import os

url = 'https://history.openweathermap.org/data/2.5/aggregated/year?lat=35&lon=139&appid=a7d9ecfa2043441c1eafcf7528d24379'

response = requests.get(url).json()

print(response)

