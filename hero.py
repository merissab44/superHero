class Hero:
    # We want out hero to have a default "starting health"
    # we set that in the finction header
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        # when a hero is created the current health
        # us the same as their starting health
        self.current_health = starting_health

if __name__ == "__main__":
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health)