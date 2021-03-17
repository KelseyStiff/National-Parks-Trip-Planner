import unittest 
from unittest import TestCase
from unittest.mock import patch
from peewee import Model, CharField, ForeignKeyField, DecimalField, BooleanField, Database, Check, IntegrityError, SqliteDatabase

import config
db_path = 'test_parks.db'
config.db_path = db_path

from model import Trip
import database 


class TestParksDB(TestCase):

    def setUp(self):
        # Remove existing data from test database and recreate tables
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Trip])
        self.db.create_tables([Trip])

# TODO don't call save_park - instead add data manually
    def add_sample_data(self):
        database.save_trip('Yellowstone National Park', 'Middlanoware', 'Wyoming', 'Beautiful scenic park.', 1234567.89, 9876543.21, 'image url 1', 'image url 2', 'image url 3')
        database.save_trip('Yosemite', 'Somewhere', 'Nevada', 'Cool national park.', 1234567.890, 09876543.21, 'image url 1', 'image url 2', 'image url 3')
        database.save_trip('Random Park', 'A City', 'Somewherolina', 'This is the park description.', 555555.55, 66666.66, 'image url 1', 'image url 2', 'image url 3')


    def test_save_trip(self):
        database.save_trip('Park Name', 'Park City', 'Parksylvania', 'Park Description', 65656556.0, 55555.000, 'image', 'image', 'image')
        trip = Trip.get_or_none(park_name = 'Park Name')
        self.assertIsNotNone(trip)  
        trip = Trip.get_or_none(park_name = 'NAME THAT DOES NOT EXIST') 
        self.assertIsNone(trip)


    def test_get_trip_by_park_name(self):
        self.add_sample_data()
        trip = database.get_trip_by_park_name('Yosemite')
        expected = ['Yosemite', 'Somewhere', 'Nevada', 'Cool national park.', 1234567.890, 
                     09876543.21, 'image url 1', 'image url 2', 'image url 3']
        actual = [trip.park_name, trip.park_city, trip.park_state, trip.park_description, float(trip.latitude), 
                  float(trip.longitude), trip.image_1, trip.image_2, trip.image_3]
        self.assertEqual(actual, expected)

    
    def test_get_all_trips(self):
        self.add_sample_data()
        trips = database.get_all_trips()
        expected_names = ['Yellowstone National Park', 'Yosemite', 'Random Park']
        actual_names = []
        for park in trips:
            actual_names.append(park.park_name)
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


    def test_get_all_trips_coordinates(self):
        self.add_sample_data()
        actual_coordinates = database.get_all_trips_coordinates()
        expected_coordinates = {1234567.89 : 9876543.21, 1234567.890 : 09876543.21, 555555.55 : 66666.66}
        self.assertEqual(actual_coordinates, expected_coordinates)


    def test_delete_all_trips(self):
        self.add_sample_data()
        database.delete_all_trips()
        for trip in Trip.select().execute():
            self.assertIsNone(trip)


    def test_delete_trip_by_park_name(self):
        self.add_sample_data()
        database.delete_trip_by_park_name('Yosemite')
        trip = Trip.get_or_none(park_name = 'Yosemite')
        self.assertIsNone(trip)


if __name__ == '__main__':
    unittest.main()        