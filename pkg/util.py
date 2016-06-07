import libtcodpy as libtcod
import config as c
import textwrap


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


# Writes a message to the game console
def message(msg, color=libtcod.white):

    msg_lines = textwrap.wrap(msg, c.msg_width)

    for line in msg_lines:
        # If the buffer is full, delete the topmost entry
        if len(c.msg_buffer) == c.msg_height:
            del c.msg_buffer[0]

        c.msg_buffer.append((line, color))
