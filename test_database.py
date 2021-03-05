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


    def add_test_data(self):
        database.save_park('Yellowstone National Park', 'Middlanoware', 'WY', 'Beautiful scenic park.', 1234567.89, 9876543.21, 'image url 1', 'image url 2', 'image url 3')
        database.save_park('Yosemite', 'Somewhere', 'NA', 'Cool national park.', 1234567.890, 09876543.21, 'image url 1', 'image url 2', 'image url 3')
        database.save_park('Random Park', 'A City', 'SS', 'This is the park description.', 555555.55, 66666.66, 'image url 1', 'image url 2', 'image url 3')


    def test_save_park(self):
        database.save_park('Park Name', 'Park City', 'PS', 'Park Description', 65656556.0, 55555.000, 'image', 'image', 'image')
        park = database.get_park_by_name('Park Name')
        self.assertIsNotNone(park)
        

if __name__ == '__main__':
    unittest.main()        