
import sys, os, random, time
pygame_available = False
try:
    import pygame
except:
    pygame_available = False

def idToCoord(tid):
    tid = int(tid)
    for i in range(3):
        for j in range(3):
            if tid == 0:
                return (i,j)
            tid -= 1

def getPCMove(game_state):
    check_spot = [0,2,4,6,8]
    need_to_check = {
        '0':[1,3],
        '2':[1,5],
        '4':[0,1,2,3,5,6,7,8],
        '6':[3,7],
        '8':[5,7]
    }
    spots_coord = []
    player_spot = []
    id = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] == 'X':
                player_spot.append(id)
            id += 1
            spots_coord.append([i,j])
    for s in player_spot:
        if s in check_spot:
            for c in need_to_check[str(s)]:
                if checkSpot(spots_coord[c],game_state):
                    print(s,c)

def getComputerMove(game_state):
    vm =  getValidMoves(game_state)
    for c in vm:
        predict_state = []
        for _ in game_state:
            row = []
            for t in _:
                row.append(t)
                #print(row)
            predict_state.append(row)
        predict_state[c[0]][c[1]] = 'X'
        predict_result = determineResult(predict_state)
        if predict_result == 1 or predict_result == 2:
            return (c[0],c[1])
        print(predict_result)
    return vm[random.randint(0,len(vm)-1)]

def checkSpot(coord,game_state):
    return True if game_state[coord[0]][coord[1]] == 'X' else False

def clearScreen():
    #os.system('cls' if os.name == 'nt' else 'clear')
    pass

def getValidMoves(game_state):
    valid_moves = []
    for row in range(len(game_state)):
        for col in range(len(game_state[0])):
            if game_state[row][col] == " ":
                valid_moves.append((row,col))
    return valid_moves

def move(game_state,pos,symbol):
    if game_state[pos[0]][pos[1]] == " ":
        game_state[pos[0]][pos[1]] = symbol
        return True
    return False

def convertRowsToCols(grid):
    result = []
    for j in range(len(grid[0])):
        new_col = []
        for i in range(len(grid)):
            new_col.append(grid[i][j])
        result.append(new_col)
    return result

GAME_RESULT_XWIN = 1
GAME_RESULT_OWIN = 2
GAME_RESULT_TIE = 0
GAME_RESULT_NONE = -1

PLAYER_ONE_SYMBOL = "X"
PLAYER_TWO_SYMBOL = "O"

def checkForSameSymbol(sym_list):
    if sym_list[0] == PLAYER_ONE_SYMBOL and sym_list[1] == PLAYER_ONE_SYMBOL and sym_list[2] == PLAYER_ONE_SYMBOL:
        return GAME_RESULT_XWIN
    if sym_list[0] == PLAYER_TWO_SYMBOL and sym_list[1] == PLAYER_TWO_SYMBOL and sym_list[2] == PLAYER_TWO_SYMBOL:
        return GAME_RESULT_XWIN
    return GAME_RESULT_NONE

def determineResult(game_state):
    #check rows
    for game_row in game_state:
        result = checkForSameSymbol(game_row)
        if result != GAME_RESULT_NONE:
            return result

    #check columns
    game_state_transpose = convertRowsToCols(game_state)
    for game_col in game_state_transpose:
        result = checkForSameSymbol(game_col)
        if result != GAME_RESULT_NONE:
            return result

    #check diagonals
    diag1 = [game_state[0][0],game_state[1][1],game_state[2][2]]
    diag2 = [game_state[0][2],game_state[1][1],game_state[2][0]]

    diag1_result = checkForSameSymbol(diag1)
    if diag1_result != GAME_RESULT_NONE:
        return diag1_result
    diag2_result = checkForSameSymbol(diag2)
    if diag2_result != GAME_RESULT_NONE:
        return diag2_result

    has_empty = False
    for game_row in game_state:
        for symbol in game_row:
            if symbol == " ":
                has_empty = True
                break
    if not has_empty:
        return GAME_RESULT_TIE
    
    return GAME_RESULT_NONE


