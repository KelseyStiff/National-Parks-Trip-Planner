from peewee import Model, CharField, Database, Check, SqliteDatabase, DecimalField
from config import db_path
import os

db = SqliteDatabase(db_path)

# The base model is used to link all subsequent models to the database
class BaseModel(Model):
    class Meta:
        database = db


class Park(BaseModel):
    park_name = CharField(null=False, unique=True) # The user shouldn't be able to add the same park twice
    park_city = CharField(null=False)
    park_state = CharField(null=False)
    park_description = CharField(null=False)
    latitude = DecimalField(null=False)
    longitude = DecimalField(null=False)
    image_1 = CharField(null=False)
    image_2 = CharField(null=False)
    image_3 = CharField(null=False)



    def __str__(self):
        return "Name: {0:30} City: {0:20} State: {0:20} Description: {0:40}".format(self.park_name,self.park_city,self.park_state,self.park_description)


def create_db():
    db.create_tables([Park])