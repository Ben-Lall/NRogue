import pkg.config as c


# A tile
class Tile:

    def __init__(self, blocked, block_sight=None, color=c.color_unexplored):
        self.blocked = blocked

        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight
        self.color = color

        # By default, tiles start unexplored
        self.explored = False

    # Set blocked and block_sight to false
    def set_unblocked(self):
        self.blocked = False
        self.block_sight = False

    # Set blocked and block_sight to false
    def set_blocked(self):
        self.blocked = True
        self.block_sight = True
