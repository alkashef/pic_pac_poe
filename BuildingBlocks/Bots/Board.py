# I think there is a better way to handel those states
X = 0
O = 1
NULL = 2

class Board:
    board = [[NULL,NULL,NULL],
             [NULL,NULL,NULL],
             [NULL,NULL,NULL]]

    def get_empty_cells(self):
        empty_cells = set()
        for i, row in enumerate(self.board):
            for j, _ in enumerate(row):
                if self.board[i][j] == NULL:
                    empty_cells.add( (i, j) )
        return empty_cells


