import random
from Player import Player


class RandomPlayer(Player):

    @staticmethod
    def play(board):
        empty_slots_tuple = board.empty_slots()
        chosen_location = random.choice(empty_slots_tuple)
        return chosen_location
