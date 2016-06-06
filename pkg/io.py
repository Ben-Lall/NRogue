import pkg.libtcodpy as libtcod
import pkg.config as c

# Pends for user keyboard input, then handles it accordingly
def handle_keys():
    key = libtcod.console_wait_for_keypress(True)

    # Alt + Enter: Toggle fullscreen
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    if key.vk == libtcod.KEY_ESCAPE:
        return 'exit'

    if c.game_state == 'playing':
        # Movement keys (Arrows)
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            c.player.move(0, -1, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            c.player.move(0, 1, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            c.player.move(-1, 0, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            c.player.move(1, 0, c.map)
            c.fov_recompute = True

        # Movement keys (NumPad Numbers)
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP1):
            c.player.move(-1, 1, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP2):
            c.player.move(0, 1, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP3):
            c.player.move(1, 1, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP4):
            c.player.move(-1, 0, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP5):
            return 'wait'
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP6):
            c.player.move(1, 0, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP7):
            c.player.move(-1, -1, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP8):
            c.player.move(0, -1, c.map)
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP9):
            c.player.move(1, -1, c.map)
            c.fov_recompute = True
        else:
            return 'noTurn'

