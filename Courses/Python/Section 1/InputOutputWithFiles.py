
# Open a file
MyFile = open("MyFile.txt")

# Avoid errors when opening a file
with open("MyFile.txt") as MyNewFile:
    Contents = MyNewFile.read()

# Read a txt file
print(MyFile.read())

# Resets a file so it can be read again
MyFile.seek(0)

# Read a list of lines represented by an element
print(MyFile.readlines())

# Close files
MyFile.close()

# Read to files
with open("MyFile.txt", mode = "r" ) as MyFile:
    Contents = MyFile.read()
    print(Contents)

# Append to files
with open("MyFile.txt", mode = "a" ) as MyFile:
    MyFile.write("This is a new line")

# Write to files
with open("MyNewFile.txt", mode = "w" ) as MyFile:
    MyFile.write("Create a new file")
