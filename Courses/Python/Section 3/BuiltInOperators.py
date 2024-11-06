# Range fuction

MyList = [1, 2, 3, 4, 5]


# for i in range(START,STOP,STEP):

for i in range(3,10,2): 
    print(i)

# Enumerate function

IndexCount = 0

for i in enumerate("abcde"): # The enumerate function returns a tuple containing index and value
    print(f"Character: {i}")


for (a,b) in "abcde":
    print(f"Character: {b}")


# Zip function

MyList1 = [1, 2, 3]
MyList2 = ["a", "b", "c"]

for i in zip(MyList1, MyList2): # Creates a tuple of corresponding elements
    print(i) # Ignores extra elements in the longer list


# In operator

MyList = [1, 2, 3, 4, 5]

if 3 in MyList: # Checks if 3 is in the list
    print("3 is in the list")


# Maths functions

min_value = min(MyList) # Finds the minimum value in the list
max_value = max(MyList) # Finds the maximum value in the list

# Random Library
 
from random import shuffle

MyList = [1, 2, 3, 4, 5]

shuffle(MyList) # Shuffles the elements in the list

print(MyList)

# Randint function

from random import randint
random_value = randint(1,10) # Generates a random integer between 1 and 10

# Input function

name = input("Enter your name: ")
print(f"Hello {name}")