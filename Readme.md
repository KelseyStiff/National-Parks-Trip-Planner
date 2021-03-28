About:
This program provides information about national parks around the united states. The program only takes the state and the month that you are planning to travel, and it will give you information such as the description of the parks, the weather condition, complete address, and the location of the parks on the map. 
This app's main structure is python, and we used Javascript, HTML, CSS for ease of use, and a better user interface.

Requirements: 
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
Flask==1.1.2
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.3
MarkupSafe==1.1.1
peewee==3.14.1
requests==2.25.1
urllib3==1.26.3
Werkzeug==1.0.1

In order to run the program, you first need to install flask
$ pip install Flask
and then run flask
$ flask run

Run the port that has been given to you in a browser, and you can use the app.
NOTE: You need to create a free account in the websites provided below in order to get your API key (having an API key is necessary to run the program)
1- https://www.nps.gov/subjects/developer/get-started.htm
2- https://unsplash.com/developers
3- https://dev.meteostat.net/api/
4 - https://docs.mapbox.com/help/getting-started/access-tokens/


UI: 
The main page displays a line with two questions that the user can use the dropdowns to answer to the questions. 
Below the questions, there is an extensive map of the united states.
When you answer the questions and click on search, the app will display all the national parks on the map with small markers of each park's location. 
You can get more details of each park by clicking on the markers shown on the map. And save the trip information/view saved trips by selecting the save button


KNOWN BUGS/UNFINISHED FEATURES:


Authors: 
Kelsey Stiff, Andrea Pratt, Mohammad Sargazi
