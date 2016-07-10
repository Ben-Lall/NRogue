import pkg.config as c
from pkg.entity import Entity


##
# An item
# x: The item's x-coordinate
# y: The item's y-coordinate
# char: The item's representative character
# color: The item's color
# name: The item's name
# volume: The item's volume
# weight: The item's weight
# category: The category that the item falls in.  Used for sorting it properly in inventories.  Must exist in c.order
# token: Identifier used to quickly find this item when it's in an inventory.
#        is 0 when outside of an inventory, and is assigned some other value otherwise
# owner: The creature carrying this item
# flags: Flags that help define this item
class Item(Entity):
    def __init__(self, x, y, char, color, name, volume, weight, category="misc", token=0, owner=None, flags=None):
        Entity.__init__(self, x, y, char, color, name, False)
        # Ensure this Item has a valid x
        assert type(x) is int, "Violation of : x is not of type int for %r" % name

        # Ensure this Item has a valid y
        assert type(y) is int, "Violation of : y is not of type int for %r" % name

        # Ensure this Item has a valid char
        assert type(char) is str, "Violation of : char is not of type str for %r" % name

        # Ensure this Item has a valid name
        assert type(name) is str, "Violation of : name is not of type str for %r" % name

        # Ensure this Item has a valid volume
        assert type(volume) is float, "Violation of : volume is not of type float for %r" % name

        # Ensure this Item has a valid weight
        assert type(weight) is float, "Violation of : weight is not of type float for %r" % name

        # Ensure this Item has a valid category
        assert type(category) is str, "Violation of : category is not of type str for %r" % name
        assert c.order.__contains__(category), \
            "violation of : %r does not have a valid category: %r" % (name, category)

        # Ensure this Item has a valid token
        assert type(token) is int, "Violation of : token is not of type int for %r" % name

        # Ensure this Item has valid flags
        if flags is not None:
            assert type(flags) is list, "Violation of : flags is not of type list for %r, instead got %r"
            bad_flags = [x for x in flags if x not in c.item_flags]
            assert len(bad_flags) == 0, "Violation of : %r is/are a valid flag(s) for %r" % (bad_flags, self.name)

        self.volume = volume
        self.weight = weight
        self.category = category
        self.token = token
        self.owner = owner
        if flags is None:
            flags = []
        self.flags = flags
