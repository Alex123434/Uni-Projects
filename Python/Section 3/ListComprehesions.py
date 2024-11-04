# List Comprehension

MyString = "Hello World"

MyList = []

for i in MyString:
    MyList.append(i)

print(MyList)

# More efficient way using list comprehension

MyList = [i for i in MyString] # The square brackets are used instead of append method

print(MyList)

MyNums = [1,2,3,4,5,6,7,8,9,10]

MyList = [num**2 for num in MyNums] #Squares each number and stores in a new list

print(MyList)
       
MyList = [num for num in MyNums if num % 2 == 0] # Filters out odd numbers

print(MyList)

# Nested list comprehension

Celsius = [1,2,3,4,5,6,7]
Farenheit = [((9/5)*temp + 32) for temp in Celsius] # Converts Celsius to Fahrenheit

print(Farenheit)


# This is the same as above but using a single line list comprehension
Farenheit = []

for temp in Celsius:
    Farenheit.append((9/5)*temp + 32)

    print(Farenheit)

# IF, ELSE, AND, OR statements in list comprehension

MyList = [num for num in MyNums if num % 2 == 0 if num > 5] # Filters out odd numbers less than or equal to 5

print(MyList)

MyList = [num if num % 2 == 0 else "Odd" for num in MyNums] # Assigns "Odd" to odd numbers

print(MyList)

# Nested list comprehension with IF, ELSE, AND, OR statements

MyList = [[num if num % 2 == 0 else "Odd" for num in row] for row in [[1,2,3],[4,5,6],[7,8,9]]]

print(MyList)