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
        if word == "point":
            pluralization = "points"
        else:
            print "pluralization for %s not found." % word
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


def index_to_token(selector):
    if type(selector) is str:
        index = ord(selector)
    else:
        index = selector
    token = -1

    if 97 <= index <= 126:
        token = index - 96
    elif 65 <= index <= 90:
        token = index - 38
    elif 48 <= index <= 64:
        token = index + 5
    elif 33 <= index <= 47:
        token = index + 37

    return token


def token_to_index(token):
    selector = '  '
    if 1 <= token <= 26:
        selector = chr(token + 96) + ':'
    elif 27 <= token <= 52:
        selector = chr(token + 38) + ':'
    elif 53 <= token <= 69:
        selector = chr(token - 5) + ':'
    elif 70 <= token <= 84:
        selector = chr(token - 37) + ':'

    return selector


def display_inventory(source):
    # Set up indent space and header
    indent_space = '    '
    header = 'Inventory vol: %s/%s weight:%s/%s' % (str(source.volume()), str(source.max_volume()),
                                                    str(source.carry_weight()), str(source.max_carry_weight()))
    header_height = libtcod.console_get_height_rect(c.con, 0, 0, c.screen_width, c.screen_height, header)
    height = source.inventory_size() + header_height + len(c.order) + 1
    width = 50

    inventory_window = libtcod.console_new(width, height)
    libtcod.console_set_default_foreground(inventory_window, libtcod.white)
    libtcod.console_print_rect_ex(inventory_window, 0, 0, width, height, libtcod.BKGND_NONE, libtcod.LEFT,
                                  header)
    libtcod.console_hline(inventory_window, 0, header_height, width)

    y = header_height + 1
    category_index = 0
    inventory = source.stats.inventory
    selector_val = 1

    for category in inventory:
        if len(inventory[category_index]) > 0:
            libtcod.console_print_ex(inventory_window, 0, y, libtcod.BKGND_NONE, libtcod.LEFT, c.order[category_index])
            y += 1
        for item in inventory[category_index]:
            current_item, amount = item.items()[0]

            name = item.name
            if amount > 1:
                name += " (%s)" % str(amount)

            selector = token_to_index(selector_val)
            option = '%s%s%s' % (selector, indent_space, name)
            libtcod.console_print_ex(inventory_window, 2, y, libtcod.BKGND_NONE, libtcod.LEFT, option)

            y += 1
            selector_val += 1
            
        category_index += 1

    xdst = int((1.0 / 10) * c.screen_width)
    ydst = int((1.0 / 20) * c.screen_height)

    libtcod.console_blit(inventory_window, 0, 0, c.screen_width, c.screen_height, 0, xdst, ydst, 1.0, 0.7)
    libtcod.console_flush()
