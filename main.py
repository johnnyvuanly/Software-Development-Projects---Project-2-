""" Program to track the inventory for Concrete Craft """
import peewee
from model import Inventory
import db
import ui

def main():
    print_menu()
    user_input = 0

    """ While  the user enters a valid menu option menu is shown -
    menu set up mostly from https://chunkofcode.net/how-to-implement-a-dynamic-command-line-menu-in-python/"""

    while user_input != 6:
        user_input = int(input('Enter Choice: '))

        if user_input == 1:
            add_material()
        elif user_input == 2:
            show_all_material()
        elif user_input == 3:
            show_available_material()
        elif user_input == 4:
            delete_material()
        elif user_input == 5:
            change_availability()
        
        elif user_input == 7:
            break
        print_menu()

def print_menu():
    print('*Concrete Craft Inventory Tracker*')
    print('1. Add material')
    print('2. Display all material in inventory')
    print('3. Display all available material in the inventory')
    print('4. Delete material')
    print('5. Change material Availability')
    print('6. Exit')
    print('*Concrete Craft Inventory Tracker*')

def add_material():
    new_material = ui.get_material_info()
    try:
        new_material.save()
    except peewee.IntegrityError:
        ui.message('Error, material already exist in the database')

def show_all_material():
    search_term = ui.ask_question('Enter name of material to view information on it: ')
    matches = db.material_search(search_term)
    ui.show_material(matches)

def show_available_material():
    available_material = db.get_materials_by_availability()
    ui.show_material()

def delete_material():
    material_to_delete = ui.ask_question('Enter name of the material to delete: ')
    db.delete_material(material_to_delete)

def change_availability():
    material_id = ui.get_material_id()
    item_name = db.get_material_by_id(material_id)
    if not item_name:
        ui.message('Material not found')
        return
    new_status = ui.get_availability()
    item_name.query = new_status
    item_name.save()

if __name__ == '__main__':
    main() # don't forget to call main
