def print_tic_tac_toe(board):
    print("-------------")
    for row in board:
        print("|", " | ".join(row), "|")
        print("-------------")

def x_print1(board):
    if Player1Turn == 1 and Player1Op == "X":
        board[0][0] = "X"
        print_tic_tac_toe(board)

    elif Player1Turn == 2 and Player1Op == "X":
        board[0][1] = "X"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 3 and Player1Op == "X":
        board[0][2] = "X"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 4 and Player1Op == "X":
        board[1][0] = "X"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 5 and Player1Op == "X":
        board[1][1] = "X"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 6 and Player1Op == "X":
        board[1][2] = "X"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 7 and Player1Op == "X":
        board[2][0] = "X"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 8 and Player1Op == "X":
        board[2][1] = "X"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 9 and Player1Op == "X":
        board[2][2] = "X"
        print_tic_tac_toe(board)

def o_print1(board):
    if Player1Turn == 1 and Player1Op == "O":
        board[0][0] = "O"
        print_tic_tac_toe(board)

    elif Player1Turn == 2 and Player1Op == "O":
        board[0][1] = "O"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 3 and Player1Op == "O":
        board[0][2] = "O"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 4 and Player1Op == "O":
        board[1][0] = "O"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 5 and Player1Op == "O":
        board[1][1] = "O"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 6 and Player1Op == "O":
        board[1][2] = "O"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 7 and Player1Op == "O":
        board[2][0] = "O"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 8 and Player1Op == "O":
        board[2][1] = "O"
        print_tic_tac_toe(board)
    
    elif Player1Turn == 9 and Player1Op == "O":
        board[2][2] = "O"
        print_tic_tac_toe(board)

def x_print2(board):
    if Player2Turn == 1 and Player2Op == "X":
        board[0][0] = "X"
        print_tic_tac_toe(board)

    elif Player2Turn == 2 and Player2Op == "X":
        board[0][1] = "X"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 3 and Player2Op == "X":
        board[0][2] = "X"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 4 and Player2Op == "X":
        board[1][0] = "X"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 5 and Player2Op == "X":
        board[1][1] = "X"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 6 and Player2Op == "X":
        board[1][2] = "X"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 7 and Player2Op == "X":
        board[2][0] = "X"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 8 and Player2Op == "X":
        board[2][1] = "X"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 9 and Player2Op == "X":
        board[2][2] = "X"
        print_tic_tac_toe(board)

def o_print2(board):
    if Player2Turn == 1 and Player2Op == "O":
        board[0][0] = "O"
        print_tic_tac_toe(board)

    elif Player2Turn == 2 and Player2Op == "O":
        board[0][1] = "O"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 3 and Player2Op == "O":
        board[0][2] = "O"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 4 and Player2Op == "O":
        board[1][0] = "O"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 5 and Player2Op == "O":
        board[1][1] = "O"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 6 and Player2Op == "O":
        board[1][2] = "O"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 7 and Player2Op == "O":
        board[2][0] = "O"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 8 and Player2Op == "O":
        board[2][1] = "O"
        print_tic_tac_toe(board)
    
    elif Player2Turn == 9 and Player2Op == "O":
        board[2][2] = "O"
        print_tic_tac_toe(board)

def win_check(board):
    global Winner  # Tell Python to use the global variable

    # Check all rows
    if board[0][0] == board[0][1] == board[0][2] != " ":
        Winner = True
       
    elif board[1][0] == board[1][1] == board[1][2] != " ":
        Winner = True
       
    elif board[2][0] == board[2][1] == board[2][2] != " ":
        Winner = True

    # Check all columns
    elif board[0][0] == board[1][0] == board[2][0] != " ":
        Winner = True
    
    elif board[0][1] == board[1][1] == board[2][1] != " ":
        Winner = True
    
    elif board[0][2] == board[1][2] == board[2][2] != " ":
        Winner = True

    # Check both diagonals
    elif board[0][0] == board[1][1] == board[2][2] != " ":
        Winner = True
    
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        Winner = True

    return Winner  
    


board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

Winner = False         

TakenMoves = []

Player1Op = str(input("Player 1, choose your marker (X or O): \n"))

ValidFormat = False

while ValidFormat == False:
    if Player1Op != "O" and Player1Op != "X":
        Player1Op = str(input("Invalid input. Please choose 'X' or 'O'.\n"))
    else:
        ValidFormat = True

if Player1Op == "X":
    Player2Op = "O"

elif Player1Op == "O":
    Player2Op = "X"

print(f"Player 1, you will use {Player1Op}.\n")
print(f"Player 2, you will use {Player2Op}.\n")   

print_tic_tac_toe(board)
print("\n")

while Winner == False:

    Player1Turn = int(input("Player 1, select your desired position (1-9): \n"))

    for i in TakenMoves:
        if int(i) == Player1Turn:
            Player1Turn = int(input("Invalid move. This position is already taken. Please try again.\n"))
            continue
        else:
            continue

    if Player1Op == "O":
        o_print1(board)
        TakenMoves.append(Player1Turn)

    elif Player1Op == "X":
        x_print1(board)
        TakenMoves.append(Player1Turn)

    print("\n")
    print_tic_tac_toe(board)
    print("\n")

    win_check(board)

    if Winner == True:
        Winner = True
        print("Congratulations Player 1, You have won!")
        break

    Player2Turn = int(input("Player 2, select your desired position (1-9): \n"))
    
    for i in TakenMoves:
        if int(i) == Player2Turn:
            Player2Turn = int(input("Invalid move. This position is already taken. Please try again.\n"))
            continue
        else:
            continue

    if Player2Op == "X":
        x_print2(board)
        TakenMoves.append(Player2Turn)
            
    elif Player2Op == "O":
        o_print2(board)
        TakenMoves.append(Player2Turn)
    
    print("\n")
    print_tic_tac_toe(board)
    print("\n")

    win_check(board)

    if Winner == True:
        Winner = True
        print("Congratulations Player 2, You have won!")
        break