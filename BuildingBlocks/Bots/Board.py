# I think there is a better way to handel those states
import Role



class Board:
    board = [[Role.NULL,Role.NULL,Role.NULL],
             [Role.NULL,Role.NULL,Role.NULL],
             [Role.NULL,Role.NULL,Role.NULL]]

    def get_empty_cells(self):
        empty_cells = set()
        for i, row in enumerate(self.board):
            for j, _ in enumerate(row):
                if self.board[i][j] == Role.NULL:
                    empty_cells.add( (i, j) )
        return empty_cells

    def set_cell(self, i, j, role):
        self.board[i][j] = role

    def show(self):
        for i in self.board:
            print(i)


