import requests
import os
from pprint import pprint

key = os.environ.get('UNSPLASH_KEY')
url = 'https://api.unsplash.com/search/photos'
number_of_images = 3

def get_park_image(park):
    response = _unsplash_api_call(park)
    images = _extract_data(response)
    return images


def _unsplash_api_call(park):
    query = {'query':park, 'per_page':number_of_images, 'client_id':key}
    response = requests.get(url, params=query).json()
    return response


def _extract_data(response):
    image_urls = []
    images = response['results']
    for image in images:
        image_urls.append(image['urls']['small'])
    return image_urls


# Test module usage
pprint(get_park_image('Yosemite'))