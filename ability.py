import random
class Ability:
    def __init__(self, name, max_damage):
        # initialized values that will be passed when 
        # we call the class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_value = random.randint(0, self.max_damage)
        return random_value

# if __name__ == "__main__":
#     ability = Ability("Debugging Ability", 20)
#     print(ability.name)
#     print(ability.attack())