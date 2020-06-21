# I think there is a better way to handel those states
import Role
import numpy as np



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

    def tanspose(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = self.board[j][i]

    def get_winning_cells_for(self, role):

        # TODO: Generalize the following 2 loops. 
        winning_cells = set()
        for i, row in enumerate(self.board):
            if row.count(role) == 2 and row.count(Role.NULL) == 1:
                j = row.index(Role.NULL)
                winning_cells.add( (i, j) )

        self.tanspose()

        for i, row in enumerate(self.board):
            if row.count(role) == 2 and row.count(Role.NULL) == 1:
                j = row.index(Role.NULL)
                winning_cells.add( (j, i) )

        self.tanspose()

        # TODO: Support diagonals
         
        return winning_cells

