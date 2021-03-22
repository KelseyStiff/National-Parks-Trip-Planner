import flask
from flask import request, url_for, render_template, redirect
import os
from states_months import states, months
from apis import national_parks_api

app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
 # key = os.environ.get('MAPBOX_KEY')
  key = 'pk.eyJ1Ijoia2l0dHlzdGlmZiIsImEiOiJjazZ2aDF3ZzcwMXNxM2hvMmJiZTlvaTI5In0.oEO-8s7LpbrCHJatQnXVKg'
  state = states
  month = months
  parks = []

  if request.method == 'GET':
    state_input = request.args.get("states")
    month_input = request.args.get("months")

    if state_input and month_input:
      parks = national_parks_api.get_park_data(state_input,month_input)
      return render_template('index.html', key=key, month=month, state=state, parks=parks)
  else:
    pass # TODO - add error response

  return render_template('index.html', key=key, month=month, state=state, parks=parks)


if __name__ == '__main__':
    app.run(debug=True)