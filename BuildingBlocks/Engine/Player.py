import random


class Player:
    def __init__(self, mark, play_tactic):
        self.mark = mark
        self.play_tactic = play_tactic


    def random_player(board):
        # select random empty position in board
        empty_slots_tuple = board.empty_slots()
        current_loc = random.choice(empty_slots_tuple)
        return current_loc

