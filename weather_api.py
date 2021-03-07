import requests
import os
from pprint import pprint

key = 'd5iUahogk60F0E2GYZ2OK37j9LpL0hSm'
url = 'https://api.meteostat.net/v2/point/climate?lat=44&lon=-93&alt=58'

headers={'x-api-key': key}

resp = requests.get(url,headers=headers)

pprint(resp.json())
