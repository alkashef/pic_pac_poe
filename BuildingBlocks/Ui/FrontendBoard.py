class FrontendBoard(object):

    def __init__(self, board, p1_name, p2_name, p1_label, p2_label, turn, first_turn, state):
        self.__board = board
        self.__p1_name = p1_name
        self.__p2_name = p2_name
        self.__p1_label = p1_label
        self.__p2_label = p2_label
        self.__turn = turn
        self.__first_turn = first_turn
        self.__state = state

    def set_board(self, board):
        self.__board = board

    def get_board(self):
        return self.__board

    def set_(self, p1_name):
        self.__p1_name = p1_name

    def get_p1_name(self):
        return self.__p1_name

    def set_p2_name(self, p2_name):
        self.__p2_name = p2_name

    def get_p2_name(self):
        return self.__p2_name

    def set_p1_label(self, p1_label):
        self.__p1_label = p1_label

    def get_p1_label(self):
        return self.__p1_label

    def set_p2_label(self, p2_label):
        self.__p2_label = p2_label

    def get_p2_label(self):
        return self.__p2_label

    def set_turn(self, turn):
        self.__turn = turn

    def get_turn(self):
        return self.__turn

    def set_first_turn(self, first_turn):
        self.__first_turn = first_turn

    def get_first_turn(self):
        return self.__first_turn

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state
