import numpy as np
from Player import Player
from Board import Board
from time import sleep


class Game:
    def __init__(self, p0_class, p1_class, p0_name='0', p1_name='1', n=3, starting_player=0):
        self.Board = Board(n, -10)
        self.player_0 = p0_class(0, p0_name)
        self.player_1 = p1_class(1, p1_name)
        self.round_number = 0
        self.winner = -10
        self.player_turn = starting_player

    def current_turn(self):
        """

        Returns: Player with the current turn

        """
        player_dictionary = {0: self.player_0, 1: self.player_1}
        if self.round_number > 1:
            self.player_turn = abs(self.player_turn - 1)
        return player_dictionary[self.player_turn]

    def print_game(self):
        print(self.player_turn)
        print(self.round_number)
        print(self.Board.board)

    def play_game(self):
        """

        This function is responsible for playing the game

        """
        while self.winner == -10:
            sleep(1)
            self.round_number += 1
            player_in_turn = self.current_turn()
            play = player_in_turn.play_tactic(self.Board)
            self.Board.play_turn(play, player_in_turn.mark)
            self.winner = self.Board.game_end()
            self.print_game()
        print(self.winner)
