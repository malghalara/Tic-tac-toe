import random
  
# starting the game with display message 
print ("""           _______    _____   _________  ______  _____   ________  _____     _____
              |    | |            |     |     | |           |     |     |   |
              |    | |      ---   |     |_____| |      ---  |     |     |   |-----
              |    | |_____       |     |     | |_____      |     |____ |   |____     """)
#game board via 2D list, formating, function calling
board=[
    ["1", "2", "3"],
    ["4", "5", "6"],   
    ["7", "8", "9"],
]

#display board function 
def display_board(board):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(board[0][0], board[0][1], board[0][2])) 
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(board[1][0], board[1][1], board[1][2]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}  ".format(board[2][0], board[2][1], board[2][2]))
    print("\t     |     |")
    print("\n")

display_board(board)

# Selecting mode of game
def getGameMode(): 
    print("----------Select Mode---------------")  
    print("To start the Game enter 1 ")
    print("To exit game enter 2")
    selected_mode = int(input(""))
    while (selected_mode!=1 and selected_mode!=2): 
        selected_mode = int(input("You have entered invalid input. please enter 1 to start again and 2 for exit: "))
    return selected_mode

# Player Mark selection
def getPlayerMark(player1):  
        print(player1,"enter your mark O or X")
        p1_mark = input("").capitalize()
        while (p1_mark!="X" and p1_mark!="O"):
            p1_mark=input("You have entered incorrect mark, please enter O or X:  ").capitalize()
        if p1_mark=="O":
            return ("O", "X")
        else:
            return ("X", "O")
# Toss for game
def getTossValue(player1,player2):                  
        TOSS_VALUE = random.randint(0,1)
        p1_toss = input("Enter 0 for head or 1 for tail:  ")
        while (p1_toss != "0" and p1_toss != "1"):
            p1_toss = input("Please enter correct value: ")
        p1_toss = int(p1_toss)
        if (TOSS_VALUE == p1_toss ):
            print(f"{player1} has won the toss")
            player_turn = player1
        else:
            print(f"{player2} has won the toss")
            player_turn = player2
        return player_turn

# starting the game
def playGame(p1_mark, player_turn, player1, player2, p2_mark):
    count = 1
    print("--------THE GAME IS STARTED----------\n")
    while count <=9:
        if(player_turn == player1):
            print(player1,"it is your turn")
            display_board(board)
            p1_move = (input("Enter a position through 1 to 9 or \"q\" to quit: "))
            if (quitGame(p1_move)): break
            if not (check_input(p1_move)): 
                continue    #again start from input
            p1_move = int(p1_move)
            coards = getCordinates(p1_move)
            if isTaken(coards):
                print("This position is already taken. Please select another position")
                continue 
            else:
                add_to_board(coards,board,p1_mark)
                display_board(board)
                isP1Winner = check_winner(board, p1_mark)
                if (isP1Winner): 
                    print("-------------WOHOO Player 1 has won the game!") 
                    break
                else:
                    if count == 9:
                        print("The match is tie ")
                        break
                player_turn = player2
                count = count + 1
        else:
            print(player2,"it is your turn")
            getp2Move(p1_mark, p2_mark, count, board)
            isP2Winner = check_winner(board, p2_mark)
            if(isP2Winner):
                print("-------------WOHOO Player 2 has won the game!") 
                break
            elif count == 9:
                print("The match is tie ")
                break
            player_turn = player1
            count = count + 1

# if user wants to quit the game
def quitGame(p1_move):
    if (p1_move) == "q" or (p1_move) == "Q" :
        print("The game is end")
        return True
    else: 
        False

# checking the validity of input
def check_input(p1_move):
    if (p1_move.isnumeric()):
        if (int(p1_move) >=1 and int(p1_move) <=9):
            return True
        else:
            print('The number is not in bound')
            return False
    else:
        print('This is an invalid number')
        return False

