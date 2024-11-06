def myfunc(a,b):
    # Returns 5% of the sum of a and b
    return sum((a,b)) * 0.05

def myfunc(*args): # *args allows any number of arguments to be passed to the function
    return sum(args) * 0.05

def Myfunc(**kwargs): # **kwargs allows any number of keyword arguments to be passed to the function
    if "Fruit" in kwargs:
        print(f"I love {kwargs['Fruit']}")
    else:
        print("I don't love any fruit")

Result = Myfunc(Fruit = "Apple")
print(Result)

def myfunc2(*args, **kwargs): # *args and **kwargs can be mixed together, the order is important
    print("I would like:", args[0], kwargs["Food"])

result = myfunc2(10,20, Food = "Chocolate")
print(result)