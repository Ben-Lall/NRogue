import pkg.libtcodpy as libtcod
import pkg.config as c


# Pends for user keyboard input, then handles it accordingly
def handle_keys():
    key = libtcod.console_wait_for_keypress(True)
    move_key_pressed = False
    pre_coordinates = (c.player.x, c.player.y)

    # Initialize c.player_action
    c.player_action = ''

    # Alt + Enter: Toggle fullscreen
    if key.vk == libtcod.KEY_ENTER and (key.lalt or key.ralt):
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    if key.vk == libtcod.KEY_ESCAPE:
        c.player_action = 'exit'

    if c.game_state == 'playing' and c.player_action != 'exit':
        # Movement keys (Arrows)
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            c.player.move(0, -1)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            c.player.move(0, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            c.player.move(-1, 0)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            c.player.move(1, 0)
            move_key_pressed = True
            c.fov_recompute = True

        # Movement keys (Keypad Numbers)
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP1):
            c.player.move(-1, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP2):
            c.player.move(0, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP3):
            c.player.move(1, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP4):
            c.player.move(-1, 0)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP5):
            c.fov_recompute = True
            c.player_action = 'wait'
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP6):
            c.player.move(1, 0)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP7):
            c.player.move(-1, -1)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP8):
            c.player.move(0, -1)
            move_key_pressed = True
            c.fov_recompute = True
        elif libtcod.console_is_key_pressed(libtcod.KEY_KP9):
            c.player.move(1, -1)
            move_key_pressed = True
            c.fov_recompute = True

        # wait
        elif libtcod.console_is_key_pressed(libtcod.KEY_KPDEC) or key.c == 46:
            c.player_action = 'wait'
        else:
            c.player_action = 'noTurn'

        # Determine if the player has taken a turn
        if c.player_action != 'attacking' and move_key_pressed and pre_coordinates == (c.player.x, c.player.y):
            c.player_action = 'noTurn'
