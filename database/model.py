from peewee import Model, CharField, Database, Check, SqliteDatabase, DecimalField, ForeignKeyField, AutoField
from .config import db_path
import os
from apis.conversion_dicts import months_string, months_int

db = SqliteDatabase(db_path)

# The base model is used to link all subsequent models to the database
class BaseModel(Model):
    class Meta:
        database = db


class Park(BaseModel):
    park_id = CharField(unique=True, constraints=[Check('length(park_id) <= 500')])
    park_name = CharField(null=False, constraints=[Check('length(park_name) <= 500')]) 
    park_city = CharField(null=False, constraints=[Check('length(park_city) <= 500')])
    park_state = CharField(null=False, constraints=[Check('length(park_state) <= 500')]) 
    park_description = CharField(null=False, constraints=[Check('length(park_description) <= 1000')])
    latitude = DecimalField(null=False, constraints=[Check('length(latitude) <= 500')])
    longitude = DecimalField(null=False, constraints=[Check('length(longitude) <= 500')])


    def __str__(self):
        return f"{self.park_id} {self.park_name} {self.park_city} {self.park_state} {self.park_description} {self.latitude} {self.longitude}"


    def dump(self):
        return {"park": {"id": self.park_id,
                          "name": self.park_name,
                          "city": self.park_city,
                          "state": self.park_state,
                          "description" : self.park_description,
                          "latitude" : float(self.latitude),
                          "longitude" : float(self.longitude)
                          }}


class Trip(BaseModel): # The user shouldn't be able to add the same Trips twice 
    month = CharField(null = False)
    park = ForeignKeyField(Park, backref='parks')
    image_1 = CharField()
    image_2 = CharField()
    image_3 = CharField()
    image_4 = CharField()
    precipitation = DecimalField()
    avg_temp = DecimalField()
    max_temp = DecimalField()
    min_temp = DecimalField()

    def __str__(self):
        return f"{self.month} {self.park} {self.image_1} {self.image_2} {self.image_3} {self.image_4} \
                 {self.precipitation} {self.avg_temp} {self.max_temp} {self.min_temp}"


    def dump(self):
        return {"park": {
                          "trip_id" : self.id,
                          "month": self.month,
                          "park_id" : self.park.park_id,
                          "park_name": self.park.park_name,
                          "city": self.park.park_city,
                          "state": self.park.park_state,
                          "description" : self.park.park_description,
                          "latitude" : float(self.park.latitude),
                          "longitude" : float(self.park.longitude),
                          "image_1" : self.image_1,
                          "image_2" : self.image_2,
                          "image_3" : self.image_3,
                          "image_4" : self.image_4,
                          "precipiation" : float(self.precipitation),
                          "avg_temp" : float(self.avg_temp),
                          "max_temp" : float(self.max_temp),
                          "min_temp" : float(self.min_temp)
                          }}


    def __eq__(self, other):
        return (self.park == other.park) & (int(months_int[self.month.upper()]) == int(other.month))


    def __ne__(self, other):
        return not self.__eq__(other)


class SavedTrip(Trip):
    pass

    




def create_db():
    db.connect()
    db.create_tables([Park, Trip, SavedTrip])
    