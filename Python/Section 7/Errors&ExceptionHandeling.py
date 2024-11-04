def add (n1,n2):
    print(n1 + n2)

try:
    # Attempt this code but my have an error
     Result = add(10, "20")
     print(Result)

except:
    # What I want to do if an error occurs
    print("An error occurred, you didn't provide valid inputs.")

else:
    # This code will run if no error occurs
    print("No error occurred.")
    print(Result)

# Check if the file was created successfully

try:
    f = open("TestFile.txt", "r")
    f.write("Hello, this is a test.")

# Check if the file was created successfully

except TypeError:

    print("There was a type error.")

except OSError:
    print("OS error occurred.")

except:
    print("All other exceptions.")

finally:
    # This code will run whether or not an error occurred
    print("This code block will always run.")
    if 'f' in locals():
        f.close()

def ask_for_int():

    while True:
        try:
            result = int(input("Please enter an integer: "))
        except: 
            print("That's not an integer!")
            continue
        else:
            print("Thank you for entering an integer.")
            break
        finally:
            print("This code block will always run.")
        
ask_for_int()
