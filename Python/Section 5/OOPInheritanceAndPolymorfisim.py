# Inheritance example

class Animal():

    def __init__(self):
        print("Animal created")

    def who_am_i(self):
        print("I am an animal")
    
    def eat(self):
        print("I am eating")

# Derived classes

class Dog(Animal):

    def __init__(self):
        # Inherit from Animal class 
        Animal.__init__(self)
        print("Dog created")

    # Override method
    def who_am_i(self):
        print("I am a dog")

mydog = Dog()

print(mydog.who_am_i())
print(mydog.eat())

# Polymorphism

class Dog():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"
    
class Cat():

    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"
    
niko = Dog("Niko")
felix = Cat("Felix")

print(niko.speak())
print(felix.speak())

# Demostrate Polymorphism

for pet in [niko, felix]:

    print(type(pet))
    print(pet.speak())

# Another way to demonstrate polymorphism

def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(felix)

# Abstract Classes

class Animal():
    def __init__(self,name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
    
myanimal = Animal("Fred")
print(myanimal.speak()) # This will raise an error

# Interface example 

class Dog(Animal):

    def speak(self):
        return self.name + " says woof!"
    
fido = Dog("fido")
print(fido.speak())