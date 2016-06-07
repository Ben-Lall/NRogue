from .. import entity


class StatSheet(entity.Entity):

    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    # Modifies hp by the operator, making sure to keep within proper bounds, with the ability to overload if needed
    def mod_hp(self, operator, overload=False):

        # If current hp is beyond self.max_health, we don't want to accidentally reset to self.max_health
        if self.hp > self.max_hp:
            overload = True
        if operator >= 0:
            # Allows hp to transcend boundaries of self.max_health
            if overload:
                self.hp += operator
            else:
                self.hp = min(self.max_hp, self.hp + operator)
        else:
            self.hp = max(0, self.hp + operator)

        if self.hp == 0:
            self.owner.death_function()


    # Modifies power by the operator, making sure to not go below 0
    def mod_power(self, operator):
        self.power = max(0, self.power + operator)

    # Modifies defense by the operator, making sure to not go below 0
    def mod_defense(self, operator):
        self.defense = max(0, self.defense + operator)


