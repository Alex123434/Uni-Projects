from random import shuffle

MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def shuffle_list(MyList):
    shuffle(MyList)
    return MyList


def player_guess():

    Guess = ""

    while Guess not in ["0", "1", "2"]:
        Guess = int(input("Guess a number between 1 and 2: "))

    return int(Guess)

Result = player_guess()
print(Result)

def check_guess(Guess, BallList):
    if BallList[Guess] == "o":
        print("Correct! You've won!")
    
    else:
        print("Sorry, you've lost!")
        print(BallList)

BallList = ["","o",""]
MixedUpList = shuffle_list(MyList)
guess = MixedUpList[player_guess()]
check_guess(guess, BallList)
