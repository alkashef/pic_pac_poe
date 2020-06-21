# Adding another searching path
from sys import path
import os

# The current path of the current module.
path_current_module = os.path.dirname(os.path.abspath(__file__))
code_path = os.path.join(path_current_module, '..')
path.append(code_path)


from RandomPlayer import RandomPlayer
from Board import Board
import Role
import unittest


from RandomPlayer import RandomPlayer
from Board import Board
import Role





class Testing_RandomPlayer(unittest.TestCase):

    def test_did_it_play(self):
        player = RandomPlayer()
        board = Board()
        numberOfNullsBeforePlay = len(board.get_empty_cells())
        board = player.random_move(board, Role.X)
        numberOfNullsAfterPlay = len(board.get_empty_cells())
        self.assertEqual(numberOfNullsBeforePlay, numberOfNullsAfterPlay-1)
