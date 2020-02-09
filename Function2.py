#Understanding abstraction
#by writing and calling functions, you practice whats known as abstrction.
#Abstraction lets you think about the big picture w/o worrying about the details.
#e.g. funtion for getting age..we dont worry how it is being computed, we just call the function
def instructions():
    """displays the game instructions."""
    print(
        """
                  Welcome to Tic-Tac-Toe.

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

#main
print("heres the instruction")
instructions()
