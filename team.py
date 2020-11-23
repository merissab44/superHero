class Team:
    def __init__(self, name):
        '''This is the team name'''
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        pass

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
        pass