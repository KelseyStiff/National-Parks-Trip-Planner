import requests
from prettyprinter import pprint
urls = ['https://developer.nps.gov/api/v1/parks?&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb',
'https://developer.nps.gov/api/v1/parks?start=101&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb',
'https://developer.nps.gov/api/v1/parks?start=51&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb', 
'https://developer.nps.gov/api/v1/parks?start=151&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb', 
'https://developer.nps.gov/api/v1/parks?start=202&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb', 
'https://developer.nps.gov/api/v1/parks?start=252&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb', 
'https://developer.nps.gov/api/v1/parks?start=302&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb', 
'https://developer.nps.gov/api/v1/parks?start=352&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb',
'https://developer.nps.gov/api/v1/parks?start=402&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb',
'https://developer.nps.gov/api/v1/parks?start=452&api_key=8KEJWdmy0u98yA2aqe9uLH5A2SVkNzBzhjez2xMb',
]


try:
     User_states = input('Enter:')
     for l in urls: # Since the api has a limit of 50 parks, we have to have multiple apis to run after each other. This line loops through all the 400 data in the api
        data= requests.get(l).json()
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

                #print(f'{name} : latitude: {latitude}, longitude: {longitude}') 
                print(name)
except: 
    print('API not responding')      
