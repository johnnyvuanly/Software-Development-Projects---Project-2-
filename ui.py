from model import Inventory

def get_material_info():
    """ Get material name, cost per item, stock, which vendor was used to push the item
    returns material name, cost, stock, and place of purchase base off of user input"""
    name = input('Enter the name of the item to add to the database: ')
    cost = float(input('Enter the amount of the item per unit: $'))
    stock = int(input('Enter how much of the material you have left, per unit: '))
    vender = input('Enter the name of the vendor used to purchase the item: ')
    available = (input('Enter yes or no if the item is available: ')).lower()
    if available == "yes":
        available == True
    else:
        available == False
    return Inventory(name=name, cost=cost, stock=stock, vendor=vender, available=available)

def show_material(materials_list):
    """ Display all of the materials in a list or 'No materials in inventory' message """
    if materials_list:
        for items in materials_list:
            print(items)
        else:
            print('No items in the material inventory')

def get_material_id():
    """ Allows the user to search the name of the material by id and returns the row data. """
    while True:
        try:
            id = int(input('Enter Material ID: '))
            if id > 0:
                return id
            else:
                print('Please enter a positive number.')

        except ValueError:
            print('Please enter a number.')

def get_availability():
    """ Ask user to enter 'is' or 'is not' 
    :returns: True if user enters 'is' or False if user enters 'is not' """
    while True:
        response = input('Enter \'is\' if the material is available or \'is not\' if the material is not available: ')
        if response.lower() in ['is not', 'is']:
            return response.lower() == 'is'
        else:
            print('Type \'is\' or \'is not\'')

def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)

def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)