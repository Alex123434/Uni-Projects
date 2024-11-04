from random import randint

RandomNum = randint(1,100) 

PlayerGuess = int(input("Try to guess my number, its between 1-100: \n"))

Attempts = 10

AttemptsCondition = True

while AttemptsCondition == True:

    if PlayerGuess == RandomNum:
        print(f"Congratulations, you guessed my number correctly!! \n")
        break

    elif Attempts == 0:
        AttemptsCondition = False
        print(f"You ran out of attempts, my number was {RandomNum}\n")

    elif PlayerGuess > RandomNum:

        print(f"Remaining attempts: {Attempts - 1}")
        print(f"LOWER")
        PlayerGuess = int(input("Try to guess my number, its between 1-100: \n"))
        Attempts -= 1
    
    else:

        print(f"Remaining attempts: {Attempts - 1}")
        print(f"HIGHER")
        PlayerGuess = int(input("Try to guess my number, its between 1-100: \n"))
        Attempts -= 1
    