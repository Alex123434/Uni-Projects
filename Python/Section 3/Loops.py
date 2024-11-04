MyList = [1,2,3,4,5,6,7,8,9,10]

# For loop
for i in MyList:
    print(i)

# Print only even number in a list

EvenNums = []

for i in MyList:
    if i % 2 == 0:
        EvenNums.append(i)

print(f"The even numbers in the list are: {EvenNums}")


# Sum all number in a list

ListSum = 0

for i in MyList:
    ListSum += i

print(f"The sum of all number in te list is: {ListSum}")

# Print all letters of a string

MyString = "Hello World"

for i in MyString:
    print(i)

# Tuple Unpacking

MyListOfTuplesPairs = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in MyListOfTuplesPairs:
    print(a)

# Iterate though a Dictionary

Dictionary = {"k1": 1, "k2": 2, "k3": 3}

# Iterating though keys

for i in Dictionary:
    print(i)

# Iterating though Keys and Values

for i in Dictionary.items():
    print(i)

# Iterating through Values

for i in Dictionary.values():
    print(i)

# Tuple Unpacking in Dictionaries

for (a,b) in Dictionary.items():
    print(b)


