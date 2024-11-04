# Map Function

def square(num):
    return num ** 2

MyNums = [1, 2, 3, 4, 5]

# Apply square function to each number in MyNums and store result in a new list
MyList = list(map(square, MyNums))
print(MyList)  # Output: [1, 4, 9, 16, 25]

# Filter Function

def is_even(num):
    return num % 2 == 0

MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter out odd numbers from MyList and store result in a new list

MyList = list(filter(is_even, MyList))
print(MyList)  # Output: [2, 4, 6, 8, 10]

# Lambda Expresions

def square(num):
    result = num ** 2
    return result

# Turning a function into a lambda expression

lambda num: num ** 2

# They are useful when you want to use a function only once or pass it as an argument to another function.

list(map(lambda num: num ** 2,MyNums))

list(filter(lambda num: num % 2 == 0, MyList))