from consumable import Consumable
import pkg.libtcodpy as libtcod


class LesserHealingPotion(Consumable):
    def __init__(self, x, y):
        Consumable.__init__(self, x, y, 'u', libtcod.lighter_red, 'Lesser Healing Potion', 0.2, 1.5, flags=['heals'], hp_mod=5)


