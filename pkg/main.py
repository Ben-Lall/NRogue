import io
import pkg.libtcodpy as libtcod
import pkg.config as c
import pkg.builder as builder

# Game Window Setup
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(c.screen_width, c.screen_height, 'NRogue', False)
libtcod.console_set_default_background(0, c.background_color)

# Generate Map
builder.make_map()

while not libtcod.console_is_window_closed():
    # Display console

    builder.render_all()

    libtcod.console_flush()

    for entity in c.entities:
        entity.clear(c.con)

    io.handle_keys()