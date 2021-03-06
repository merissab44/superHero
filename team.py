import random
from random import choice
from hero import Hero
class Team:
    def __init__(self, name):
        '''This is the team name'''
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)
    def remove_hero(self, name):
        foundHero = False
        #loop through each hero in the list self.heroes
        for hero in self.heroes:
            # if we find a name in the list that matches the name 
            # we passed in 
            if hero.name == name:
                self.heroes.remove(hero)
                # set the condition to True
                foundHero = True
            #if we did not find a hero with the name in the list
            # return 0
            if not foundHero:
                return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(f"hero: {hero.name}")

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)

            hero1.fight(hero2)

            if hero1.is_alive() == False:
                self.remove_hero(hero1)
            elif hero2.is_alive() == False:
                other_team.remove_hero(hero2)
            else:
                self.remove_hero(hero1)
                other_team.remove_hero(hero2)
    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths = 1
            kd = hero.kills/hero.deaths 
            print(f"{hero.name} Kill/ Deaths: {kd}")


# if __name__ == "__main__":

#     avengers = Team("Avengers")
#     dc = Team("DC")

#     avengers.add_hero("Spider Man")
#     avengers.add_hero("Iron Man")

#     dc.add_hero("Scorpion")
#     dc.add_hero("Sub Zero")

#     dc.view_all_heroes()
#     avengers.living_heroes = ["Iron Man", "Captain America", "Hulk", "Black Panther"]
#     dc.living_opponents = ["Scorpion", "Jack", "Athena", "Sub Zero"]

#     print(avengers.attack(dc))