class Dog:
    # Required attributes are defined inside a init method
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")
    # Methods are functions inside of the class
    # We always need to put self parameter for every class method
    def bark(self):
        print("Woof")