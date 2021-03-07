import requests
import os
from pprint import pprint

key = os.environ.get('CLIMATE_KEY')
url = 'https://api.meteostat.net/v2/point/climate?lat=44&lon=-93&alt=58'

headers={'x-api-key': key}

resp = requests.get(url,headers=headers)

pprint(resp.json())
