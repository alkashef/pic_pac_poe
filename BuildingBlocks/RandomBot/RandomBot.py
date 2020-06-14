import random

X = 0
O = 1
NULL = 2

XOboard = [[NULL,NULL,NULL],
           [NULL,NULL,NULL],
           [NULL,NULL,NULL]]

def get_empty_cells(board):
    empty_cells = set()
    for i, row in enumerate(board):
        for j, _ in enumerate(row):
            if board[i][j] == NULL:
                empty_cells.add( (i, j) )
    return empty_cells


def random_bot(board, role):
    emptyCells = get_empty_cells(board)
    i, j = random.sample(emptyCells, 1)[0]
    board[i][j] = role
    return board
