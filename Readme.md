About:
This program provides information about national parks around the united states. The program only takes the state and the month that you are planning to travel, and it will give you information such as the description of the parks, the weather condition, complete address, and the location of the parks on the map. 
This app's main structure is python, and we used Javascript, HTML, CSS for ease of use, and a better user interface.

In order to run this application, run the command: pip install requirement.txt

this should install everything needed, if issues installing flask via requirments run command below
$ pip install Flask
and then run flask
$ flask run

for more information on flask installation:
https://flask.palletsprojects.com/en/1.1.x/installation/

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


CREDS:
Page Title image by <a href="https://unsplash.com/@simonmigaj?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Simon Migaj</a> on <a href="https://unsplash.com/s/photos/travel-app?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

most of our flask set up was adapted from flasks documentation:
https://flask.palletsprojects.com/en/1.1.x/
https://flask.palletsprojects.com/en/1.1.x/quickstart/

referenced this link for passing objects to template:
https://stackoverflow.com/questions/47169097/passing-objects-through-flask-urls

adapted this code from stackoverflow for fetching data within a Javascript function:
https://stackoverflow.com/questions/58777484/how-to-access-outside-the-js-fetch-api-the-returned-value

adapted and referenced how to use the dumps method:
https://www.geeksforgeeks.org/json-dump-in-python/






  

KNOWN BUGS:

* when clicking on the 'Lincoln Boyhood' Park causes errors (unknown cause)
* some random parks cause an error as well (unknown cause)


UNFINISHED FEATURES:

displaying saved trips needs better formatting (like in a table)
no delete saved trip option - database function exists but no feature to do so in the template
error handling - there is a pull request for error handling that we did not merge bc fear of too many conflicts with master



Authors: 
Kelsey Stiff, Andrea Pratt, Mohammad Sargazi
