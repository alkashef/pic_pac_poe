from Engine import create_board, evaluate_tial
from Player import player_dict


def play_game(player_type_dict):
    # Main function to play one game
    board, winner, counter = create_board(), -10, 1
    while winner == -10:
        for player in [1, 2]:
            board = player_dict(board, player, player_type_dict[player])
            winner = evaluate_tial(board)
            print("Board after " + str(counter) + " move")
            print(board)
            counter += 1
            if winner in (player, -1):
                break
    return(winner)
