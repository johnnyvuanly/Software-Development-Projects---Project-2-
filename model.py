from peewee import *
from database_config import db_path

db = SqliteDatabase(db_path)

class Inventory(Model):
    name = CharField(null=False)
    cost = FloatField(null=False)
    stock = IntegerField(null=False)
    vendor = CharField(null=False)
    available = BooleanField(default=True)

    class Meta:
        database = db

    def __str__(self):
        availability_status = 'is' if self.available else 'is not'
        return f'This {availability_status} avaiable. There is {self.stock} left of {self.name} which costs {self.cost} and is purchased from {self.vendor}'

db.connect()
db.create_tables([Inventory])