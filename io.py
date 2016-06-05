import libtcodpy as libtcod
import config as c

def handle_keys():
    # Blocking Call for Keypress
    key = libtcod.console_wait_for_keypress(True)

    # Movement keys (Arrows)
    if key.vk == libtcod.KEY_UP:
        c.player.move(0, -1)
    elif key.vk == libtcod.KEY_DOWN:
        c.player.move(0, 1)
    elif key.vk == libtcod.KEY_RIGHT:
        c.player.move(1, 0)
    elif key.vk == libtcod.KEY_LEFT:
        c.player.move(-1, 0)

    # Movement keys (NumPad)
    elif key.vk == libtcod.KEY_KP1:
        c.player.move(-1, 1)
    elif key.vk == libtcod.KEY_KP2:
        c.player.move(0, 1)
    elif key.vk == libtcod.KEY_KP3:
        c.player.move(1, 1)
    elif key.vk == libtcod.KEY_KP4:
        c.player.move(-1, 0)
    elif key.vk == libtcod.KEY_KP5:
        # Replace
        c.player.move(0, 0)
    elif key.vk == libtcod.KEY_KP6:
        c.player.move(1, 0)
    elif key.vk == libtcod.KEY_KP7:
        c.player.move(-1, -1)
    elif key.vk == libtcod.KEY_KP8:
        c.player.move(0, -1)
    elif key.vk == libtcod.KEY_KP9:
        c.player.move(1, -1)

