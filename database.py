from model import Trip
import model
import peewee
from peewee import IntegrityError


"""
Accepts all values for a park object and saves it to the database. All parameters are required except images.
Some park names may not pull up enough pictures.
"""
def save_trip(trip):  
    try:
        Trip.create(
            month = trip.month,
            park_name = trip.park_name, 
            park_city = trip.park_city, 
            park_state = trip.park_state, 
            park_description = trip.park_description, 
            latitude = trip.latitude, 
            longitude = trip.longitude, 
            image_1 = trip.image_1, 
            image_2 = trip.image_2, 
            image_3 = trip.image_3,
            precipitation = trip.precipitation,
            avg_temp = trip.avg_temp,
            max_temp = trip.max_temp,
            min_temp = trip.min_temp
            )
    except IntegrityError:
        return "There was an issue while trying to save this trip."


"""Returns all saved trip objects"""
def get_all_trips():
    return Trip.select()


def delete_all_trips():
    Trip.delete().execute()


def get_trip_by_park_name(park_name): # Returns none if park not in database
    return Trip.get_or_none(park_name = park_name)


def get_park_city(park_name): # Returns None if the park's not found
    trip = get_trip_by_park_name(park_name)
    if trip != None:
        return trip.park_city
    else:
        return None


def get_park_latitude_by_name(park_name):
    trip = get_trip_by_park_name(park_name)
    return float(trip.latitude)


def get_park_longitude_by_name(park_name):
    trip = get_trip_by_park_name(park_name)
    return float(trip.longitude)
    

"""Returns a dictionary containing the float coordinates of all saved parks"""
def get_all_trips_coordinates(): 
    trips = get_all_trips()
    coordinates = {}
    for park in trips:
        coordinates.update({float(park.latitude) : float(park.longitude)}) 
    return coordinates


def delete_trip_by_park_name(park_name):
    trip = get_trip_by_park_name(park_name)
    if trip != None:
        Trip.delete_instance(trip)


#Test functionality
model.create_db()
trip = Trip(month='November', park_name='Random Park Name', park_city='Randomville', park_state='Randesota', 
            park_description='A random cool park.', latitude=25.761681, longitude=-80.191788, image_1='someurl.com', 
            image_2='someotherurl.com', image_3='anotherurl.com', precipitation=58, avg_temp=62.5, max_temp=89.3, min_temp=33.9)
save_trip(trip)