class Tile:

    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked

        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked
        self.block_sight = block_sight

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
