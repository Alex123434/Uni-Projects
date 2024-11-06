
MyStr = "Hello World"


# Indexing first character
print(MyStr[0])

# Indexing last character
print(MyStr[-1])


MyStr = "abcdefghijk"

# Slicing 

# MyStr[START:STOP:STEP]

# Go from 2 up to the end
print(MyStr[2:]) 

# Go from 2 up to 5, not including 5
print(MyStr[2:5]) 

# Step Size

# Go from the start to the end in jumps of 2
print(MyStr[::2])

# Reverse string

# Get all but starting from th end
print(MyStr[::-1])