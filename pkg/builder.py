import pkg.libtcodpy as libtcod
import pkg.config as c
import pkg.tile as tile
import pkg.entity as entity
import pkg.util as util
from Creature.player import Player
from Creature.orc import Orc
from Creature.troll import Troll
from LesserHealingPotion import LesserHealingPotion


# a rectangle of tiles
class Rect:
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.x2 = x + w
        self.y1 = y
        self.y2 = y + h
        # (x1, y1) is the top left corner, (x2, y2) is the bottom right

    # Return the center point of self
    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return center_x, center_y

    # Return True if self and other overlap
    def intersect(self, other):
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    # Return a random set of coordinates in self
    def get_random_coordinates(self):
        x = libtcod.random_get_int(0, self.x1 + 1, self.x2 - 1)
        y = libtcod.random_get_int(0, self.y1 + 1, self.y2 - 1)
        return x, y


# Renders all entities and tiles in range of the player
def render_all(mouse):
    for entity in c.entities:
        if c.DEBUG or libtcod.map_is_in_fov(c.fov_map, entity.x, entity.y):
            entity.draw(c.con)

    # Set colors of all the map's tiles
    for y in range(c.map_height):
        for x in range(c.map_width):
            if c.DEBUG:
                visible = True
            else:
                visible = libtcod.map_is_in_fov(c.fov_map, x, y)
            wall = c.map[x][y].blocked
            if (x, y) == (mouse.cx, mouse.cy):
                libtcod.console_set_char_background(c.con, mouse.cx, mouse.cy, c.color_mouse_over +
                                                    libtcod.console_get_char_background(c.con, x, y))
            elif visible:
                if wall:
                    libtcod.console_set_char_background(c.con, x, y, c.color_light_wall, libtcod.BKGND_SET)
                else:
                    libtcod.console_set_char_background(c.con, x, y, c.color_light_ground, libtcod.BKGND_SET)
                c.map[x][y].explored = True
            else:
                if c.map[x][y].explored:
                    if wall:
                        libtcod.console_set_char_background(c.con, x, y, c.color_dark_wall, libtcod.BKGND_SET)
                    else:
                        libtcod.console_set_char_background(c.con, x, y, c.color_dark_ground, libtcod.BKGND_SET)
                else:
                    libtcod.console_set_char_background(c.con, x, y, c.color_unexplored, libtcod.BKGND_SET)

    libtcod.console_blit(c.con, 0, 0, c.screen_width, c.screen_height, 0, 0, 0)

    # Show GUI containing player's stats
    libtcod.console_set_default_background(c.panel, libtcod.black)
    libtcod.console_clear(c.panel)

    # Update hp bar
    util.render_bar(c.panel, c.hp_bar_x, c.hp_bar_y, c.hp_bar_width, 'HP', c.player.hp(), c.player.max_hp(),
                    libtcod.darker_red, libtcod.darkest_red)

    # Print line by line the game messages
    y = c.msg_y
    for (line, color) in c.msg_buffer:
        words = line.split(' ')
        current_line_length = 0
        for word in words:
            current_color = color
            if word == c.player.name:
                current_color = libtcod.purple
            elif c.entity_names.__contains__(word):
                current_color = libtcod.dark_red
            libtcod.console_set_default_foreground(c.panel, current_color)
            libtcod.console_print_ex(c.panel, c.msg_x + current_line_length, y, libtcod.BKGND_NONE, libtcod.LEFT, word)
            current_line_length += len(word) + 1
        y += 1

    # List the objects at the player's cursor
    libtcod.console_set_default_foreground(c.panel, libtcod.light_gray)
    names_list = util.get_names_under_mouse(mouse)
    names = str(names_list)
    names = names[2:-2]  # Formatting

    if len(names_list) > 1:
        # Because of the way things are rendered, the last element of this list is always the object on top
        names = names_list[-1] + " and " + str(len(names_list) - 1) + " more"

    libtcod.console_print_ex(c.panel, 1, 0, libtcod.BKGND_NONE, libtcod.LEFT, names)

    # Blit info panel to console
    libtcod.console_blit(c.panel, 0, 0, c.screen_width, c.panel_height, 0, c.panel_x, c.panel_y)


