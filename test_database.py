import unittest 
from unittest import TestCase
from unittest.mock import patch
from peewee import Model, CharField, ForeignKeyField, DecimalField, BooleanField, Database, Check, IntegrityError, SqliteDatabase

import config
db_path = 'test_parks.db'
config.db_path = db_path

from model import Park
import database 


class TestParksDB(TestCase):

    def setUp(self):
        # Remove existing data from test database and recreate tables
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Park])
        self.db.create_tables([Park])


    def add_sample_data(self):
        database.save_park('Yellowstone National Park', 'Middlanoware', 'WY', 'Beautiful scenic park.', 1234567.89, 9876543.21, 'image url 1', 'image url 2', 'image url 3')
        database.save_park('Yosemite', 'Somewhere', 'NA', 'Cool national park.', 1234567.890, 09876543.21, 'image url 1', 'image url 2', 'image url 3')
        database.save_park('Random Park', 'A City', 'SS', 'This is the park description.', 555555.55, 66666.66, 'image url 1', 'image url 2', 'image url 3')


    def test_save_park(self):
        database.save_park('Park Name', 'Park City', 'PS', 'Park Description', 65656556.0, 55555.000, 'image', 'image', 'image')
        park = Park.get_or_none(park_name = 'Park Name')
        self.assertIsNotNone(park)
        
        park = Park.get_or_none(park_name = 'NAME THAT DOES NOT EXIST') 
        self.assertIsNone(park)


    def test_get_park_by_name(self):
        self.add_sample_data()
        park = database.get_park_by_name('Yosemite')
        expected = ['Yosemite', 'Somewhere', 'NA', 'Cool national park.', 1234567.890, 
                     09876543.21, 'image url 1', 'image url 2', 'image url 3']
        actual = [park.park_name, park.park_city, park.park_state, park.park_description, float(park.latitude), 
                  float(park.longitude), park.image_1, park.image_2, park.image_3]
        self.assertEqual(actual, expected)

    
    def test_get_all_parks(self):
        self.add_sample_data()
        parks = database.get_all_parks()
        expected_names = ['Yellowstone National Park', 'Yosemite', 'Random Park']
        actual_names = []
        for p in parks:
            actual_names.append(p.park_name)
        self.assertEqual(expected_names, actual_names)


    def test_get_park_city(self):
        self.add_sample_data()
        actual_city = database.get_park_city('Yosemite')
        expected_city = 'Somewhere'
        self.assertEqual(actual_city, expected_city)


    def test_get_park_latitude_by_name(self):
        self.add_sample_data()
        actual_latitude = database.get_park_latitude_by_name('Yosemite')
        expected_latitude = 1234567.890
        self.assertEqual(actual_latitude, expected_latitude)


    def test_get_park_longitude_by_name(self):
        self.add_sample_data()
        actual_longitude = database.get_park_longitude_by_name('Yosemite')
        expected_longitude = 09876543.21
        self.assertEqual(actual_longitude, expected_longitude)


    def test_get_all_parks_coordinates(self):
        self.add_sample_data()
        actual_coordinates = database.get_all_parks_coordinates()
        expected_coordinates = {1234567.89 : 9876543.21, 1234567.890 : 09876543.21, 555555.55 : 66666.66}
        self.assertEqual(actual_coordinates, expected_coordinates)


    def test_delete_all_parks(self):
        self.add_sample_data()
        database.delete_all_parks()
        for p in Park.select().execute():
            self.assertIsNone(p)


    def test_delete_park_by_name(self):
        self.add_sample_data()
        database.delete_park_by_name('Yosemite')
        park = Park.get_or_none(park_name = 'Yosemite')
        self.assertIsNone(park)


if __name__ == '__main__':
    unittest.main()        