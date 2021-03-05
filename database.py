from model import Park
import model
import peewee


def save_park(name, city, state, description, latitude, longitude, image1, image2, image3):  
    park = Park(
        park_name = name, park_city = city, park_state = state, 
        park_description = description, latitude = latitude, 
        longitude = longitude, image_1 = image1, image_2 = image2, 
        image_3 = image3
        )
    park.save()


def get_park_by_name(park_name):
    return Park.get(park_name = park_name)


def get_all_parks():
    parks = Park.select()
    return parks


def get_park_city(park_name):
    park = get_park_by_name(park_name)
    city = park.park_city
    return city






#model.create_db()
#save_park('test park', 'Minneapolis', 'MN', 'a test park', 123.45, 6345.3, 'sldkfjsdl', 'sldkfslfj', 'sldkjsldkf')

