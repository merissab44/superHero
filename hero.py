import random
from ability import Ability
from armor import Armor
class Hero:
    # We want out hero to have a default "starting health"
    # we set that in the finction header
    def __init__(self, name, starting_health=100):
        # abilities and armors dont have starting values
        self.abilities = list()
        self.armors = list()
        #name of our hero
        self.name = name
        #when we create hero, their starting health
        #is there current health
        self.starting_health = starting_health
        # when a hero is created the current health
        # us the same as their starting health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            # add the damage of the attack to get the total damage
            total_damage += ability.attack()
            print(f" the total damage was: {total_damage}")
            return total_damage
    
    def add_armor(self, armor):
        # adding each armor to the list self.armors
        self.armors.append(armor)

    def defend(self, damage_amt):
        damage_amt = self.attack()
        total_block = 0
        block = 0
        for armor in self.armors:
            # adds the "strength" of the armor to get the total block
            block += armor.block()
            return block
        print(damage_amt)
        print(block)
        total_block = damage_amt - block
        print(f"Your total block is {total_block}")
        return total_block
    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        print(f"Your current health is now {self.current_health}")
        return self.current_health
    def is_alive(self):
        if self.current_health <= 0:
            print(" hero has fallen over ")
            return False
        else:
            return True

    def fight(self, opponent):
        hero_choice = [self.name, opponent.name]
        print(f"{random.choice(hero_choice)} won!")

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())