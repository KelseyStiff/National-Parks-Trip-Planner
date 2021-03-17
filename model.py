from peewee import Model, CharField, Database, Check, SqliteDatabase, DecimalField
from config import db_path
import os

db = SqliteDatabase(db_path)

# The base model is used to link all subsequent models to the database
class BaseModel(Model):
    class Meta:
        database = db


class Trip(BaseModel): # The user shouldn't be able to add the same Trip twice 
    park_name = CharField(null=False, constraints=[Check('length(park_name) > 0'), Check('length(park_name) <= 30')]) 
    park_city = CharField(null=False, constraints=[Check('length(park_city) > 0'), Check('length(park_city) <= 30')])
    park_state = CharField(null=False, constraints=[Check('length(park_state) > 0'), Check('length(park_state) <= 30')]) 
    park_description = CharField(null=False, constraints=[Check('length(park_description) > 0'), Check('length(park_description) <= 200')])
    latitude = DecimalField(null=False, constraints=[Check('length(latitude) > 0'), Check('length(latitude) <= 30')])
    longitude = DecimalField(null=False, constraints=[Check('length(longitude) > 0'), Check('length(longitude) <= 30')])
    image_1 = CharField(constraints=[Check('length(image_1) <= 100')])
    image_2 = CharField(constraints=[Check('length(image_2) <= 100')])
    image_3 = CharField(constraints=[Check('length(image_3) <= 100')])
    precipitation = DecimalField()
    avg_temp = DecimalField()
    max_temp = DecimalField()
    min_temp = DecimalField()


    def __str__(self):
        return "Name: {0:30} City: {1:20} State: {2:20} Description: {3:40}".format(self.park_name,self.park_city,self.park_state,self.park_description)


def create_db():
    db.create_tables([Trip])