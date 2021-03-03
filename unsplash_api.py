import requests
import os

national_park = input('What park do you want images for? ')

key = os.environ('UNSPLASH_KEY')

random_park_image = requests.get(f'https://api.unsplash.com/photos/random?query="{national_park}";client_id={key}').json()
    
image_url = random_park_image['links']['download']