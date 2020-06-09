import numpy as np


def create_board():
    # Creates an empty board
    return np.zeros((3, 3)).astype(int)


def possibilities(board):
    # Empty slots vector of tuples
    a = (((np.where(board.flatten() == 0)[0]/3)).astype(int),
         np.where(board.flatten() == 0)[0].astype(int))
    return list(zip(a[0], (a[1] - 3*a[0])))


def evaluate_tial(test_board):
    # Evaluates whether there is  win or a tie
    vertical_min = np.min(test_board, axis=0)
    vertical_max = np.max(test_board, axis=0)
    horizontal_min = np.min(test_board, axis=1)
    horizontal_max = np.max(test_board, axis=1)
    diagonal_min = np.min(np.diagonal(test_board), axis=0)
    diagonal_max = np.max(np.diagonal(test_board), axis=0)
    diagonal_mirror_min = np.min(np.diagonal(np.fliplr(test_board)), axis=0)
    diagonal_mirror_max = np.max(np.diagonal(np.fliplr(test_board)), axis=0)
    vertical_result = vertical_min[np.where(vertical_min == vertical_max)]
    horizontal_result = horizontal_min[np.where(
            horizontal_min == horizontal_max)]
    if vertical_result.size > 0:
        return vertical_result[0]
    if horizontal_result.size > 0:
        return horizontal_result[0]
    if diagonal_min == diagonal_max:
        return diagonal_min
    if diagonal_mirror_min == diagonal_mirror_max:
        return diagonal_mirror_min
    if test_board.flatten()[np.where(test_board.flatten() != 0)].size == 9:
        return(-1)
    return 0
