import requests
from prettyprinter import pprint
import os
key = os.environ.get('NATIONAL_PARKS_KEY')
querry = {'api_key': key}

urls = ['https://developer.nps.gov/api/v1/parks?&',
'https://developer.nps.gov/api/v1/parks?start=101&',
'https://developer.nps.gov/api/v1/parks?start=51&', 
'https://developer.nps.gov/api/v1/parks?start=151&', 
'https://developer.nps.gov/api/v1/parks?start=202&', 
'https://developer.nps.gov/api/v1/parks?start=252&', 
'https://developer.nps.gov/api/v1/parks?start=302&', 
'https://developer.nps.gov/api/v1/parks?start=352&',
'https://developer.nps.gov/api/v1/parks?start=402&',
'https://developer.nps.gov/api/v1/parks?start=452&'
]


try:
     User_states = input('Enter:')
     for l in urls: # Since the api has a limit of 50 parks, we have to have multiple apis to run after each other. This line loops through all the 400 data in the api
        data= requests.get(l, params=querry).json()
        #pprint(data)
        list_of_parks = data['data']
       
        for x in list_of_parks:
            #name = x['fullname']
            state = x['states']

            if state == User_states:
                name = x['fullName']
                latitude = x['latitude']
                longitude = x['longitude']
                description = x['description']
                address = x['addresses'][1]
                city = address['city']
                weather_info = x['weatherInfo']
                postalcode = address['postalCode']
                line1 = address['line1']
                state_code= address['stateCode']

                print(f'Name: {name}, address: {line1}, {city}, {state_code},{postalcode} \n Weather info : {weather_info}')
            
except: 
    print('API not responding')      
