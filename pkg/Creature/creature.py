from .. import entity
from .. import libtcodpy as libtcod
from .. import config as c
from .. import util
import math


class Creature(entity.Entity):
    def __init__(self, x, y, char, color, name, stats, ai=None, death_function=None, inventory=()):
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

        self.inventory = inventory

    def hp(self):
        return self.stats.hp

    def max_hp(self):
        return self.stats.max_hp

    def power(self):
        return self.stats.power

    def defense(self):
        return self.stats.defense

    def volume(self):
        return self.stats.volume

    def max_volume(self):
        return self.stats.mod_max_volume

    def carry_weight(self):
        return self.stats.carry_weight

    def max_carry_weight(self):
        return self.stats.max_carry_weight

    def mod_hp(self, operator, overload=False):
        assert type(operator) is int
        self.stats.mod_hp(operator, overload)

    def mod_power(self, operator):
        assert type(operator) is int
        self.stats.mod_power(operator)

    def mod_defense(self, operator):
        assert type(operator) is int
        self.stats.mod_defense(operator)

    def mod_volume(self, operator):
        assert type(operator) is int
        self.stats.mod_volume(operator)

    def mod_max_volume(self, operator):
        assert type(operator) is int
        self.stats.mod_max_volume(operator)

    def mod_carry_weight(self, operator):
        assert type(operator) is int
        self.stats.mod_carry_weight(operator)

    def mod_max_carry_weight(self, operator):
        assert type(operator) is int
        self.stats.mod_max_carry_weight(operator)

    def add_to_inventory(self, item):
        self.stats.add_to_inventory(item)

    def move_towards(self, tar_x, tar_y):
        assert type(tar_x) is int and type(tar_y) is int

        # Get distance
        dx = tar_x - self.x
        dy = tar_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Normalize to length 1
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy)

    def move_astar(self, target=None, tar_x=None, tar_y=None):
        if target:
            tar_x = target.x
            tar_y = target.y
        else:
            for entity in c.entities:
                if entity.x == tar_x and entity.y == tar_y:
                    target = entity
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
        path = libtcod.path_new_using_map(fov, 1.41)
        # Compute the path between self's coordinates and the target's coordinates
        libtcod.path_compute(path, self.x, self.y, tar_x, tar_y)

        # Check if the path exists, and in this case, also the path is shorter than 25 tiles
        # The path size matters if you want the monster to use alternative longer paths (for example through other rooms) if for example the player is in a corridor
        # It makes sense to keep path size relatively low to keep the monsters from running around the map if there's an alternative path really far away
        if not libtcod.path_is_empty(path) and libtcod.path_size(path) < 25:
            # Find the next coordinates in the computed full path
            x, y = libtcod.path_walk(path, True)
            if x or y:
                # Set self's coordinates to the next path tile
                self.x = x
                self.y = y
        else:
            # Keep the old move function as a backup so that if there are no paths (for example another monster blocks a corridor)
            # it will still try to move towards the player (closer to the corridor opening)
            self.move_towards(tar_x, tar_y)

            # Delete the path to free memory
        libtcod.path_delete(path)

    def basic_attack(self, target):
        assert isinstance(target, Creature)

        damage = max(0, self.power() - target.defense())
        util.message('The ' + self.name + ' attacks the ' + target.name + ' for ' + str(damage) + ' hit ' +
                      util.pluralize(damage, "point") + '.')
        target.mod_hp(-1 * damage)

    # Pick up the item at the given coordinates and place it into inventory, if it's possible
    # Requires: self != Player => self.volume + item.volume <= self.max_volume
    def pick_up(self, target_x, target_y):
        assert type(target_x) is int and type(target_y) is int

        for item in c.items:
            if item.x == target_x and item.y == target_y:
                if self.volume() + item.volume <= self.max_volume():
                    self.add_to_inventory(item)
                    util.message(self.name + ' picks up a ' + item.name)

                else:
                    util.message('You do not have enough inventory space to pick that up!')

    # Use the item pertaining to the given token
    # Requires token <= |self.stats.inventory|
    def use_item(self, token):
        assert type(token) is int

        used_item = self.stats.remove_from_inventory(token)
        used_item.owner = self

        used_item.consume()
        util.message('You use the ' + used_item.name)

        used_item.owner = None



