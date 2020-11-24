import random
from ability import Ability
from armor import Armor
from weapon import Weapon
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
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
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

    def defend(self):
        total_block = 0
        if len(self.armors) == 0:
            print('Theres no armor')
            return 0
        for armor in self.armors:
            # adds the "strength" of the armor to get the total block
            print(f"name: {armor.name}")
            total_block += armor.block()
        print(f"Your total block is {total_block}")
        return total_block
    def take_damage(self, damage):
        print(damage)
        print(self.defend())
        self.current_health -= damage + self.defend()
        print(f"Your current health is now {self.current_health}")
        return self.current_health
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths
    def fight(self, opponent):
        #Check to see if hero has abilities, if no abilities, print draw
        if len(self.abilities) > 0 or len(opponent.abilities) > 0:
            while(self.is_alive() and opponent.is_alive()):
                #Start fighting loop until a hero has won
                print(f'{opponent.name} attacked {self.name}!')
                self.take_damage(opponent.attack())
                print(f"{self.name}'s remaining health: {self.current_health}")
                print(f'{self.name} attacked {opponent.name}!')
                opponent.take_damage(self.attack())
                print(f"{opponent.name}'s remaining health: {opponent.current_health}")
                if self.is_alive() == False:
                    opponent.add_kill(1)
                    self.add_death(1)
                    return (f"{self.name} has been defeated by {opponent.name}")
                elif opponent.is_alive() == False:
                    opponent.add_death(1)
                    self.add_kill(1)
                    return (f"{opponent.name} has been defeated by {self.name}")
        else:
            print("Draw!")
            
        #print(f'{random.choice(hero_choice)} wins!')
    # def fight(self, opponent):
    #     if len(self.abilities) <= 0 or len(opponent.abilities) <= 0:
    #         print ('Draw')
    #     else:
    #         while self.current_health > 0 and opponent.current_health > 0:
    #             opponent_dmg = opponent.attack()
    #             self_dmg = self.attack()
    #             opponent_kills = opponent.add_kill()
    #             opponent.take_damage(self_dmg)
    #             print(opponent.is_alive())
    #             self.take_damage(opponent_dmg)
    #             print(self.is_alive())
    #             if self.is_alive() == False:
    #                 print(f"{opponent.name} has won!")
    #                 opponent_kills += 1
    #             elif opponent.is_alive() == False:
    #                 print(f"{self.name} has won!")
    #             else:
    #                 print("It's a tie!")
    #    hero_choice = [self, opponent]
        #    for hero in hero_choice:
        #        hero.attack()
        #        self.take_damage(opponent.attack())
        #        hero.defend(opponent.attack())


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    weapon1 = Weapon("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    hero1.add_weapon(weapon1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    print(hero1.fight(hero2))

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())