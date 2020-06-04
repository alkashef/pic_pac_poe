import random

"""
0  -> x
1  -> o
2 -> empty
"""

XOboard = [[2,2,2],
           [2,2,2],
           [2,2,2]]

def get_empty_cells(board):
    pass


def random_bot(board, role):
    """
        role: belongs to {1, 0, 2}
    """
    emptyCells = get_empty_cells(board)
    x, y = random.randint(0, len(emptyCells)-1)
    board[x][y] = role
    return board
