from model import Park
import peewee


def save_park(name, city, state, description, image1, image2, image3):
    park = Park(park_name = name, park_city = city, park_state = state, park_description = description, image_1 = image1, image_2 = image2, image_3 = image3)
    park.save()


def get_park(name):
    return Park.get(park_name = name)

    


