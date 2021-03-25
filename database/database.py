from . import model 
from .model import Trip
import peewee
from peewee import IntegrityError
from .model import Park


"""
Accepts all values for a park object and saves it to the database. All parameters are required except images.
Some park names may not pull up enough pictures.
"""

def save_parks_list(parks):
    try:
        for p in parks:
            p.save()
    except IntegrityError:
        return "Data already in database."


def get_parks_by_state(state):
    Park.select().where(Park.park_state == state)
    

def save_trip(trip):  
    pass


def get_park_by_code(code):
    park = Park.get(Park.park_id == code)
    return park



"""Returns all saved trip objects"""
def get_all_trips():
    return Trip.select()


def delete_all_trips():
    Trip.delete().execute()


