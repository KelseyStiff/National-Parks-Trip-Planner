import requests
import os

# TODO add exception handling for connection error, and key error (some searches may not return an image)

national_park = input('What park do you want images for? ')

key = os.environ.get('UNSPLASH_KEY')

random_park_image = requests.get(f'https://api.unsplash.com/photos/random?query="{national_park}";client_id={key}').json()
    
image_url = random_park_image['links']['download']

print(image_url)