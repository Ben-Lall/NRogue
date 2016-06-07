import math
import pkg.libtcodpy as libtcod
import pkg.config as c


class Entity:

    def __init__(self, x, y, char, color, name, blocks = True):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks

    def draw(self, con):
        libtcod.console_set_default_foreground(con, self.color)
        libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)

    def clear(self, con):
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)

    def move(self, dx, dy):
        if not c.is_blocked(self.x + dx, self.y + dy):
            self.x += dx
            self.y += dy

    def distance_to(self, other):
        # Return the distance to another object
        dx = other.x - self.x
        dy = other.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)