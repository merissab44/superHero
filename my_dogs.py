from dog import Dog
# instantiation call which creates the dog object
# in order to store and access the name we assign it to a variable
my_dog = Dog("Rex", "SuperDog")
my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)
# print(my_dog.breed)
# # Python implicitly passes self so we don't need to when we call a funtion
# my_dog.bark()