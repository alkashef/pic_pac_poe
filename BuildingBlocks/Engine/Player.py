from Engine import possibilities


def random_player(board, player):
    # Play turn in sequential order
    selection = possibilities(board)
    current_loc = selection[0]
    board[current_loc] = player
    return board


def human_player(board, player):
    # Play turn using input
    selection = possibilities(board)
    print(f'Your move :{selection}')
    current_loc = eval(input())
    board[current_loc] = player
    return board


def player_dict(board, player, player_type):
    dict_players = {'h': human_player, 'r': random_player}
    return dict_players[player_type](board, player)
