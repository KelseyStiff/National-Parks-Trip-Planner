import requests
from pprint import pprint
import os
from .conversion_dicts import states_to_codes
from database.model import Park

key = os.environ.get('NATIONAL_PARKS_KEY')




"""All interaction with this module should be done through this function"""
def get_park_data(state):
    state_code = _get_state_code(state.upper())
    url = f'https://developer.nps.gov/api/v1/parks?stateCode={state_code}&api_key={key}'
    list_of_parks = _call_park_api(url)
    parks = _create_trip_object_list(list_of_parks, state_code)
    return parks


def _create_trip_object_list(list_of_parks, state_code):   
    parks_in_state = []
    for park in list_of_parks:
        try:
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
        except KeyError:
            return parks_in_state
    return parks_in_state


def _get_state_code(state):
    try:
        state_code = states_to_codes[state] # Convert full state to 2 letter state code
        return state_code
    except KeyError:
        return "Invalid state."


def _call_park_api(url):
    list_of_parks = []
    try:
        data = requests.get(url).json()  
        for d in data['data']:
            list_of_parks.append(d)
        return list_of_parks   
    except ConnectionError:
        return "Error getting data. Try checking your internet connection."
