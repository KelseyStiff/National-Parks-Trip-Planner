import flask
from flask import request, url_for, render_template, redirect

app = flask.Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    # content for app goes here 
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)