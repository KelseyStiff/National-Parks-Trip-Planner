import requests

national_park = input('What park do you want images for? ')

random_park_image = requests.get(f'https://api.unsplash.com/photos/random?query="{national_park}";client_id=3a31301fc8edce2497d0e0dd001ec1bfbed7a207b9207dd2ccc5c87baade2b12').json()
    
image_url = random_park_image['links']['download']