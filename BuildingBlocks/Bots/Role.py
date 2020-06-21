X = 0
O = 1
NULL = 2

def get_opponent(given):
    if given == X:
        return O
    if given == O:
        return X
    else:
        raise "Given Must be Role.X or Role.O"