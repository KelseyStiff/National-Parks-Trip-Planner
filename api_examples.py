import requests
from pprint import pprint
import os

"""Functioning weather API"""
def get_weather_api_data():
    key = os.environ.get('WEATHER_KEY')
    location = 'paris, fr'

    query = {'q' : location, 'units' : 'imperial', 'appid' : key}
    weather_url = 'http://api.openweathermap.org/data/2.5/forecast'
    response = requests.get(weather_url, params=query)
    data = response.json()
    pprint(data)


"""Currency exchange API functioning properly"""
def get_currency_api_data():
    params = {'base': 'USD', 'symbols': 'EUR'}
    url = 'https://api.exchangeratesapi.io/latest'
    pprint(requests.get(url, params=params).json())


"""Functioning Google Translate API"""
def get_translation_data():
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    # payload = "q=Je%2C%20suis%2C%20une%2C%20fille&target=en" This is the format for a query

    while True:
        text_to_translate = input('What do you want to translate? ')

        single_space_example_input = " ".join(text_to_translate.split())  # Remove extra spaces

        final_string = single_space_example_input.replace(' ', '%2C%20') # Replace spaces with the query seperator

        language_to_translate_to = 'fr'

        payload = f'q={final_string}&target={language_to_translate_to}'

        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept-encoding': "application/gzip",
            'x-rapidapi-key': "f33d94cb5amsh22be35ae89cf691p112258jsn8f57fa76be02",
            'x-rapidapi-host': "google-translate1.p.rapidapi.com"
            }

        response = requests.request("POST", url, data=payload, headers=headers).json()


        translation = response['data']['translations'][0]['translatedText']
        original_language = response['data']['translations'][0]['detectedSourceLanguage']

        print(f'Translation: {translation}\nOriginal Text Language: {original_language}')

        if text_to_translate == '':
            break

    
def get_points_of_interest():
    key = '5b3ce3597851110001cf6248b08a97b53d964b5e8aaf1a905b7cf551'

    body = {"request":"pois","geometry":{"bbox":[[8.8034,53.0756],[8.7834,53.0456]],"geojson":{"type":"Point","coordinates":[8.8034,53.0756]},"buffer":200}}

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
        'Authorization': '5b3ce3597851110001cf6248b08a97b53d964b5e8aaf1a905b7cf551',
        'Content-Type': 'application/json; charset=utf-8'
        }
      
    call = requests.post('https://api.openrouteservice.org/pois', json=body, headers=headers).json()


    for i in range(10):
        try:
            pprint(call[0]['features'][i]['properties']['osm_tags']['name'])
        except:
            continue


    
get_points_of_interest()