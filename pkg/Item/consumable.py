from item import Item


class Consumable(Item):
    def __init__(self, x, y, char, color, name, volume, weight, flags=None, hp_mod=0, defense_mod=0, power_mod=0):
        Item.__init__(self, x, y, char, color, name, volume, weight, category="consumable", flags=flags)
        self.hp_mod = hp_mod
        self.defense_mod = defense_mod
        self.power_mod = power_mod
    
    def consume(self):
        self.owner.mod_hp(self.hp_mod)
        self.owner.mod_defense(self.defense_mod)
        self.owner.mod_power(self.power_mod)