# converting the user input into cordinates
def getCordinates(p1_move):
    p1_move = p1_move - 1
    row = int(p1_move/3)
    column = p1_move
    if (column > 2):
        column = p1_move % 3
    return(row,column)  

# checking if the user input is already taken or not
def isTaken(coards):
    row = coards[0]
    column = coards[1]
    if (board[row][column]=="O" or board[row][column]=="X" ):
        return True
    else: 
        return False

# inserting mark on the board
def add_to_board(coards,board, symbol):
    row = coards[0]
    column = coards[1]
    board[row][column] = symbol

# checking winner by matching rows , column and diagnols
def check_winner(board, symbol):
  # check rows
  for row in range(3):
    if board[row][0] == symbol and board[row][1] == symbol and board[row][2] == symbol:
      return True
  # check columns
  for col in range(3):
    if board[0][col] == symbol and board[1][col] == symbol and board[2][col] == symbol:
      return True
  # check diagonals
  if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
    return True
  if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
    return True
  return False

# checking the conditions to declare the winner
def getp2Move(p1_mark, p2_mark, count, board): 
    if(board[1][1] != p1_mark and count == 1):
        board[1][1]=p2_mark

    elif board[1][1]==p1_mark and count==2:
        board[0][0]=p2_mark

    elif board[1][1]!=p1_mark and count==2:
        board[1][1]=p2_mark
        
    elif(board[0][0]==p2_mark and board[0][1]==p2_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark
        
    elif(board[1][0]==p2_mark and board[1][1]==p2_mark) and (not isTaken ((1,2))):
        board[1][2]=p2_mark

    elif(board[2][0]==p2_mark and board[2][1]==p2_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark
    
    elif(board[0][0]==p2_mark and board[1][0]==p2_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark

    elif(board[0][1]==p2_mark and board[1][1]==p2_mark) and (not isTaken ((2,1))):
        board[2][1]=p2_mark

    elif(board[0][2]==p2_mark and board[1][2]==p2_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark 
       
    elif(board[0][0]==p2_mark and board[1][1]==p2_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark

    elif(board[0][2]==p2_mark and board[1][1]==p2_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark

    elif(board[0][0]==p2_mark and board[0][2]==p2_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark

    elif(board[1][0]==p2_mark and board[1][2]==p2_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark

    elif(board[2][0]==p2_mark and board[2][2]==p2_mark) and (not isTaken ((2,1))):
        board[2][1]=p2_mark
                      
    elif(board[0][0]==p2_mark and board[2][0]==p2_mark) and (not isTaken ((1,0))):
        board[1][0]=p2_mark

    elif(board[0][1]==p2_mark and board[2][1]==p2_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark

    elif(board[0][2]==p2_mark and board[2][2]==p2_mark) and (not isTaken ((1,2))):
        board[1][2]=p2_mark

    elif(board[0][0]==p2_mark and board[2][2]==p2_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark

    elif(board[0][2]==p2_mark and board[2][0]==p2_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark
    
    elif(board[0][1]==p2_mark and board[0][2]==p2_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark
        
    elif(board[1][1]==p2_mark and board[1][2]==p2_mark) and (not isTaken ((1,0))):
        board[1][0]=p2_mark

    elif(board[2][1]==p2_mark and board[2][2]==p2_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark

    elif(board[1][0]==p2_mark and board[2][0]==p2_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark

    elif(board[1][1]==p2_mark and board[2][1]==p2_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark

    elif(board[1][2]==p2_mark and board[2][2]==p2_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark

    elif(board[1][1]==p2_mark and board[2][2]==p2_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark

    elif(board[2][0]==p2_mark and board[1][1]==p2_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark

    elif(board[0][0]==p1_mark and board[0][1]==p1_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark

    elif(board[1][0]==p1_mark and board[1][1]==p1_mark) and (not isTaken ((1,2))):
        board[1][2]=p2_mark
        
    elif(board[2][0]==p1_mark and board[2][1]==p1_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark

    elif(board[0][0]==p1_mark and board[1][0]==p1_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark

    elif(board[0][1]==p1_mark and board[1][1]==p1_mark) and (not isTaken ((2,1))):
        board[2][1]=p2_mark

    elif(board[0][2]==p1_mark and board[1][2]==p1_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark
    
    elif(board[0][0]==p1_mark and board[1][1]==p1_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark
    
    elif(board[0][2]==p1_mark and board[1][1]==p1_mark) and (not isTaken((2, 0))):
        board[2][0]=p2_mark
    
    elif(board[0][0]==p1_mark and board[0][2]==p1_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark
        
    elif(board[1][0]==p1_mark and board[1][2]==p1_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark
        
    elif(board[2][0]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((2,1))):
        board[2][1]=p2_mark
        
    elif(board[0][0]==p1_mark and board[2][0]==p1_mark) and (not isTaken ((1,0))):
        board[1][0]=p2_mark
        
    elif(board[0][1]==p1_mark and board[2][1]==p1_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark
        
    elif(board[0][2]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((1,2))):
        board[1][2]=p2_mark
    
    elif(board[0][0]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark
        
    elif(board[0][2]==p1_mark and board[2][0]==p1_mark) and (not isTaken ((1,1))):
        board[1][1]=p2_mark
        
    elif(board[0][1]==p1_mark and board[0][2]==p1_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark
        
    elif(board[1][1]==p1_mark and board[1][2]==p1_mark) and (not isTaken ((1,0))):
        board[1][0]=p2_mark

    elif(board[2][1]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark
    
    elif(board[1][0]==p1_mark and board[2][0]==p1_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark
    
    elif(board[1][1]==p1_mark and board[2][1]==p1_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark
        
    elif(board[1][2]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark
    
    elif(board[1][1]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark
        
    elif(board[1][1]==p1_mark and board[2][0]==p1_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark
    
    elif(board[0][1]==p1_mark and board[2][0]==p1_mark) and (not isTaken ((0,0))):  
        board[0][0]=p2_mark
    
    elif(board[0][1]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark
    
    elif(board[2][1]==p1_mark and board[0][2]==p1_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark
    
    elif(board[2][1]==p1_mark and board[0][0]==p1_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark
    
    elif(board[1][0]==p1_mark and board[2][2]==p1_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark
    
    elif(board[1][0]==p1_mark and board[0][2]==p1_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark
    
    elif(board[1][2]==p1_mark and board[0][0]==p1_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark
    
    elif(board[1][2]==p1_mark and board[2][0]==p1_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark
    
    elif(board[1][1]==p2_mark and board[0][0]==p1_mark and board[2][2]== p1_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark
    
    elif(board[1][1]==p2_mark and board[0][1]==p1_mark and board[2][1]== p1_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark
    

    elif(board[1][1]==p2_mark and board[0][2]==p1_mark and board[2][0]== p1_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark
    
    elif(board[1][1]==p2_mark and board[1][0]==p1_mark and board[1][2]== p1_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark
    
    elif(board[1][1]==p1_mark and board[0][2]==p1_mark) and (not isTaken ((1,2))):
        board[1][2]=p2_mark
    
    elif(board[2][1]==p1_mark and board[1][2]==p1_mark) and (not isTaken ((2,2))):
        board[2][2]=p2_mark
    
    elif(board[1][0]==p1_mark and board[2][1]==p1_mark) and (not isTaken ((2,0))):
        board[2][0]=p2_mark
    
    elif(board[1][0]==p1_mark and board[0][1]==p1_mark) and (not isTaken ((0,0))):
        board[0][0]=p2_mark
    
    elif(board[0][1]==p1_mark and board[1][2]==p1_mark) and (not isTaken ((0,2))):
        board[0][2]=p2_mark
    
    elif(board[1][1]==p2_mark and board[1][0]==p1_mark and board[0][2]== p1_mark) and (not isTaken ((0,1))):
        board[0][1]=p2_mark
    
    elif(board[0][0]==p2_mark and board[1][1]==p1_mark) and (not isTaken((0,1))):
        board[0][1]=p2_mark
    
    elif board[0][0]==p1_mark and board[1][1]==p2_mark and (not isTaken((0,1))):
        board[0][1]=p2_mark
    
    elif board[1][1]==p2_mark and board[0][2]==p1_mark and (not isTaken((2,0))):
        board[2][0]=p2_mark
    
    elif board[0][0]==p1_mark and board[1][1]==p2_mark and (not isTaken((1,0))):
        board[1][0]=p2_mark
    
    elif(board[0][0]==p1_mark and board[1][1]==p2_mark and board[2][2]==p1_mark) and (not isTaken((1, 2))):
        board[1][2] = p2_mark

    elif(board[0][2]==p1_mark and board[1][1]==p2_mark and board[2][0]== p1_mark) and (not isTaken ((1,0))):
        board[1][0]=p2_mark
    
    #opposite applying
    elif(board[0][0]== p1_mark ) and( not isTaken((0,2))):
        board[0][2] = p2_mark
    
    elif(board[1][0]== p1_mark ) and( not isTaken((1,2))):
        board[1][2] = p2_mark
    
    elif(board[2][0]== p1_mark ) and( not isTaken((2,2))):
        board[2][2] = p2_mark
    
    elif(board[0][1]== p1_mark ) and( not isTaken((2,1))):
        board[2][1] = p2_mark
    
    elif(board[0][0]== p1_mark ) and( not isTaken((2,0))):
        board[2][0] = p2_mark
    
    elif(board[0][2]== p1_mark ) and( not isTaken((2,2))):
        board[2][2] = p2_mark
    
    elif(board[0][0]== p1_mark ) and( not isTaken((2,2))):
        board[2][2] = p2_mark
    
    elif(board[0][2]== p1_mark ) and( not isTaken((2,0))):
        board[2][0] = p2_mark
    
    elif(board[1][2]== p1_mark ) and( not isTaken((1,0))):
        board[1][0] = p2_mark
    
    elif(board[2][2]== p1_mark ) and( not isTaken((2,0))):
        board[2][0] = p2_mark
    
    elif(board[2][1]== p1_mark ) and( not isTaken((0,1))):
        board[0][1] = p2_mark
    
    elif(board[2][0]== p1_mark ) and( not isTaken((0,0))):
        board[0][0] = p2_mark
    
    elif(board[2][2]== p1_mark ) and( not isTaken((0,2))):
        board[0][2] = p2_mark
    
    elif(board[2][2]== p1_mark ) and( not isTaken((0,0))):
        board[0][0] = p2_mark
    
    elif(board[2][0]== p1_mark ) and( not isTaken((0,2))):
        board[0][2] = p2_mark
    

    display_board(board)

def main():
    while True:
        selected_mode = getGameMode()
        if(selected_mode == 1): 

            print("--------------WELCOME TO SINGLE PLAYER GAME-------------------")
            #player selection
            player1 = input("Enter your name: ").capitalize()
            player2 = "Computer"
            p1_mark, p2_mark = getPlayerMark(player1)
            print(f"{player1} your make is {p1_mark} and {player2} mark is {p2_mark}")
            player_turn = getTossValue(player1,player2)
            playGame(p1_mark, player_turn, player1, player2, p2_mark)
         
        else : 
            print("----------------GAME OVER-------------------")
        play_again = input("Do you want to play again? Enter Y for yes and press any other key to exit game: ").capitalize()
        if (play_again == "y" or play_again == "Y"):
            count = 1 
            for row in range(3):
                for col in range(3):
                    board[row][col] = count
                    count +=1
            continue
        else:
            print("Game Exit")
            break

main()
