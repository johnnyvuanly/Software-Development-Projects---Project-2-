from peewee import *
from model import Inventory

def add_material(inventory):
    print(inventory)
    inventory.save()

