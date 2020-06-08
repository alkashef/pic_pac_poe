# Tic-Tac-Toe Game 

# importing all necessary libraries 
import numpy as np 
import random 
from time import sleep 

# Creates an empty board 
def create_board(): 
    return np.zeros((3,3)).astype(int)

# Empty slots vector of tuples
def possibilities (board):
    a = (((np.where(board.flatten()==0)[0]/3)).astype(int) , np.where(board.flatten()==0)[0].astype(int))
    return list(zip(a[0], (a[1] - 3*a[0])))


# function wraps players to be changed to a class
def player_dict(board , player , player_type ):
    
    # Play turn randomly
    def random_player(board, player): 
        selection = possibilities(board)
        current_loc = random.choice(selection)
        board[current_loc] = player 
        return board 

    # Play turn using input
    def human_player(board, player): 
        selection = possibilities(board)
        print(f'Your move :{selection}')
        current_loc = eval(input())
        board[current_loc] = player 
        return board 
    
    dict_players  = {'h' : human_player , 'r' : random_player }
    return dict_players[player_type](board, player)
    
# Evaluates whether there is  win or a tie 
def evaluate_tial(test_board):
    vertical_min = np.min(test_board, axis=0)
    vertical_max = np.max(test_board, axis=0)
    horizontal_min = np.min(test_board, axis=1)
    horizontal_max = np.max(test_board, axis=1)
    diagonal_min = np.min(np.diagonal(test_board), axis=0)
    diagonal_max = np.max(np.diagonal(test_board), axis=0)
    diagonal_mirror_min = np.min(np.diagonal(np.fliplr(test_board)), axis=0)
    diagonal_mirror_max = np.max(np.diagonal(np.fliplr(test_board)), axis=0)

    vertical_result = vertical_min[np.where(vertical_min==vertical_max)]
    horizontal_result = horizontal_min[np.where(horizontal_min==horizontal_max)]

    if vertical_result.size > 0 :
        return vertical_result[0]

    if horizontal_result.size > 0 :
        return horizontal_result[0]

    if diagonal_min == diagonal_max:
        return diagonal_min

    if diagonal_mirror_min == diagonal_mirror_max:
        return diagonal_mirror_min
    
    if test_board.flatten()[np.where(test_board.flatten()!=0)].size == 9:
        return(-1)

    return 0

# Main function to play one game 
def play_game(player_type_dict): 
    board, winner, counter = create_board(), 0, 1
    while winner == 0 :
        for player in [1, 2]:
            board = player_dict (board , player , player_type_dict[player])
            
            counter += 1
            winner = evaluate_tial(board)
            print("Board after " + str(counter-1) + " move")
            print(board)
            if winner in (player,-1) : 
                break
    return(winner)