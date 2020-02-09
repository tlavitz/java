#Display the game instructions
#determine who goes first
#create an empty tictac board
#while nobodys won and its not a tie
#    if its the human turn
#        get human move
#        updatethe board with the move
#    otherwise
#        calculate the computers move
#        update the board with the move
#    dispaly the board
#   switch turns
#congratulate winner or declare tie

#global constants
X="X"
O="O"
EMPTY=" "
TIE="TIE"
NUMOFSQUARES=9

#display_intruct() FUNCTION
def display_inst():
    print(
        """
                 Welcome to Tic Tac Toe.
                  You VS. The Computer

    Make your move by entering number 0-8. The number
        will correspond to the board position as shown:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8


                        Lets Play! \n
        """

    )

#the yes and no function

def yesNo(question):
    """Ask a yes or no question"""
    response=None
    while response not in ("y","n"):
        response=input(question).lower()
    return response

#the ask number function

def askNum(question,low,high):
    """Ask for a number within a rnage"""
    response=""
    while response not in range(low,high):
        response=int(input(question))
    return response


#the pieces Function
def pieces():
    """determine if player or computer goes first"""
    whosfirst=yesNo("Do you want to make the first move? [y/n]: ")
    if whosfirst=="y":
        print("\nOk you go first..")
        human=X
        computer=O
    else:
        print("\nAha!!making me go first will be your end..I'll go first.")
        computer=X
        human=O
    return computer,human


#create new board function
def newBoard():
    """create new game board"""
    board=[]
    for square in range(NUMOFSQUARES):
        board.append(EMPTY)
    return board


displayBoard function

def displayBoard(board):
    """display game board on screen."""
    print("\n\t",board[0],"|"board[1],"|",board[2])
    print("\t","---------")
    print("\n\t",board[3],"|"board[4],"|",board[5])
    print("\t","---------")
    print("\n\t",board[6],"|"board[7],"|",board[8],"\n")

#make legal moves function
def legalMoves(board):
    """create list of legal moves"""
    moves=[]
    for square in range(NUMOFSQUARES):
        if board[square]==EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """determine the game winner"""
    WINPATTERN=((0,1,2),
    (3,4,5),
    (6,7,8),
    (0,3,6),
    (1,4,7),
    (2,5,8),
    (0,4,8),
    (2,4,6),)
    for row in WINPATTERN:
        if board[row[0]]==