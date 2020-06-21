from Game import Game
from RandomPlayer import RandomPlayer

x = Game(p1_type=RandomPlayer,
         p2_type=RandomPlayer,
         p1_mark="x",
         p2_mark="o",
         p1_name="Mahdy",
         p2_name="Moemen",
         empty_slots_mark=" ")

x.play_game()
