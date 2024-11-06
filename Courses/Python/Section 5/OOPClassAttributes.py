mylist= [1, 2, 3, 4, 5]

class Dog():
    # This class represents a dog
    def __init__(self,breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

# Create an instance of the Dog class with a breed of Labrador
mydog = Dog(breed = "Labrador", name = "Buddy", age = 3)

print(type(mydog))

# Create an instance of the Dog class

print(mydog.breed)
print(mydog.name)
print(mydog.age)
