def hello(name = "Jose"):
    print("The hello function has been called")

    def greet():
        return "This is the greet function inside hello"
    
    def welcome():
        return "This is the welcome function inside hello"
    
    if name == "Jose":
        return greet
    else:
        return welcome


new_func = hello()
print(new_func())


def cool():

    def super_cool():
        return "I am super cool"
    
    return super_cool

some_func = cool()
print(some_func())


def hello():
    return "Hello from Jose"

def other(some_def_func):
    print("Other code is available")
    print(some_def_func())

other(hello)


def new_decorator(original_func):

    def wrap_func():
        print("Some extra code before the original function execution")
        original_func()
        print("Some extra code after the original function execution")
    
    return wrap_func

def func_to_be_decorated():
    print("I want to be decorated")

decorated_func = new_decorator(func_to_be_decorated)()

@new_decorator

def func_to_be_decorated_2():
    print("I want to be decorated 2")

func_to_be_decorated_2()