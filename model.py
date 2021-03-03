from peewee import *
from database_config import db_path

db = SqliteDatabase(db_path)

class Inventory(Model):
    material = CharField
    cost = CharField
    stock = IntegerField
    vendor = CharField 
    available = BooleanField(default=True)

    class Meta:
        database = db

    def __str__(self):
        availability_status = 'is' if self.available else 'is not'
        return f'This {availability_status} avaiable. There is {self.stock} left of {self.material} which costs {self.cost} and is purchased from {self.vendor}'

db.connect()
db.create_tables([Inventory])