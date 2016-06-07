from .. import entity
import math


class Creature(entity.Entity):
    def __init__(self, x, y, char, color, name, stats, ai=None):
        entity.Entity.__init__(self, x, y, char, color, name, True)
        self.stats = stats
        self.ai = ai
        if self.ai is not None:
            self.ai.owner = self

    def move_towards(self, tar_x, tar_y):
        # Get distance
        dx = tar_x - self.x
        dy = tar_y - self.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        # Normalize to length 1
        dx = int(round(dx / distance))
        dy = int(round(dy / distance))
        self.move(dx, dy)

