from Creature import Creature
from StatSheet import StatSheet
from .. import libtcodpy as libtcod
from FighterAI import FighterAI


class Orc(Creature):
    def __init__(self, x, y,):
        stat_sheet = StatSheet(hp=10, defense=0, power=3)
        Creature.__init__(self, x, y, 'o', libtcod.light_green, name='Orc', stats=stat_sheet, ai=FighterAI())
