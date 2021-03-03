from peewee import Model, CharField, Database, Check, SqliteDatabase
from config import db_path
import os

db = SqliteDatabase(db_path)

# The base model is used to link all subsequent models to the database
class BaseModel(Model):
    class Meta:
        database = db


class Park(BaseModel):
    park_name = CharField(null=False)
    park_city = CharField(null=False)
    park_state = CharField(null=False)
    park_description = CharField(null=False)
    image_1 = CharField(null=False)
    image_2 = CharField(null=False)
    image_3 = CharField(null=False)



    def __str__(self):
        return(f'Name: {self.park_name} City: {self.park_city} State: {self.park_state} Description: {self.park_description}')

