import random
class Hero:
    # We want out hero to have a default "starting health"
    # we set that in the finction header
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        # when a hero is created the current health
        # us the same as their starting health
        self.current_health = starting_health

    def fight(self, opponent):
        hero_choice = [self.name, opponent.name]
        print(f"{random.choice(hero_choice)} won!")
if __name__ == "__main__":
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbeldore")

  print(hero1.fight(hero2))