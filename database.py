from model import Trip
import model
import peewee
from peewee import IntegrityError


"""
Accepts all values for a park object and saves it to the database. All parameters are required except images.
Some park names may not pull up enough pictures.
"""
def save_trip(name, city, state, description, latitude, longitude, image1=None, image2=None, image3=None):  
    try:
        Trip.create(
            park_name = name, 
            park_city = city, 
            park_state = state, 
            park_description = description, 
            latitude = latitude, 
            longitude = longitude, 
            image_1 = image1, 
            image_2 = image2, 
            image_3 = image3
            )
    except IntegrityError:
        return "There was an issue while trying to save this trip."


def get_trip_by_park_name(park_name): # Returns none if park not in database
    return Trip.get_or_none(park_name = park_name)


"""Returns all saved trips objects"""
def get_all_trips():
    trips = Trip.select()
    return trips


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


def delete_all_trips():
    Trip.delete().execute()


def delete_trip_by_park_name(park_name):
    trip = get_trip_by_park_name(park_name)
    if trip != None:
        Trip.delete_instance(trip)


# model.create_db()
# save_trip('Yellowstone National Park', 'Middlanoware', 'Wyoming', 'Beautiful scenic park.', 1234567.89, 9876543.21, 'sldksjdlf', 'sdlkjsdfl', 'sldkjsldkfd')
# save_trip('Yosemite', 'Somewhere', 'Nevada', 'Cool national park.', 1234567.890, 09876543.21, 'sldksjdl', 'sdlkjsdf', 'sldkjsldkf')
# save_trip('Random Park', 'A City', 'Somewherolina', 'This is the park description.', 555555.55, 66666.66, 'asdfsdfs', 'sdfdfsdsfdaf', 'sdfsdfadfasdf')
