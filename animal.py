class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')
    def drink(self):
        print(f'{self.name} is drinking')
class Frog(Animal):
    def jump(self):
        print(f'{self.name} is jumping')

animal1 = Animal("George")
frog1 = Frog("Melanie")
animal1.eat()
animal1.drink()
frog1.eat()
frog1.drink()
frog1.jump()