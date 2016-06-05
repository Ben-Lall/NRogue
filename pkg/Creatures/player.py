from .. import entity

class Player(entity.Entity):

    def __init__(self, x, y, char, color, blocks = True):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.blocks = blocks