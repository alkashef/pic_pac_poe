import random
import Board
import Role


class HeuristicPlayer:

    def heuristic_play(self, board, role):
        """
            1 Do Not Lose
            2 Win
        """
        print("Heuristic Play")


if __name__ == "__main__":
    board = Board.Board()
    player = HeuristicPlayer()
    
    board.board[0][0] = 1
    #board.board[0][2] = 1
    board.board[1][1] = 1
    board.board[2][2] = 1
    board.board[2][0] = 1
    board.show()
    board.get_winning_cells_for(Role.O)