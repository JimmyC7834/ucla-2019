# Summer Discover 2019
# Computer Programming
# Rock-Paper-Scissors game

import random

# Here is the code for a rock-paper-scissors game against the computer:
#    The game should ask for the player to type r for rock, p for paper, s for scissors, or q to quit
#    Then it should choose a random move for the computer
#    Print what the computer did, and who won
#    Print the current score
#    Repeat until the player quits

#    Each function below has one or more bugs, fix them so the game works!
#    The bugs may be syntax errors, one missing line of code, or code that does not do what we want.
#    You only need to make small changes, don't overthink it!

# Read the description of askForMove() carefully, something important is missing from the code!
def askForMove():  
    # askForMove() must 
    #    ask the player for their move
    #    if the player did not type a valid move, keep asking until they do
    #    return 'r', 'p', 's', or 'q'   (whichever the player typed)
    valid_moves = ['r','p','s','q']
    player_move = ""

    # use a loop to keep going until the player types a valid move
    while not player_move in valid_moves:
        print("Will you use rock (r), paper (p), or scissors (s)? Or quit (q)?")
        player_move = str(input())
        if not player_move in valid_moves:
            print("Invalid move! Try again.")
    return player_move

#one line of code has no errors, but doesn't do what we want
def getComputerMove():  
    # the computer can do rock (r), paper (p) or scissors (s)
    # select one at random, then return it
    potential_moves = ['r','p','s']
    actual_move = potential_moves[random.randint(0,2)]
    return actual_move

def resolveMoves(player_move,computer_move):   
    # return 'w' if the player won, 't' in case of a tie, and 'l' if the player lost
    if player_move == 'r' and computer_move == 's':
        return 'w'
    elif player_move == 'p' and computer_move == 'r':
        return 'w'
    elif player_move == 's' and computer_move == 'p':
        return 'w'
    elif player_move == computer_move:
        return 't'
    else:
        return 'l'


# The 'main' function of the game
# This is the starting point for the program
def main():
    #initialize the random number generator so we can randomize the computer move.
    #see random.randint()  in the getComputerMove() function for how we use the random number generator
    random.seed()  

    #we want to keep score!
    player_score = 0
    computer_score = 0

    #use a loop to keep going until the player quits
    should_keep_playing = True
    while should_keep_playing:
        #Pay close attention to how we defined the other 3 functions, and whether they are being used as intended
        player_move = askForMove()

        computer_move = getComputerMove
        print("The computer played",computer_move,".")

        if player_move == 'q':
            should_keep_playing = False  #if the player quit, we should not keep playing
        else:
            result = resolveMoves(computer_move,player_move)
            if result == 'w':
                print("Congratulations, you won!")
                player_score -= 1
            elif  result == 't':
                print("It was a tie!")
            else:
                print("You lost. Dang!")
                computer_score += 1
            print("The current score is: \n\r player -",player_score,"\n\r computer -",computer_score)


# Actually run the main function to start the game
if __name__ == "__main__":
    main()