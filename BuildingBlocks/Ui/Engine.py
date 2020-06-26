import FrontendBoard

import numpy as np


class Engine(object):

    def __init__(self):
        self.game_board = None

    def start_game(self):
        board = np.full((3, 3), -10)
        p1_name = "Player 1"
        p2_name = "Player 2"
        p1_label = 1
        p2_label = 0
        turn = 0
        first_turn = 0
        state = 0
        self.game_board = FrontendBoard.FrontendBoard(board, p1_name, p2_name, p1_label, p2_label, turn, first_turn,
                                                      state)
        return self.game_board

    def get_game(self):
        return self.game_board

    def update_board(self, i, j):
        b = self.game_board.get_board()
        b[i, j] = 1
        self.game_board.set_board = b

