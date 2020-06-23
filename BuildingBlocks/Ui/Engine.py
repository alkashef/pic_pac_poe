import FrontendBoard

import numpy as np


class Engine(object):

    def __init__(self):
        pass

    def start_game(self):
        board = np.full((3, 3), -10)
        p1_name = "ayouya"
        p2_name = "ahmoda"
        p1_label = 1
        p2_label = 0
        turn = 0
        first_turn = 0
        state = 0
        game_board = FrontendBoard.FrontendBoard(board, p1_name, p2_name, p1_label, p2_label, turn, first_turn, state)
        return game_board