GAME_STATE_INITIAL = [[" "," "," "],[" "," "," "],[" "," "," "]]
def printGame(game_state):

    if pygame_available:
        return

    clearScreen()
    # if game_state == GAME_STATE_INITIAL:
    if True:
        print("  0  |  1  |  2")
        print("  -------------")
        print("  3  |  4  |  5")
        print("  -------------")
        print("  6  |  7  |  8\n\n")
    
    for i in range(len(game_state)):
        print("  "+game_state[i][0]+"  |  "+game_state[i][1]+"  |  "+game_state[i][2])
        if i != len(game_state)-1:
            print("  -------------")
    print("")

def squareNumberToIndex(num):
    return (int(num/3),num%3)

def isValidMove(game_state,move):
    valid_moves = getValidMoves(game_state)
    return move in valid_moves

def getPlayerInput(game_state):
    player_input = ""
    input_was_num = True
    square_number = -1
    first_try = True
    valid_move = False 
    move = (-1,-1)

    while not valid_move:
        if not first_try:
            if not input_was_num:
                print("You need to enter a number between 0 and 8")
            if not valid_move:
                print("You need to move in an empty square")

        first_try = False
        input_was_num = True
        player_input = input("Enter the number of the square you want to move in:")
        if player_input == "q":
            sys.exit()
        
        try:
            square_number = int(player_input)
        except ValueError:
            input_was_num = False
        
        if input_was_num:
            move = squareNumberToIndex(square_number)
            valid_move = isValidMove(game_state,move)
        
    
    return move

GAME_MODE_NONE = 0
GAME_MODE_2P = 1
GAME_MODE_AI = 2

def main():
    should_keep_playing = True
    game_state = [[" "," "," "],[" "," "," "],[" "," "," "]]
    current_player = PLAYER_ONE_SYMBOL
    turn_counter = 0
    game_result = GAME_RESULT_NONE
    ai_valid_move = True
    game_mode = GAME_MODE_NONE
    
    while should_keep_playing:

        while game_mode != GAME_MODE_2P and game_mode != GAME_MODE_AI:
            print("Would you like to play against another player (1) or the AI (2)?\n")
            game_mode = int(input())

        if pygame_available:
            return
        else:
            printGame(game_state)

            if not ai_valid_move:
                print("WARNING, WARNING, WARNING")
                time.sleep(1)
                print("Your AI plays tic-tac-toe worse than a blind monkey.")
                print("It tried to move in an invalid location.")
                print("A random move has been selected for it.")
                time.sleep(4)
            ai_valid_move = True

            pos = (-1,-1)

            if game_mode == GAME_MODE_AI:
                if current_player == PLAYER_ONE_SYMBOL:
                    pos = getPlayerInput(game_state)
                else:
                    print("Computer is choosing a move...")
                    time.sleep(1)
                    print("...")
                    time.sleep(1)
                    pos = getComputerMove(game_state)
                    valid_moves = getValidMoves(game_state)
                    if not pos in valid_moves:
                        ai_valid_move = False
                        pos = random.choice(valid_moves)
            else:
                pos = getPlayerInput(game_state)
            
            move(game_state,pos,current_player)

            if current_player == PLAYER_ONE_SYMBOL:
                current_player = PLAYER_TWO_SYMBOL
            else:
                current_player = PLAYER_ONE_SYMBOL
            turn_counter+=1

        game_result = determineResult(game_state)
        
        if game_result != GAME_RESULT_NONE:
            printGame(game_state)
            if game_result == GAME_RESULT_XWIN:
                print(PLAYER_ONE_SYMBOL,"wins!!! It took",turn_counter,"moves.")
            elif game_result == GAME_RESULT_OWIN:
                print(PLAYER_TWO_SYMBOL,"wins!!! It took",turn_counter,"moves.")
            elif game_result == GAME_RESULT_TIE:
                print("It was a tie...")
            
            player_input = input()
            if player_input == "r":
                game_state = [[" "," "," "],[" "," "," "],[" "," "," "]]
                current_player = PLAYER_ONE_SYMBOL
                turn_counter = 0
                game_result = GAME_RESULT_NONE
                ai_valid_move = True
                game_mode = GAME_MODE_NONE
            else:
                should_keep_playing = False


if __name__ == "__main__":
    main()


