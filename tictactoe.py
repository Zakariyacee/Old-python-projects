import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

currentplayer = "x"
winner = None
gamerunning = True

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("__________")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("__________")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("__________")

def playerinput(board):
    userinput = int(input("Input a number between 1 to 9 "))
    if userinput >= 1 and userinput <= 9 and board[userinput-1] == "-":
        board[userinput-1] = currentplayer
    else:
        print("Sorry, a player is already in that spot")


# chech for win or tie
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True

def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("Its a tie!")
        gamerunning = False


def checkforwin():
    if checkdiagonal(board) or checkhorizontal(board) or checkrow(board):
        print(f"the winner is {winner}")


# swtitch to other player

def switchplayer(): # only pass arguments into the parenthesis when ur gonna modify the board 
    global currentplayer
    if currentplayer == "x":
        currentplayer = "o"
    else:
        currentplayer = "x"
# check for the win or tie again


def computer(board):
    while currentplayer == "o":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "o"
            switchplayer()




while gamerunning:
    printboard(board)
    playerinput(board)
    checkforwin()
    checktie(board)
    switchplayer()
    computer(board)
    checktie(board)
