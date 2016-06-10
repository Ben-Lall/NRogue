from .. import libtcodpy as libtcod
from .. import config as c
from .. import util


# AI for a basic monster.
class FighterAI:
    def __init__(self):
        self.destination_x = None
        self.destination_y = None

    def take_turn(self):
        # Basic movement; moves towards the last place it saw you
        monster = self.owner

        # If the monster sees the player, then it should make its destination the player's tile
        if libtcod.map_is_in_fov(c.fov_map, monster.x, monster.y):
            self.destination_x = c.player.x
            self.destination_y = c.player.y
            print (self.owner.name + ' has begun its pursuit of ' + c.player.name)

        # If the monster has arrived at its destination and doesn't see the player, it gives up
        elif self.destination_x == self.owner.x and self.destination_y == self.owner.y:
            self.destination_x = None
            self.destination_y = None
            print (self.owner.name + ' has lost sight of ' + c.player.name)

        # If the monster has a destination, it should...
        if self.destination_x and self.destination_y:
            # Move towards it if it's far away
            if monster.distance_to(target=c.player) >= 2:
                monster.move_astar(tar_x=self.destination_x, tar_y=self.destination_y)

            # Attack it if it's close
            elif c.player.hp() > 0:
                monster.basic_attack(c.player)

    def death_function(self):
        monster = self.owner
        util.message('The ' + monster.name + ' has died!')
        monster.move_to_bottom()
        monster.color = libtcod.dark_red
        monster.blocks = False
        monster.ai = None
        monster.name = 'remains of ' + monster.name

