"""
Errors and Exceptions Homework
Problem 1
Handle the exception thrown by the code below by using try and except blocks.

"""

for i in [3,5,6]:

    try:
       
        ans = print(i**2)
        
    
    except TypeError:
       
            print("Error: Cannot perform operation on non-numeric values.")
           
    else:
        print("Program execution completed.")
        print(ans)


"""
Problem 2
Handle the exception thrown by the code below by using try and except blocks. 
Then use a finally block to print 'All Done.'

"""

x = 5
y = 0

try:
    z = x/y

except ZeroDivisionError:
     print("Error: Division by zero is not allowed.")

finally:
     print("All Done.")


"""
Problem 3
Write a function that asks for an integer and prints the square of it. 
Use a while loop with a try, except, else block to account for incorrect inputs.
"""

def ask():

     while True:
        try:
            ans = int(input("Please enter a integer: \n"))
        
        except:
            print("This is not an integer, try again: ")
            continue
        else:
            print("This is an integer, thank you")
            break



ask()
