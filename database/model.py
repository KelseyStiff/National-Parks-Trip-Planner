from peewee import Model, CharField, Database, Check, SqliteDatabase, DecimalField, ForeignKeyField
from .config import db_path
import os

db = SqliteDatabase(db_path)

# The base model is used to link all subsequent models to the database
class BaseModel(Model):
    class Meta:
        database = db


class Park(BaseModel):
    park_id = CharField(primary_key=True, constraints=[Check('length(park_id) > 0'), Check('length(park_id) <= 20')])
    park_name = CharField(null=False, constraints=[Check('length(park_name) > 0'), Check('length(park_name) <= 30')]) 
    park_city = CharField(null=False, constraints=[Check('length(park_city) > 0'), Check('length(park_city) <= 30')])
    park_state = CharField(null=False, constraints=[Check('length(park_state) > 0'), Check('length(park_state) <= 30')]) 
    park_description = CharField(null=False, constraints=[Check('length(park_description) > 0'), Check('length(park_description) <= 200')])
    latitude = DecimalField(null=False, constraints=[Check('length(latitude) > 0'), Check('length(latitude) <= 30')])
    longitude = DecimalField(null=False, constraints=[Check('length(longitude) > 0'), Check('length(longitude) <= 30')])


    def __str__(self):
        return f"{self.park_id} {self.park_name} {self.park_city} {self.park_state} {self.park_description} {self.latitude} {self.longitude}"


    def dump(self):
        return {"park": {"id": self.park_id,
                          "name": self.park_name,
                          "city": self.park_city,
                          "state": self.park_state,
                          "description" : self.park_description,
                          "latitude" : self.latitude,
                          "longitude" : self.longitude
                          }}


class SavedTrip(BaseModel): # The user shouldn't be able to add the same SavedTrips twice 
    month = CharField(null = False)
    park = ForeignKeyField(Park, backref='parks')
    # image_1 = CharField(constraints=[Check('length(image_1) <= 100')])
    # image_2 = CharField(constraints=[Check('length(image_2) <= 100')])
    # image_3 = CharField(constraints=[Check('length(image_3) <= 100')])
    # image_4 = CharField(constraints=[Check('length(image_4) <= 100')])
    # precipitation = DecimalField()
    # avg_temp = DecimalField()
    # max_temp = DecimalField()
    # min_temp = DecimalField()

    # def __str__(self):
    #     return f"{self.park_name} {self.park_city} {self.park_state} {self.park_description} {self.latitude} {self.longitude} \
    #              {self.image_1} {self.image_2} {self.image_3} {self.image_4} {self.precipitation} {self.avg_temp} {self.max_temp} {self.min_temp}"

    def __str__(self):
        return f"{self.month} {self.park}"


    def dump(self):
        return {"park": {"month": self.month,
                          "park_id" : self.parks.park_id,
                          "park_name": self.parks.park_name,
                          "city": self.parks.park_city,
                          "state": self.parks.park_state,
                          "description" : self.parks.park_description,
                          "latitude" : self.parks.latitude,
                          "longitude" : self.parks.longitude
                        #   "image_1" : self.image_1,
                        #   "image_2" : self.image_2,
                        #   "image_3" : self.image_3,
                        #   "image_4" : self.image_4,
                        #   "precipiation" : self.precipitation,
                        #   "avg_temp" : self.avg_temp,
                        #   "max_temp" : self.max_temp,
                        #   "min_temp" : self.min_temp
                          }}


def create_db():
    db.connect()
    db.create_tables([Park, SavedTrip])
    