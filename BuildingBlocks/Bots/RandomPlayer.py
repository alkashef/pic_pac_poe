import random
import Board
import Role


class RandomPlayer:

    def random_move(self, board, role):
        emptyCells = board.get_empty_cells()
        i, j = random.sample(emptyCells, 1)[0]
        board.set_cell(i, j, role)
        return board
