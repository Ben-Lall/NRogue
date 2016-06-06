from .. import entity


class Creature(entity.Entity):

    def __init__(self, x, y, char, color, name, stats, ai=None):
        entity.Entity.__init__(self, x, y, char, color, name, True)
        self.stats = stats
        self.ai = ai
        if self.ai is not None:
            self.ai.owner = self

