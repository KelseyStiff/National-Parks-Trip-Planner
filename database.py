from model import Park
import model
import peewee


"""
Accepts all values for a park object and saves it to the database. All parameters are required except images.
Some park names may not pull up enough pictures.
"""
def save_park(name, city, state, description, latitude, longitude, image1=None, image2=None, image3=None):  
    park = Park(
        park_name = name, park_city = city, park_state = state, 
        park_description = description, latitude = latitude, 
        longitude = longitude, image_1 = image1, image_2 = image2, 
        image_3 = image3
        )
    park.save()


def get_park_by_name(park_name):
    return Park.get(park_name = park_name)


"""Returns all saved park objects"""
def get_all_parks():
    parks = Park.select()
    return parks


def get_park_city(park_name):
    park = get_park_by_name(park_name)
    city = park.park_city
    return city


def get_park_latitude_by_name(park_name):
    park = get_park_by_name(park_name)
    return park.latitude


def get_park_longitude_by_name(park_name):
    park = get_park_by_name(park_name)
    return park.longitude
    

"""Returns a dictionary containing the float coordinates of all saved parks"""
def get_all_parks_coordinates(): #
    parks = get_all_parks()
    coordinates = {}
    for p in parks:
        coordinates.update({float(p.latitude) : float(p.longitude)}) 
    return coordinates



# save_park('Yellowstone National Park', 'Middlanoware', 'Wyoming', 'Beautiful scenic park.', 1234567.89, 9876543.21, 'sldksjdlf', 'sdlkjsdfl', 'sldkjsldkfd')
# save_park('Yosemite', 'Somewhere', 'Nevada', 'Cool national park.', 1234567.890, 09876543.21, 'sldksjdl', 'sdlkjsdf', 'sldkjsldkf')
# save_park('Random Park', 'A City', 'Some State', 'This is the park description.', 555555.55, 66666.66, 'asdfsdfs', 'sdfdfsdsfdaf', 'sdfsdfadfasdf')

print(get_all_parks_coordinates())