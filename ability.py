import random
class Ability:
    def __init__(self, name, max_damage):
        # initialized values that will be passed when 
        # we call the class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, int(self.max_damage))
        return random_value
