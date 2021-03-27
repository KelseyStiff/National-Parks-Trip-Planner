from . import model 
from .model import Trip
import peewee
from peewee import IntegrityError
from .model import Park, SavedTrip


def save_parks_list(parks):
    try:
        for p in parks:
            p.save()
    except IntegrityError:
        return "Data already in database."


def get_parks_by_state(state):
    Park.select().where(Park.park_state == state)
    

def save_trip(trip):  
    saved_trips = SavedTrip.select().execute()
    unique = True
    for s in saved_trips:
        if s == trip:
            unique = False
    if unique:
        model.SavedTrip.create(month = trip.month, park = trip.park, image_1 = trip.image_1, image_2 = trip.image_2,
                                image_3 = trip.image_3, image_4 = trip.image_4, precipitation = trip.precipitation,
                                avg_temp = trip.avg_temp, max_temp = trip.max_temp, min_temp = trip.min_temp)
        return "Success!"


def get_park_by_code(code):
    park = Park.get(Park.park_id == code)
    return park


"""Returns all saved trip objects"""
def get_all_trips():
    return Trip.select()


def delete_all_trips():
    Trip.delete().execute()


