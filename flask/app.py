import flask
from flask import request, url_for, render_template, redirect
import sys
import os
sys.path.insert(1, 'project_4/states_and_months')


app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    key = os.environ.get('MAPBOX_KEY')
    return render_template('index.html', key=key)

if __name__ == '__main__':
    app.run(debug=True)