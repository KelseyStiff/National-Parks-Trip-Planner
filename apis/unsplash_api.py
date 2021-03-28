import requests
import os
from pprint import pprint
from database.model import Trip

key = os.environ.get('UNSPLASH_KEY')



url = 'https://api.unsplash.com/search/photos'
number_of_images = 4

def get_park_image(trip):
    response = _unsplash_api_call(trip.park.park_name)
    trip_with_images = _extract_data(response, trip)
    return trip_with_images


def _unsplash_api_call(park):
    query = {'query':park, 'per_page':number_of_images, 'client_id':key}
    response = requests.get(url, params=query).json()
    return response


def _extract_data(response, trip):
    images = response['results']
    trip.image_1 = images[0]['urls']['small']
    trip.image_2 = images[1]['urls']['small']
    trip.image_3 = images[2]['urls']['small']
    trip.image_4 = images[3]['urls']['small']
    return trip
    









