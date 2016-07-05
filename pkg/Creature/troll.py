from Creature import Creature
from StatSheet import StatSheet
from .. import libtcodpy as libtcod
from FighterAI import FighterAI


class Troll(Creature):
    def __init__(self, x, y,):
        stat_sheet = StatSheet(hp=15, defense=1, power=4)
        Creature.__init__(self, x, y, 't', libtcod.darker_green, 'Troll', stats=stat_sheet, ai=FighterAI())
