from Game import Game
from RandomPlayer import RandomPlayer
from HumanPlayer import HumanPlayer

x = Game(p0_class=HumanPlayer,
         p1_class=RandomPlayer,
         starting_player=0)

x.play_game()
