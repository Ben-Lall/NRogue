import libtcodpy as libtcod
import config as c
import textwrap


# Return a list containing the names of all objects under the player's mouse
def get_names_under_mouse(mouse):
    (x, y) = (mouse.cx, mouse.cy)
    # Create a list of all entities in the player's FOV
    names = [entity.name for entity in c.entities if entity.x == x and entity.y == y and
             libtcod.map_is_in_fov(c.fov_map, entity.x, entity.y)]

    return names


# Given a number and string word, determines if the string needs pluralization, then
# goes through
def pluralize(num, word):
    if num != 1:
        pluralization = word
        if word == 'point':
            pluralization = 'points'
        else:
            print "pluralization for " + word + " not found."
        return pluralization
    else:
        return word


def is_blocked(x, y):
    # first test the map tile
    if c.map[x][y].blocked:
        return True

    # now check for any blocking objects
    for entity in c.entities:
        if entity.blocks and entity.x == x and entity.y == y:
            return True

    return False


# Render a bar meter
def render_bar(con, x, y, total_width, name, value, maximum, bar_color, back_color):
    bar_width = int(float(value) / maximum * total_width)

    # Bar background
    libtcod.console_set_default_background(con, back_color)
    libtcod.console_rect(con, x, y, total_width, 1, False, libtcod.BKGND_SCREEN)

    # Bar foreground
    libtcod.console_set_default_background(con, bar_color)
    if bar_width > 0:
        libtcod.console_rect(con, x, y, bar_width, 1, False, libtcod.BKGND_SCREEN)

    # Text Overlay
    libtcod.console_set_default_foreground(con, libtcod.white)
    libtcod.console_print_ex(con, x + total_width / 2, y, libtcod.BKGND_NONE, libtcod.CENTER,
                             name + ': ' + str(value) + '/' + str(maximum))


# Adds the message along with its color to the message buffer
def message(msg, color=libtcod.white):

    msg_lines = textwrap.wrap(msg, c.msg_width)

    for line in msg_lines:
        # If the buffer is full, delete the topmost entry
        if len(c.msg_buffer) == c.msg_height:
            del c.msg_buffer[0]

        c.msg_buffer.append((line, color))
    return c.msg_buffer


# Returns true if target is within a range defined by a circle around source with a given radius
def is_in_radius(target, source, radius):
    return (target.x - source.x) ** 2 + (target.y - source.y) ** 2 <= radius


