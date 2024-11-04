x = 0

while x < 5:
    x = x + 1
    print(f"The current value of x is :{x}")
    
else:
    print("X is not less than 5")


MyString = "Hello World!"

for i in MyString:
    if i == "o":
        continue
    print(i)