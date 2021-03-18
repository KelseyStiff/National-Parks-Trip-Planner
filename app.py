import flask
from flask import request, url_for, render_template, redirect
import sys
import os
import states_months


app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    key = os.environ.get('MAPBOX_KEY')
    months = states_months.months
    states = states_months.states
    return render_template('index.html', key=key, months=months, states=states)


if __name__ == '__main__':
    app.run(debug=True)