import flask
from flask import request, url_for, render_template, redirect
import os
from states_months import states, months, state_coordinates
from apis import national_parks_api
import json

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
      parks = national_parks_api.get_park_data(state_input,month_input)
      json_parks = json.dumps([p.dump() for p in parks]) # translate Trip object data into json
      coordinates = state_coordinates[state_input]  # coordinates for the state entered by the user
      return render_template('markers.html', key=key, month=month, state=state, parks=json.dumps(json_parks), coordinates=coordinates)
    else:
      return render_template('index.html', key=key, month=month, state=state, coordinates=[-98.5795,39.8283]) # US coordinates



# @app.route('/trip-info/<int:tripid>')
# def trip_info(parkid):
#   #to-do trip 



if __name__ == '__main__':
    app.run(debug=True)