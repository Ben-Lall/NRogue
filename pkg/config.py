import pkg.libtcodpy as libtcod
from pkg.Creatures import player as p

# Screen Dimensions
screen_width = 80
screen_height = 50

# Color Scheme
background_color = libtcod.white
color_dark_wall = libtcod.Color(65, 45, 10)
color_light_wall = libtcod.Color(100, 70, 10)
color_dark_ground = libtcod.Color(22, 22, 22)
color_light_ground = libtcod.Color(40, 40, 40)

# Console
con = libtcod.console_new(screen_width, screen_height)
game_state = 'playing'

# Player Init
player = p.Player(20, 20, '@', libtcod.white)

# Array of Entities
entities = [player]

# Map Parameters
MAP_WIDTH = 80
MAP_HEIGHT = 45
map = []

# Parameters for FOV
FOV_ALGORITHM = 0
fov_recompute = True




