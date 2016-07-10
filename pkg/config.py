import pkg.libtcodpy as libtcod

# Debug
DEBUG = False

# FPS
fps_limit = 10

# Screen Dimensions
screen_width = 192
screen_height = 100

# Color Scheme
background_color = libtcod.white
color_dark_wall = libtcod.Color(65, 45, 10)
color_light_wall = libtcod.Color(100, 70, 10)
color_dark_ground = libtcod.Color(22, 22, 22)
color_light_ground = libtcod.Color(40, 40, 40)
color_mouse_over = libtcod.Color(255, 80, 80)
color_unexplored = libtcod.black

# Console
con = libtcod.console_new(screen_width, screen_height)
game_state = 'playing'

# Player Init
player = None
player_name = 'Player'
player_action = ''

#  Entities init
entities = []
entity_names = set()
entity_memory_radius = 20

# Items init
items = []
order = ["weapon", "ammo", "consumable", "armor", "misc"]
item_flags = ["heals"]

# Map Parameters
map_width = int((3.0/4) * screen_width)
map_height = screen_height
map = []

# Mapgen Parameters
rooms = []
max_room_monsters = 3
# Likely will not be used in the future, but for now...
room_max_size = 10
room_min_size = 6
max_rooms = 30

# Parameters for FOV
fov_algorithm = 0
fov_light_walls = True
torch_radius = 10
fov_map = libtcod.map_new(map_width, map_height)
fov_recompute = True

# Initialize information panel
panel_height = screen_height
panel_width = map_width / 3
panel = libtcod.console_new(panel_width, panel_height)
hp_bar_width = 19
hp_bar_x = 0
hp_bar_y = 1
panel_y = 0
panel_x = map_width
msg_x = 0
msg_y = hp_bar_y + 2
msg_width = panel_width
msg_height = panel_height - 1 - hp_bar_y
msg_buffer = []

# Initialize mouse over panel

