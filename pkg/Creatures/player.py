from creature import Creature
from statsheet import StatSheet
from .. import libtcodpy as libtcod
from .. import config as c


class Player(Creature):

    def __init__(self, x, y):
        stat_sheet = StatSheet(hp=30, defense=2, power=5)
        Creature.__init__(self, x, y, '@', libtcod.white, c.player_name, True, stat_sheet)
