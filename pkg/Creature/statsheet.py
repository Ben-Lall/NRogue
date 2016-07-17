from .. import entity
from .. import config as c
import collections


class StatSheet(entity.Entity):

    def __init__(self, hp, defense, power, volume=0.0, max_volume=10.0, carry_weight=0.0, max_carry_weight=100.0):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.volume = volume
        self.max_volume = max_volume
        self.carry_weight = carry_weight
        self.max_carry_weight = max_carry_weight

        self.inventory = []
        for category in c.order:
            self.inventory.append(collections.OrderedDict())

    # Modifies hp by the operator, making sure to keep within proper bounds, with the ability to overload if needed
    def mod_hp(self, operator, overload=False):

        # If current hp is beyond self.max_health, we don't want to accidentally reset to self.max_health
        if self.hp > self.max_hp:
            overload = True
        if operator >= 0:
            # Allows hp to transcend boundaries of self.max_health
            if overload:
                self.hp += operator
            else:
                self.hp = min(self.max_hp, self.hp + operator)
        else:
            self.hp = max(0, self.hp + operator)

        if self.hp == 0:
            self.owner.death_function()

    # Modifies power by the operator, making sure to not go below 0
    def mod_power(self, operator):
        self.power = max(0, self.power + operator)

    # Modifies defense by the operator, making sure to not go below 0
    def mod_defense(self, operator):
        self.defense = max(0, self.defense + operator)

    # Modifies volume by the operator, making sure to not go below 0
    def mod_volume(self, operator):
        self.volume = max(0, self.volume + operator)

    # Modifies max volume by the operator, making sure to not go below 0
    def mod_max_volume(self, operator):
        self.max_volume = max(0, self.max_volume + operator)

    # Modifies carry weight by the operator, making sure to not go below 0
    def mod_carry_weight(self, operator):
        self.carry_weight = max(0, self.carry_weight + operator)

    # Modifies carry weight by the operator, making sure to not go below 0
    def mod_carry_max_weight(self, operator):
        self.max_carry_weight = max(0, self.max_carry_weight + operator)

    # Add the item to the inventory, keeping it sorted and giving it a token for identification
    # Requires self.volume + item.volume <= self.max_volume
    def add_to_inventory(self, item):

        # Current category being examined
        cat_index = 0

        # Iterate through the inventory rows at a time
        for category in c.order:
            cat_len = len(self.inventory[cat_index])
            # If the current row is the correct row, or the item has already been added, then items will need
            # their tokens incremented
            if category == item.category:
                i = 0
                # Iterate through this row until either an item that comes lexicographically after the item to be
                # added appears, or the end of the row is reached.  This will give the index where the item will
                # be added
                while i < cat_len and self.inventory[cat_index][i].name < item.name:
                    i += 1
                # Set up the item to be added
                item.owner = self
                self.carry_weight += item.weight
                self.volume += item.volume
                c.entities.remove(item)
                c.items.remove(item)

                # If the item is already in the inventory, increment its total
                if i < cat_index and item == self.inventory[cat_index][i]:
                    val = self.inventory[cat_index][item] + 1
                    self.inventory[cat_index][item] = val
                # Otherwise add a new element in the dictionary to represent it
                else:
                    self.inventory[cat_index][item] = 1
                    sorted(self.inventory[cat_index], key=lambda t: t[0])

            cat_index += 1

    # Remove from the inventory the item with the matching token, placing it somewhere on the map if necessary
    # Requires: 0 < selector <= |self.inventory|
    # Returns: the item removed
    def remove_from_inventory(self, selector, x=None, y=None):
        assert type(selector) is int
        if x and y:
            assert type(x) is int and type(y) is int

        # Current category being examined
        cat_index = 0
        # Tally of the amount of items being considered
        counter = 0
        # The item removed
        removed_item = None

        # Iterate through inventory rows at a time.
        for category in c.order:
            for item in self.inventory[cat_index]:
                counter += 1

                if counter == selector:
                    remove_item, amt = self.inventory[cat_index][selector].items()[0]

                    if amt == 1:
                        del self.inventory[cat_index][selector]
                    else:
                        self.inventory[cat_index][removed_item] = amt - 1

                    if x and y:
                        removed_item.x = x
                        removed_item.y = y
                        c.items.append(removed_item)
                        c.entities.insert(0, removed_item)
                    removed_item.owner = None
                    self.volume -= removed_item.volume
                    self.carry_weight -= removed_item.weight
            cat_index += 1
        return removed_item
