import pkg.libtcodpy as libtcod
import pkg.config as c
import pkg.tile as tile


def render_all():
    for entity in c.entities:
        entity.draw(c.con)

    for y in range(c.MAP_HEIGHT):
        for x in range(c.MAP_WIDTH):
            wall = c.map[x][y].blocked
            if wall:
                libtcod.console_set_char_background(c.con, x, y, c.color_dark_wall, libtcod.BKGND_SET)
            else:
                libtcod.console_set_char_background(c.con, x, y, c.color_dark_ground, libtcod.BKGND_SET)

    libtcod.console_blit(c.con, 0, 0, c.screen_width, c.screen_height, 0, 0, 0)


def make_map():
    c.map = [[tile.Tile(False)
               for y in range(c.MAP_HEIGHT) ]
                    for x in range(c.MAP_WIDTH) ]
    c.map[30][22].blocked = True
    c.map[30][22].block_sight = True
    c.map[50][22].blocked = True
    c.map[50][22].block_sight = True