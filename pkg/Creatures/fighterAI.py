from .. import libtcodpy as libtcod
from .. import config as c
from .. import util


# AI for a basic monster.
class FighterAI:
    def __init__(self):
        pass

    def take_turn(self):
        # Basic movement; moves towards you if it's within your fov
        monster = self.owner

        if libtcod.map_is_in_fov(c.fov_map, monster.x, monster.y):

            # If not in range, move towards the player
            if monster.distance_to(c.player) >= 2:
                monster.move_astar(c.player)

            # If it's close enough, and the player is still alive, it will attack

            elif c.player.stats.hp > 0:
                monster.basic_attack(c.player)

    def death_function(self):
        monster = self.owner
        util.message('The ' + monster.name + ' has died!')
        monster.move_to_bottom()
        monster.color = libtcod.dark_red
        monster.blocks = False
        monster.ai = None
        monster.name = 'remains of ' + monster.name

