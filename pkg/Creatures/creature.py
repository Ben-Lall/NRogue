from .. import entity
from .. import libtcodpy as libtcod
from .. import config as c
import math


class Creature(entity.Entity):
    def __init__(self, x, y, char, color, name, stats, ai=None, death_function=None):
        entity.Entity.__init__(self, x, y, char, color, name, True)

        # Set up statsheet
        self.stats = stats
        self.stats.owner = self

        # Set up ai
        self.ai = ai
        if self.ai is not None:
            self.ai.owner = self

        # Set up death_function
        self.death_function = death_function
        if self.death_function is None:
            self.death_function = ai.death_function

    def move_towards(self, tar_x, tar_y):
        # Get distance
        dx = tar_x - self.x
        dy = tar_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Normalize to length 1
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy)

    def move_astar(self, target):
        # Create a FOV map that has the dimensions of the map
        fov = libtcod.map_new(c.MAP_WIDTH, c.MAP_HEIGHT)

        # Scan the current map each turn and set all the walls as unwalkable
        for y1 in range(c.MAP_HEIGHT):
            for x1 in range(c.MAP_WIDTH):
                libtcod.map_set_properties(fov, x1, y1, not c.map[x1][y1].block_sight, not c.map[x1][y1].blocked)

        # Scan all the objects to see if there are objects that must be navigated around
        # Check also that the object isn't self or the target (so that the start and the end points are free)
        # The AI class handles the situation if self is next to the target so it will not use this A* function anyway
        for obj in c.entities:
            if obj.blocks and obj != self and obj != target:
                # Set the tile as a wall so it must be navigated around
                libtcod.map_set_properties(fov, obj.x, obj.y, True, False)

        # Allocate a A* path
        # The 1.41 is the normal diagonal cost of moving, it can be set as 0.0 if diagonal moves are prohibited
        my_path = libtcod.path_new_using_map(fov, 1.41)

        # Compute the path between self's coordinates and the target's coordinates
        libtcod.path_compute(my_path, self.x, self.y, target.x, target.y)

        # Check if the path exists, and in this case, also the path is shorter than 25 tiles
        # The path size matters if you want the monster to use alternative longer paths (for example through other rooms) if for example the player is in a corridor
        # It makes sense to keep path size relatively low to keep the monsters from running around the map if there's an alternative path really far away
        if not libtcod.path_is_empty(my_path) and libtcod.path_size(my_path) < 25:
            # Find the next coordinates in the computed full path
            x, y = libtcod.path_walk(my_path, True)
            if x or y:
                # Set self's coordinates to the next path tile
                self.x = x
                self.y = y
        else:
            # Keep the old move function as a backup so that if there are no paths (for example another monster blocks a corridor)
            # it will still try to move towards the player (closer to the corridor opening)
            self.move_towards(target.x, target.y)

            # Delete the path to free memory
        libtcod.path_delete(my_path)

    def basic_attack(self, target):
        damage = max(0, self.stats.power - target.stats.defense)

        if damage > 0:
            print self.name + ' attacks ' + target.name + ' for ' + str(damage) + ' hit points.'
            target.stats.mod_hp(-1 * damage)
        else:
            print self.name + ' attacks ' + target

