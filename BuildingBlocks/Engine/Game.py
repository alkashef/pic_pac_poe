import numpy as np
from Player import Player
from Board import Board
from time import sleep


class Game:
    def __init__(self, p1_type, p2_type, p1_mark='0', p2_mark='1',
                 p1_name='0', p2_name='1', n=3, empty_slots_mark='-10'):
        self.Board = Board(n, -10)
        self.winner = -1
        self.player_turn = 0
        self.player_1 = p1_type(0, p1_name)
        self.player_2 = p2_type(1, p2_name)
        self.p1_mark = p1_mark
        self.p2_mark = p2_mark
        self.empty_slots_mark = empty_slots_mark
        self.round_number = 0

    def change_turn(self):
        """

        Returns: Player with the current turn

        """
        player_dictionary = {0: self.player_1, 1: self.player_2}
        self.player_turn = abs(self.player_turn - 1)
        return player_dictionary[self.player_turn]

    def print_game(self, player):
        """

        Args:
            player (Player): Player that has the current turn

        Returns: Prints the board using the required tics and empty slots filling

        """
        print(f'round {self.round_number}')
        print(f'Its is player { player.name } turn')
        visualisation_board = self.Board.board.astype(str)
        visualisation_board[visualisation_board == '0'] = str(self.p1_mark)
        visualisation_board[visualisation_board == '1'] = str(self.p2_mark)
        visualisation_board[visualisation_board == '-10'] = str(self.empty_slots_mark)
        print(visualisation_board)

    def play_game(self):
        """

        This function is responsible for playing the game

        """
        player_in_turn = self.player_1
        while self.Board.game_end() == -10:
            sleep(1)
            self.round_number += 1
            player_in_turn = self.change_turn()
            play = player_in_turn.play_tactic(self.Board)
            self.Board.play_turn(play, player_in_turn.mark)
            self.print_game(player_in_turn)

