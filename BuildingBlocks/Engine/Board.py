import numpy as np


class Board:
    def __init__(self, n=3, empty_slots_mark=-10):
        self.board = np.full((n, n), empty_slots_mark).astype(int)
        self.n = n
        self.empty_slots_mark = empty_slots_mark

    def play_turn(self, chosen_location, mark):
        """

        Args:
            chosen_location (tuple):
            mark (int):

        Returns:

        """
        self.board[chosen_location] = mark

    def empty_slots(self):
        helper = ((np.where(self.board.flatten() == self.empty_slots_mark)[0] / self.n).astype(int),
                  np.where(self.board.flatten() == self.empty_slots_mark)[0].astype(int))
        return list(zip(helper[0], (helper[1] - self.n * helper[0])))

    def game_tie(self):
        if self.board.sum() > 0:
            return 1

    def _horizontal_win(self, player_marks=(0, 1)):
        helper = self.board.sum(1) / self.n
        evaluate = [x for x in helper if x in player_marks]
        if len(evaluate) > 0:
            return evaluate[0]

    def _vertical_win(self, player_marks=(0, 1)):
        helper = self.board.T.sum(1) / self.n
        evaluate = [x for x in helper if x in player_marks]
        if len(evaluate) > 0:
            return evaluate[0]

    def _diagonal_win(self, player_marks=(0, 1)):
        evaluate = self.board.diagonal().sum() / self.n
        if evaluate in player_marks:
            return evaluate

    def _flip_diagonal_win(self, player_marks=(0, 1)):
        evaluate = np.fliplr(self.board).diagonal().sum() / self.n
        if evaluate in player_marks:
            return evaluate

    def game_won(self, player_marks=(0, 1)):
        helper = [self._horizontal_win(self.board), self._vertical_win(self.board),
                  self._diagonal_win(self.board), self._flip_diagonal_win(self.board)]
        evaluate = [x for x in helper if x in player_marks]
        if len(evaluate) > 0:
            return evaluate[0]

    def game_end(self, player):
        """

        Args:
            player (Player): Player that has the current turn

        Returns: int whether the current board game ended or not. And if it ended returns the winning player.

        """
        if self.game_won() == 0:
            return 0
        elif self.game_won() == 1:
            return 1
        elif self.game_tie() == 1:
            return -1
        else:
            return -10
