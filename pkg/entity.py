import math
import pkg.libtcodpy as libtcod
import pkg.config as c
import util as util


class Entity:

    def __init__(self, x, y, char, color, name, blocks=True):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks
        c.entity_names.add(name)

    def draw(self, con):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self, con):
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)

    def move(self, dx, dy):
        if not util.is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    # Return the distance to another object or coordinate pair
    def distance_to(self, target=None, x=None, y=None):
        # Must pass in either an entity or coordinate pair
        assert isinstance(target, Entity) or (type(x) is int and type(y) is int)
        if target:
            dx = target.x - self.x
            dy = target.y - self.y
        else:
            dx = x - self.x
            dy = y - self.y
        print(self.name + ': | my_x: ' + str(self.x) + ' | my_y: ' + str(self.y))
        print('dx: ' + str(dx) + ' | tar_x: ' + str(x) + ' | player_x: ' + str(c.player.x))
        print('dy: ' + str(dy) + ' | tar_y: ' + str(y) + ' | player_y: ' + str(c.player.y))
        print(str(math.sqrt(dx ** 2 + dy ** 2)))
        return math.sqrt(dx ** 2 + dy ** 2)

    # Move this entity to the front of the array, so that it is drawn first and is overwritten by other draw calls
    def move_to_bottom(self):
        c.entities.remove(self)
        c.entities.insert(0, self)
