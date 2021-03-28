import flask
from flask import request, url_for, render_template, redirect, jsonify
import os
from apis.conversion_dicts import states, months, state_coordinates, months_string, states_to_codes
from apis import national_parks_api, climate_api, unsplash_api
import json
from database import model
from database import database
from pprint import pprint
from database.model import Park

model.create_db()
app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
  key = os.environ.get('MAPBOX_KEY')

  state = states
  month = months
  parks = []

  if request.method == 'GET':
    state_input = request.args.get("states")
    month_input = request.args.get("months")

    if state_input and month_input:
      # parks = database.get_parks_by_state(states_to_codes[state_input.upper()]) # try to get the parks from the database
      # for park in parks:
      #   print('TEST', park)
      # if parks == None: # if there aren't any parks for the state in the database, call the api to fetch it

      parks = national_parks_api.get_park_data(state_input)
      Park.delete().execute() # delete all parks in the db before saving
      database.save_parks_list(parks) # Calling a function to save all parks in the list
      json_parks = json.dumps([p.dump() for p in parks]) # translate Trip object data into json
      coordinates = state_coordinates[state_input]  # coordinates for the state entered by the user
      return render_template('markers.html', key=key, month=month, state=state, parks=json.dumps(json_parks), coordinates=coordinates, month_input=month_input)
    else:
      return render_template('index.html', key=key, month=month, state=state, coordinates=[-98.5795,39.8283], month_input=month_input) # US coordinates


@app.route('/park_info/<park_id>/<month>/', methods=['GET','POST'])
def park_info(park_id,month):
  # TO-DO fetch park info from db, make api calls for climate & unsplash data
  # return json response - return jsonify(data)
  print('park_id: ',     park_id)
  park = database.get_park_by_code(park_id)
  print(park, 'test')
  trip_w_climate = climate_api.get_weather_data(park, month)
  trip_w_climate_and_pictures = unsplash_api.get_park_image(trip_w_climate)
  database.delete_all_trips()
  trip_w_climate_and_pictures.save()
  json_trip = json.dumps(trip_w_climate_and_pictures.dump())
  return json_trip


@app.route('/saved_trip_info/<trip_id>/', methods=['GET','POST'])
def saved_trip_info(trip_id):
  if trip_id:
    trip = model.Trip.get(model.Trip.id == trip_id)
    database.save_trip(trip)
  trips = model.SavedTrip.select().execute()
  json_trips = json.dumps([t.dump() for t in trips]) 
  return json_trips

  
if __name__ == '__main__':
    app.run(debug=True)