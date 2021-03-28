import unittest 
from unittest import TestCase
from unittest.mock import patch
from peewee import Model, CharField, ForeignKeyField, DecimalField, BooleanField, Database, Check, IntegrityError, SqliteDatabase

from database.config import db_path
test_db_path = 'test_trips.db'
db_path = test_db_path

from database.model import Park, SavedTrip, Trip
from database import database

class TestDatabase(TestCase):


    def setUp(self):
        # Remove existing data from test database and recreate tables
        self.db = SqliteDatabase(db_path)
        self.db.drop_tables([Park, Trip, SavedTrip])
        self.db.create_tables([Park, Trip, SavedTrip])


    def addTestParkData(self):
        Park.create(park_id = "abcd", park_name = "park name 1", park_city = "park city 1", park_state = "park state 1", park_description = "park description 1",
                    latitude = 12.3456, longitude = 98.7654)
        Park.create(park_id = "dcba", park_name = "park name 2", park_city = "park city 2", park_state = "park state 2", park_description = "park description 2",
                    latitude = 12.3556, longitude = 98.7554)
        Park.create(park_id = "sdfs", park_name = "park name 3", park_city = "park city 3", park_state = "park state 1", park_description = "park description 3",
                    latitude = 12.3416, longitude = 98.7614)


    def addTestTripData(self):
        pass


    def test_save_parks_list(self):
        expected_parks_list = []
        park1 = Park(park_id = "abcd", park_name = "park name 1", park_city = "park city 1", park_state = "park state 1", park_description = "park description 1",
                    latitude = 12.3456, longitude = 98.7654)
        park2 = Park(park_id = "dcba", park_name = "park name 2", park_city = "park city 2", park_state = "park state 2", park_description = "park description 2",
                    latitude = 12.3556, longitude = 98.7554)
        park3 = Park(park_id = "sdfs", park_name = "park name 3", park_city = "park city 3", park_state = "park state 3", park_description = "park description 3",
                    latitude = 12.3416, longitude = 98.7614)
        expected_parks_list.append(park1)
        expected_parks_list.append(park2)
        expected_parks_list.append(park3)

        database.save_parks_list(expected_parks_list)
        parks = Park.select().execute()
        parks_list = []
        for p in parks:
            parks_list.append(p)
        self.assertEqual(expected_parks_list, parks_list)


    def test_get_parks_by_state(self):
        self.addTestParkData()
        parks_list = []
        parks = database.get_parks_by_state("park state 1")
        for p in parks:
            parks_list.append(p)
        self.assertEqual(len(parks_list), 2)


    def test_save_trip(self):
        park = Park.create(park_id = "abcd", park_name = "park name 1", park_city = "park city 1", park_state = "park state 1", park_description = "park description 1",
                    latitude = 12.3456, longitude = 98.7654)
        trip = SavedTrip(month = 5, park = park, image_1 = "lsdkfjd", image_2 = "kdldk", image_3 = "sldkfj", image_4 = "sldkdl", precipitation = 24, 
                    avg_temp = 12.3, max_temp = 56.9, min_temp = 0.45)
        database.save_trip(trip)
        database_trip = SavedTrip.get_or_none(SavedTrip.image_1 == "lsdkfjd")
        self.assertIsNotNone(database_trip)


    def test_save_duplicate_trip(self):
        park = Park.create(park_id = "abcd", park_name = "park name 1", park_city = "park city 1", park_state = "park state 1", park_description = "park description 1",
                    latitude = 12.3456, longitude = 98.7654)
        trip = Trip(month = 5, park = park, image_1 = "lsdkfjd", image_2 = "kdldk", image_3 = "sldkfj", image_4 = "sldkdl", precipitation = 24, 
                    avg_temp = 12.3, max_temp = 56.9, min_temp = 0.45)
        database.save_trip(trip)
        duplicate_trip = Trip(month = 5, park = park, image_1 = "lsdkfjd", image_2 = "kdldk", image_3 = "sldkfj", image_4 = "sldkdl", precipitation = 24, 
                    avg_temp = 12.3, max_temp = 56.9, min_temp = 0.45)
        database.save_trip(duplicate_trip)
        saved_trips = SavedTrip.select().execute()
        list_of_saved_trips = []
        for t in saved_trips:
            list_of_saved_trips.append(t)

        self.assertEqual(len(list_of_saved_trips), 1)


    def test_get_park_by_code(self):
        Park.create(park_id = "abcd", park_name = "park name 1", park_city = "park city 1", park_state = "park state 1", park_description = "park description 1",
                    latitude = 12.3456, longitude = 98.7654)
        park = database.get_park_by_code("abcd")
        self.assertIsNotNone(park)


    def test_convert_month(self):
        integer_month = 1
        expected_month = "JANUARY"
        actual_month = database._convert_month(integer_month)
        self.assertEqual(expected_month, actual_month)



