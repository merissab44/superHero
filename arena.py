from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        # Get the ability info from user
        #this include the name and max damage
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of the ability? ")

        return Ability(name, max_damage)

    def create_weapon(self):
        # get weapon info from user
        #this include the name and max damage

        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")

        return Weapon(name, max_damage)

    def create_armor(self):
        # get armor info from user
        #this include the name and max block

        name = input("What is the armor name? ")
        max_block = input("What is the max block of this armor? ")

        return Armor(name, max_block)

    def create_hero(self):
        #get hero info from user
        # this includes name and any other methods that can be called
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               #TODO add an ability to the hero
               self.create_ability()
               hero.add_ability(self.create_ability)
               #HINT: First create the ability, then add it to the hero
           elif add_item == "2":
               #TODO add a weapon to the hero
               self.create_weapon()
               hero.add_weapon(self.create_weapon)
               #HINT: First create the weapon, then add it to the hero
           elif add_item == "3":
               #TODO add an armor to the hero
               self.create_armor()
               hero.add_armor(self.create_armor)
               #HINT: First create the armor, then add it to the hero
        return hero
    def build_team_one(self):

        team_name = input("What is your team name team one? ")
        self.team_one = Team(team_name)
        # Prompt the user for the number of heroes on team one
        #for every hero the user wants to add, add it to the team
        numOfTeamMembers = int(input("How many members would you like on Team One? "))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            team1 = self.team_one
            team1.add_hero(hero)

    def build_team_two(self):
        team_name = input("What is your team name team two? ")
        self.team_two = Team(team_name)
        # Prompt the user for the number of heroes on team one
        #for every hero the user wants to add, add it to the team
        teamMembers2 = int(input("How many heroes would you like to add to team two?\n"))
        for i in range(teamMembers2):
            hero = self.create_hero()
            team2 = self.team_two
            team2.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)
        if self.team_one == 0:
            print(f"{self.team_two.name} has won the battle!")
        elif self.team_two == 0:
            print(f"{self.team_one.name} has won the battle!")

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        # This is how to calculate the average K/D for Team One
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))
        # Average K/D for Team two
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team_kills/team_deaths))
        #team one survivors
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        #team two survivors
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()