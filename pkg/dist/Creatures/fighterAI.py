from .. import libtcodpy as libtcod
from .. import config as c

# AI for a basic monster.
class FighterAI:
    # To make warning go away
    def __init__(self):
        pass

    def take_turn(self):
        # Basic movement; moves towards you if it's within your fov
        monster = self.owner

        if libtcod.map_is_in_fov(c.fov_map, monster.x, monster.y):

            # If not in range, move towards the player
            if monster.distance_to(c.player) >= 2:
                monster.move_towards(c.player.x, c.player.y)

            # If it's close enough, and the player is still alive, it will attack

            elif c.player.stats.hp > 0:
                print 'you have been attacked by the ' + monster.name + '!'

