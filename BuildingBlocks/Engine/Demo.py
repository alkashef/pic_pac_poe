from Game import Game
from RandomPlayer import RandomPlayer

x = Game(p0_class=RandomPlayer,
         p1_class=RandomPlayer,
         starting_player=0)

x.play_game()
