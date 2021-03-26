import requests
from pprint import pprint
import os
from .states_and_months import states
from database.model import Park

key = os.environ.get('NATIONAL_PARKS_KEY')





urls = [f'https://developer.nps.gov/api/v1/parks?&api_key={key}',
f'https://developer.nps.gov/api/v1/parks?start=51&api_key={key}',
f'https://developer.nps.gov/api/v1/parks?start=101&api_key={key}', 
f'https://developer.nps.gov/api/v1/parks?start=151&api_key={key}', 
f'https://developer.nps.gov/api/v1/parks?start=201&api_key={key}', 
f'https://developer.nps.gov/api/v1/parks?start=251&api_key={key}', 
f'https://developer.nps.gov/api/v1/parks?start=301&api_key={key}', 
f'https://developer.nps.gov/api/v1/parks?start=351&api_key={key}',
f'https://developer.nps.gov/api/v1/parks?start=401&api_key={key}',
f'https://developer.nps.gov/api/v1/parks?start=451&api_key={key}',
]

"""All interaction with this module should be done through this function"""
def get_park_data(state):
    state_code = _get_state_code(state.upper())
    list_of_parks = _call_park_api()
    parks = _create_trip_object_list(list_of_parks, state_code)
    return parks


def _create_trip_object_list(list_of_parks, state_code):   
    parks_in_state = []
    try:
        # Since the api has a limit of 50 parks, we have to have multiple urls to run after each other. This line loops through all the 400 data in the api   
        for park in list_of_parks:
            state = park['states']

            if state == state_code:
                park_id = park['parkCode']
                park_name = park['fullName']     
                park_state = park['states']
                park_description = park['description']
                latitude = park['latitude']
                longitude = park['longitude']                
                try:
                    address = park['addresses'][1]
                    park_city = address['city']
                except:
                    address = 'Unknown Address'
                    park_city = 'Unknown City'
  
                park = Park(park_id = park_id, park_name = park_name, park_city = park_city, park_state = park_state, 
                            park_description = park_description, latitude = latitude, longitude = longitude)
                
                parks_in_state.append(park)         
      
        return parks_in_state
    except KeyError:
        return "There are no parks for that state."


def _get_state_code(state):
    try:
        state_code = states[state] # Convert full state to 2 letter state code
        return state_code
    except KeyError:
        return "Invalid state."


def _call_park_api():
    try:
        list_of_parks = []
        for u in urls:
            data = requests.get(u).json()
            for d in data['data']:
                list_of_parks.append(d)
        return list_of_parks   
    except ConnectionError:
        return "Error getting data. Try checking your internet connection."


# parks = get_park_data('UTah', 'November')
# for park in parks:
#         print(park)