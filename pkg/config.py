import pkg.libtcodpy as libtcod
from pkg.Creatures import player as p

# Screen Dimensions
screen_width = 80
screen_height = 50

# Color Scheme
background_color = libtcod.white

# Console
con = libtcod.console_new(screen_width, screen_height)
game_state = 'playing'

# Player Init
player = p.Player(20, 20, '@', libtcod.white)

# Array of Entities
entities = [player]

#fov
fov_recompute = True




