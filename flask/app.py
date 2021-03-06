import flask
from flask import request, url_for, render_template, redirect
import sys
sys.path.insert(1, 'project_4/states_and_months')

app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    # content for app goes here 
    # key = os.environ.get('MAPBOX_KEY')
    key = 'pk.eyJ1Ijoia2l0dHlzdGlmZiIsImEiOiJjazZ2aDF3ZzcwMXNxM2hvMmJiZTlvaTI5In0.oEO-8s7LpbrCHJatQnXVKg'
    return render_template('index.html', key=key)

if __name__ == '__main__':
    app.run(debug=True)