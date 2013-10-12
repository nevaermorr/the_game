from engine.gear import *
from controller.inventory import *


class Inventory(Gear):
    """
    set of items connected with some entity or place
    """

    def __init__(self, owner):
        Gear.__init__(self)
        # list of items present in the inventory
        self.items_ = []
        # remember owner of this inventory
        self.owner = owner
        # assign switch
        self.switch = InventorySwitch(self)

    def add(self, *items_):
        """
        put something into the inventory
        """
        self.items_.extend(items_)

    def remove(self, *items_):
        """
        remove something from the inventory
        """
        # delete items from inventory through list comprehension
        self.items_ = [item for item in self.items_ if not item in items_]

    def choose_all(self, condition=False):
        """
        get from the inventory all items that meet certain condition
        """
        # by default, get all the items
        if not condition:
            return self.items_

    def is_empty(self):
        """
        check if inventory is empty
        """
        return not bool(self.items_)

    def get_items(self):
        """
        obtain all items from inventory
        """
        return self.items_


class InventoryInterface:
    """
    interface for all classes containing some inventory
    """

    def __init__(self):
        # inventory is obligatory
        self.inventory = Inventory(self)

    def get_inventory(self):
        """
        grant access to the inventory
        """
        return self.inventory

    def get_items_from(self, inventory):
        """
        choose and obtain items from an inventory
        """
        # by default choose all possible items
        items_ = inventory.choose_all()
        # remove all the items from original inventory (in order to avoid duplication)
        inventory.remove(*items_)
        return items_

    def add_items(self, *items_):
        """
        shortcut for adding items to inventory
        """
        self.inventory.add(*items_)

    def has_empty_inventory(self):
        """
        is the inventory of this object empty?
        """
        return self.inventory.is_empty()

    def show_inventory(self):
        """
        request inspection of the inventory
        """
        self.inventory.get_switch().call_display_items()
