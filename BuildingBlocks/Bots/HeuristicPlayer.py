import random
import Board
import Role
from RandomPlayer import RandomPlayer

class HeuristicPlayer:

    def heuristic_play(self, board, role):
        """
            1 Do Not Lose
            2 Win
        """
        # Closing opponenet's winning moves
        winning_moves = board.get_winning_cells_for(Role.get_opponent(role))
        if len(winning_moves) > 0:
            i, j = random.sample(winning_moves, 1)[0]
            board.set_cell(i, j, role)
            return board
        
        # Choosing a heuristic winnning cell
        winning_moves = board.get_winning_cells_for(role)
        if len(winning_moves) > 0:
            i, j = random.sample(winning_moves, 1)[0]
            board.set_cell(i, j, role)
            return board

        # If there is no heuristc win cell; Random play it.
        randomPlayer = RandomPlayer()
        return randomPlayer.random_move(board, role)



if __name__ == "__main__":
    board = Board.Board()
    player = HeuristicPlayer()
    
    board.board[0][0] = Role.X
    board.board[2][2] = Role.X
    board.board[2][0] = Role.X
    board.show()
    player.heuristic_play(board, Role.O)
    print("\n")
    board.show()
