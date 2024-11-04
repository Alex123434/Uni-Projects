def say_hello():
    print("Hello, World!")

say_hello() # Function call to print "Hello, World!"

def say_name(name):
    print(f"hello {name}")

say_name("Pepe") # Function call 

def say_name(name = "Default"): # Function call with default argument
    print(f"hello {name}")

say_name() # Function call with default argument

def add_numbers(a, b):
    return a + b

Result = add_numbers(5, 3) # Function call with arguments, assigning result to variable
print(Result)

def even_check(number):
    result = number % 2 == 0
    return result

def even_check(number):
    return number % 2 == 0 # This is a more concise version of the function

IsEven = even_check(10) # Function call with argument, assigning result to variable

# Return true if any number in the list is even

def check_even_list(MyList):
    for num in MyList: 
        if num % 2 == 0:
            return True
        else:
            pass

    return False

result = check_even_list([1,3,7])
print(result)


# Return all even number in a list

def return_all_even(MyList):
    EvenNums = []
    for num in MyList:
        if num % 2 == 0:
            EvenNums.append(num)
        else:
            pass
     
    return EvenNums

ResultEven = return_all_even([5,7,17,89,4,2,55,67,88])
print(ResultEven)