# Creates a vertical tunnel of unblocked tiles
def create_v_tunnel(y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
        c.map[x][y].set_unblocked()


# Creates a horizontal tunnel of unblocked tiles
def create_h_tunnel(x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        c.map[x][y].set_unblocked()


# Go through the tiles in the rectangle and make them passable
def create_room(room):
    for x in range(room.x1 + 1, room.x2):
        for y in range(room.y1 + 1, room.y2):
            c.map[x][y].set_unblocked()


# Places creatures in the room at position x,y where c.map[x][y].blocked = False
def place_creatures(room):
    num_monsters = libtcod.random_get_int(0, 0, c.max_room_monsters)

    for i in range(num_monsters):

        x, y = room.get_random_coordinates()

        while util.is_blocked(x, y):
            x, y = room.get_random_coordinates()

        if libtcod.random_get_int(0, 0, 100) > 80:
            monster = Troll(x, y)
        else:
            monster = Orc(x, y)

        c.entities.append(monster)


def place_items(room):
    num_items = libtcod.random_get_int(0, 0, 2)

    for i in range(num_items):
        item = None

        x, y = room.get_random_coordinates()

        while util.is_blocked(x, y):
            x, y = room.get_random_coordinates()

        if libtcod.random_get_int(0, 0, 100) > 0:
            item = LesserHealingPotion(x, y)

        if item is not None:
            c.entities.insert(0, item)
            c.items.append(item)


# Temporary map generator
def make_map():
    # Set each tile as impassable, so we can "carve" out level geometry
    c.map = [[tile.Tile(True)
               for y in range(c.map_height)]
                    for x in range(c.map_width)]

    for r in range(c.max_rooms):
        # Random width and height
        w = libtcod.random_get_int(0, c.room_min_size, c.room_max_size)
        h = libtcod.random_get_int(0, c.room_min_size, c.room_max_size)
        # Random position within map boundaries
        x = libtcod.random_get_int(0, 0, c.map_width - w - 1)
        y = libtcod.random_get_int(0, 0, c.map_height - h - 1)

        # Generate Rect
        new_room = Rect(x, y, w, h)

        # Determine if new_room intersects with any existing rooms
        failed = False
        for room in c.rooms:
            if new_room.intersect(room):
                failed = True
                break

        # If this room does not intersect
        if not failed:
            # Create room
            create_room(new_room)

            # Store center coordinates of new_room
            (new_x, new_y) = new_room.center()

            if c.DEBUG:
                room_no = entity.Entity(new_x, new_y, chr(65 + len(c.rooms)), libtcod.white, 'room-number', blocks=False)
                c.entities.insert(0, room_no)

            # If this is the first room to be generated, generate and place the player in the center
            if len(c.rooms) == 0:
                c.player = Player(20, 20)
                c.entities.append(c.player)
                c.player.x = new_x
                c.player.y = new_y
            else:
                # Connect the previous room to the new one using tunnels

                # Get the center of the previous room
                num_rooms = len(c.rooms)
                (prev_x, prev_y) = c.rooms[num_rooms - 1].center()

                # Flip a coin, if heads, draw horizontal tunnel then vertical tunnel, if tails the opposite
                if libtcod.random_get_int(0, 0, 1) == 1:
                    create_h_tunnel(prev_x, new_x, prev_y)
                    create_v_tunnel(prev_y, new_y, new_x)
                else:
                    create_v_tunnel(prev_y, new_y, new_x)
                    create_h_tunnel(prev_x, new_x, prev_y)

            # Place monsters and items (but not in the player's starting room)
            if len(c.rooms) > 1:
                place_creatures(new_room)
                place_items(new_room)

            # Append new_room to list of rooms
            c.rooms.append(new_room)


