    # TIC TAC TOE GAME

print()

# LET's START THE GAME

print("   Let's Play !!  ")
print()

#board

board= ["-","-","-",
        "-","-","-",
        "-","-","-"]

#display board

#========Declaring Global Variables=======

game_running = True
winner = None
current_turn = "X"


#displaying the board

def display_board():

    print(board[0],'|',board[1],'|',board[2]   ,"    1|2|3")
    print(board[3],'|',board[4],'|',board[5]   ,"    4|5|6")
    print(board[6],'|',board[7],'|',board[8]   ,"    7|8|9")

def play_game():

    #display the board

    display_board()

    while game_running :

        handle_turn(current_turn)

        check_if_game_over()

        flip_turn()
        

    #check for winner
    #who wins

    if (winner == 'X' or winner == 'O') :
        print(winner,'won !!')
    elif winner == None :
        print('Game Tie !!')


def handle_turn(player):

    #taking the input position

    print(player ,"'s turn.")
    position = input("Choose from 1 to 9 : ")

#tricky part

    valid = False
    while not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']:
            print("You can't go there. Try again!")
            position = input("Choose from 1 to 9 : ")

        position = int(position)-1

        if board[position] == '-' :
            valid = True
        else:
            print("Wrong Input!")

    board[position] = player

    display_board()

#check game over terms
#when win 
#when there is a tie

def  check_if_game_over():

    check_for_winner()

    check_if_tie()

#who will win

def check_for_winner():

    #global variable

    global winner

    #Calling Winner Functions

    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    
    #checking conditions

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():

    #check rows

    #global variable 

    global game_running
    
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    
    #row checking condition

    if row1 or row2 or row3:
        #game should stop
        game_running = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]


def check_columns():
    
    #check columns

    #global variable 

    global game_running

    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"
    
    #column checking condition

    if col1 or col2 or col3:
        #game should stop
        game_running = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]


def check_diagonals():
    
    #check diagonals

    #global variable

    global game_running
    
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[2] == board[4] == board[6] != "-"

    #diagonal checking condition

    if dia1 or dia2:
        #game should stop
        game_running = False

    if dia1:
        return board[0]
    if dia2:
        return board[2]


def check_if_tie():

    #check if game is still going or not

    #global variable

    global game_running 

    if '-' not in board:
        game_running = False 
        return True 
    else:
        return False


def flip_turn():

    #change player from X to O
    
    #global variable

    global current_turn
    
    if current_turn == "X":
        current_turn = "O"

    #flipping the turn from X to O
    elif current_turn == "O":
        current_turn = "X"
    return


#execution of program starts from here

play_game()



