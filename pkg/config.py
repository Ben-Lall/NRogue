import pkg.libtcodpy as libtcod
from pkg.Creatures import player as p

# Debug
DEBUG = True

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

# Mapgen Parameters
rooms = []
# Likely will not be used in the future, but for now...
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

# Parameters for FOV
FOV_ALGORITHM = 0
fov_recompute = True





