MyList = [1,2,3]
print(len(MyList))

MyList = ["one", "two", "three"]
print(MyList[0])
print(MyList[1:])

AnotherList = ["Four", "Five"]

NewList = MyList + AnotherList

print(NewList)


NewList[0] = "eight".upper()
print(NewList)

# Add items to the end of a list
NewList.append("Four")

# Remove items the end of a list
NewList.pop()

# Remove items at an index position
NewList.pop(3)

# Sorting a list
LetterList = ["a", "d", "h", "c"]

# Cannot reasign the result to something else

LetterList.sort()  # Sorts the list in place
print(LetterList)  # Prints the sorted list

# Like this yeah
LetterList = ["a", "d", "h", "c"]
x = sorted(LetterList)  # Creates a new sorted list
print(x)  # Prints the sorted list

# Reversing a list

NumList = [1, 33, 45, 21]
NumList.reverse()
print(NumList)
