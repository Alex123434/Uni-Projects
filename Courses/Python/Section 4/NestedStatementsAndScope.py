# LEGB rule: Local, Enclosing Function, Global, Built-in

x = 25

def printer():
    x = 50
    return x

print(x)  # Output: 25

print(printer())  # Output: 50

# Local Example

lambda num: num ** 2 # num is local to this lambda expression

# Enclosing Function Example

name = "THS IS A GLOBAL STRING" # Global variable

def greet():

    name = "Sammy" # Enclosing Function

    def hello():
        name = "Im a Local" # Local Variable to hello() function
        print("Hello " + name)
    
    hello()

greet()  # Output: Hello Sammy

# Scope Example

x = 50

def func():
    global x # Changing global x value
    print("x is", x)

    x = 200 # Changing global x value
    print("Changed global x to", x) # Output: Changed local x to 200

func(x)  # Output: x is 50
print("x is still", x) # Output: x is still 50