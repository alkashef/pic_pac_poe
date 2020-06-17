import numpy as np
from Player import Player
from Board import Board
from time import sleep

class Game:
    def __init__(self, p1_play_tactic, p2_play_tactic, p1_mark=0, p2_mark=1 , p1_name = 0, p2_name = 1 , n=3, empty_slots_mark=-10):
        self.Board = Board(n, -10)
        self.winner = -1
        self.player_turn = 0
        self.player_1 = Player(0, p1_play_tactic , p1_name)
        self.player_2 = Player(1, p2_play_tactic , p2_name)
        self.p1_mark = p1_mark
        self.p2_mark = p2_mark
        self.empty_slots_mark = empty_slots_mark
        self.round_number = 0

    def change_turn(self):
        player_dictionary = {0: self.player_1 , 1 : self.player_2}
        self.player_turn = abs(self.player_turn - 1)
        return player_dictionary[self.player_turn]

    def print_game(self ,Player):
        print(f'round {self.round_number}')
        print(f'Its is player { Player.name } turn')
        x = self.Board.board.astype(str)
        x[x == '0'] = str(self.p1_mark)
        x[x == '1'] = str(self.p2_mark)
        x[x == '-10'] = str(self.empty_slots_mark)
        print(x)

    def game_end(self , Player):
        if self.Board.game_won() in (1,0):
            print(f'player {Player.name} won the game')
            return 1
        elif self.Board.game_tie() == 1:
            print(f'game is a tie')
            return 1
        else:
            return 0


    def play_game(self):
        player_in_turn = self.player_1
        while self.game_end(player_in_turn) == 0:
            sleep(1)
            self.round_number += 1
            player_in_turn = self.change_turn()
            play = player_in_turn.play_tactic(self.Board)
            self.Board.play_turn(play, player_in_turn.mark)
            self.print_game(player_in_turn, self.Board)


x = Game(p1_play_tactic=Player.random_player
         , p2_play_tactic=Player.random_player
         , n=3
         , p1_mark="m"
         , p2_mark="a"
         , p1_name= "mohamed"
         , p2_name= "ahmed"
         , empty_slots_mark=" "
         )
x.play_game()
