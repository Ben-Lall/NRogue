import pkg.libtcodpy as libtcod

# Debug
DEBUG = False

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
player = None
player_name = 'Player'

#  Entities init
entities = []
entity_names = set()
entity_memory_radius = 20

# Map Parameters
MAP_WIDTH = 80
MAP_HEIGHT = 43
map = []

# Mapgen Parameters
rooms = []
MAX_ROOM_MONSTERS = 3
# Likely will not be used in the future, but for now...
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS = 30

# Parameters for FOV
FOV_ALGORITHM = 0
FOV_LIGHT_WALLS = True
torch_radius = 10
fov_map = libtcod.map_new(MAP_WIDTH, MAP_HEIGHT)
fov_recompute = True

# Initialize information panel
panel_height = screen_height / 4
panel = libtcod.console_new(screen_width, panel_height)
panel_height = 7
hp_bar_width = 20
hp_bar_x = 1
hp_bar_y = 1
panel_y = screen_height - panel_height
msg_x = hp_bar_width + hp_bar_x + 1
msg_width = screen_width - hp_bar_x - msg_x
msg_height = panel_height - 1
msg_buffer = []
