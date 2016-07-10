from creature import Creature
from statSheet import StatSheet
from .. import libtcodpy as libtcod
from .. import config as c
from .. import util


class Player(Creature):
    def __init__(self, x, y):
        stat_sheet = StatSheet(hp=30, defense=2, power=5, max_volume=10, max_carry_weight=100)
        Creature.__init__(self, x, y, '@', libtcod.white, c.player_name, stats=stat_sheet,
                          death_function=self.player_death)

    def move(self, dx, dy):
        x = self.x + dx
        y = self.y + dy

        # Find if this coordinate has a creature to attack
        target = None
        for entity in c.entities:
            if entity.x == x and entity.y == y and hasattr(entity, 'ai') and entity.ai is not None:
                target = entity
                break

        # If there is something to attack, then attack it
        if target is not None:
            c.player.basic_attack(target)
            c.player_action = 'attacking'

        # Otherwise, move
        elif not util.is_blocked(x, y):
            self.x = x
            self.y = y

    def player_death(self):
        util.message('You have died!', libtcod.dark_red)
        c.game_state = 'dead'

        self.color = libtcod.dark_red
