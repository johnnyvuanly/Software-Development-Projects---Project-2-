from model import Inventory
from peewee import fn

def delete_material(name):
    """ Removes material from inventory. Raises MaterialError if material is not in the inventory.
    :param material the Inventory to delete """

    rows_deleted = Inventory.delete().where(Inventory.name == name).execute()
    if not rows_deleted:
        raise MaterialError('Tried to delete book that does not exist')

def delete_all_material():
    """ Deletes all material from database """ 
    Inventory.delete().execute()

def get_material_by_id(material_id):
    """ Searches list for material with given ID,
    :param id the ID to search for
    :returns the material, if found, or None if material not found.
    """
    return Inventory.get_or_none(Inventory.id == material_id)

def exact_match(material):
    search = Inventory.get_or_none(Inventory.name == material.name)
    return search is not None
    
def material_search(term):
    """ Searches the inventory for material whose name contain a search term. Case insensative.
    Makes partial matches, so a search for 'ham' will match a material with the name 'Hammer'
    :param: term the search term
    :returns a list of materials that match the search term. The list will be empty if there are no matches.
    """
    query = Inventory.select().where( (fn.LOWER(Inventory.name).contains(term.lower() ) ) )
    return list(query)

def get_materials_by_availability(available):
    """ Get a list of materials that are available or list of materials that are not.
    :param available True to find all the materials that are available, False to find all the materials not available
    :returns all materials with available value.
    """
    query = Inventory.select().where(Inventory.available == available)
    return list(query)

def get_all_materials():
    """ :returns entire material list """
    query = Inventory.select()
    return list(query)

def material_count():
    """ :returns the number of materials in the store """
    return Inventory.select.count()

class MaterialError(Exception):
    """ For inventory errors. """
    pass