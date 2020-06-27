import random
from Player import Player


class HumanPlayer(Player):

    @staticmethod
    def play(board):
        empty_slots_tuple = board.empty_slots()
        print(empty_slots_tuple)
        chosen_location = eval(input())
        return chosen_location
