# String Formating for printing

# Dot Format method
# print("STRING {LOCATION INSERTED}".format(INSERTED))

print("This is a string {}".format("INSETED"))
print("The winners are: {} {} {}".format("Jack", "James", "John"))
print("The dog {1} {2} {0}".format("cat", "ate", "the"))
print("The {q} {b} {f}".format(f = "fox", b = "brown", q = "quick"))

# Float formating

Result = 100 / 777

# print("STRING {VALUE:WIDTH.PRECISIONf}".format(VALUE))

print("The result {r:1.3f}".format( r = Result))

# f Strings
# print(f"STRING {value}")

name = "Jose"
print(f"Hello his name is {name}")