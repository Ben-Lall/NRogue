import config as c
import libtcodpy as libtcod

# Game Window Setup
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE)
libtcod.console_init_root(c.screen_height, c.screen_width, 'NRogue', False)
libtcod.console_set_default_background(0, c.background_color)

while not libtcod.console_is_window_closed():
    # Display console
    libtcod.console_blit(c.con, 0, 0, c.screen_width, c.screen_height, 0, 0, 0)
