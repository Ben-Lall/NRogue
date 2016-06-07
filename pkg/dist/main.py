import pkg.IO as io
import pkg.libtcodpy as libtcod
import pkg.config as c
import pkg.builder as builder

# Game Window Setup
libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(c.screen_width, c.screen_height, 'NRogue', False)
libtcod.console_set_default_background(0, c.background_color)

# Generate Map
builder.make_map()

# Initialize FOV map
for y in range(c.MAP_HEIGHT):
    for x in range(c.MAP_WIDTH):
        libtcod.map_set_properties(c.fov_map, x, y, not c.map[x][y].block_sight, not c.map[x][y].blocked)

while not libtcod.console_is_window_closed():
    # Recompute FOV if needed (the player moved or something)
    if c.fov_recompute:
        fov_recompute = False
        libtcod.map_compute_fov(c.fov_map, c.player.x, c.player.y, c.torch_radius, c.FOV_LIGHT_WALLS, c.FOV_ALGORITHM)

    # Renderer
    builder.render_all()
    libtcod.console_flush()
    for entity in c.entities:
        entity.clear(c.con)

    # Pend for player input
    player_action = io.handle_keys()
    if player_action == 'exit':
        break

    # Simulate turns
    if c.game_state == 'playing' and player_action != 'noTurn':
        for entity in c.entities:
            if entity != c.player and libtcod.map_is_in_fov(c.fov_map, entity.x, entity.y):
                entity.ai.take_turn()
