class Dog():
    # This class represents a dog

    # Class object attributes, same for all instances
    species = "Canis familiaris"

    def __init__(self,breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    # Instance method (Actions methods)

    def bark(self, food):
        print(f"Woof! My name is {self.name} , I am {self.age} years old and I eat {food}!")

# Create an instance of the Dog class with a breed of Labrador
mydog = Dog(breed = "Labrador", name = "Buddy", age = 3)

print(type(mydog))

# Create an instance of the Dog class

print(mydog.species)  
print(mydog.breed)
print(mydog.name)
print(mydog.age)

# Call the instance method

mydog.bark("Chicken")