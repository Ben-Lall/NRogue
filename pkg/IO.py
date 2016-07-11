import pkg.libtcodpy as libtcod
import pkg.config as c
import pkg.util as util


# Handles user's mouse and keyboard input
def handle_input(key=c.key, mouse=c.mouse):

    move_key_pressed = False
    pre_coordinates = (c.player.x, c.player.y)

    # Initialize c.player_action
    c.player_action = ''

    # Alt + Enter: Toggle fullscreen
    if libtcod.console_is_key_pressed(libtcod.KEY_ENTER) and (key.lalt or key.ralt):
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    if libtcod.console_is_key_pressed(libtcod.KEY_ESCAPE) and (key.lalt or key.ralt):
        c.player_action = 'exit'

    if c.game_state == 'playing' and c.player_action != 'exit':
        # Movement keys (Arrows)
        if key.vk == libtcod.KEY_UP:
            c.player.move(0, -1)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_DOWN:
            c.player.move(0, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_LEFT:
            c.player.move(-1, 0)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_RIGHT:
            c.player.move(1, 0)
            move_key_pressed = True
            c.fov_recompute = True

        # Movement keys (Keypad Numbers)
        elif key.vk == libtcod.KEY_KP1:
            c.player.move(-1, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_KP2:
            c.player.move(0, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_KP3:
            c.player.move(1, 1)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_KP4:
            c.player.move(-1, 0)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_KP5:
            c.fov_recompute = True
            c.player_action = 'wait'
        elif key.vk == libtcod.KEY_KP6:
            c.player.move(1, 0)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_KP7:
            c.player.move(-1, -1)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_KP8:
            c.player.move(0, -1)
            move_key_pressed = True
            c.fov_recompute = True
        elif key.vk == libtcod.KEY_KP9:
            c.player.move(1, -1)
            move_key_pressed = True
            c.fov_recompute = True

        # wait
        elif key.vk == libtcod.KEY_KPDEC:
            c.player_action = 'wait'

        # Handle character keypress cases
        elif key.vk == libtcod.KEY_CHAR:
            key_char = chr(key.c)

            if key_char == '.':
                c.player_action = 'wait'
            elif key_char == 'g':
                c.player.pick_up(c.player.x, c.player.y)
            elif key_char == 'i':
                c.game_state = 'menu'

                util.display_inventory(c.player)
                libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, c.key, c.mouse, True)
                handle_input()

        # default case
        else:
            c.player_action = 'noTurn'

        # Determine if the player has taken a turn
        if c.player_action != 'attacking' and move_key_pressed and pre_coordinates == (c.player.x, c.player.y):
            c.player_action = 'noTurn'

    elif c.game_state == 'menu' and c.player_action != 'exit':
        if libtcod.console_is_key_pressed(libtcod.KEY_ESCAPE):
            c.game_state = 'playing'

        elif key.vk == libtcod.KEY_CHAR:
            token = util.index_to_token(key.c)
            if token != -1 and token <= c.player.inventory_size():
                c.player.use_item(token)
                c.game_state = 'playing'
            else:
                # present the root console to the player and wait for a key-press
                libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, c.key, c.mouse, True)
                handle_input()
        else:
            # present the root console to the player and wait for a key-press
            libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, c.key, c.mouse, True)
            handle_input()











