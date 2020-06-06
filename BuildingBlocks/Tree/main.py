from Tree import Node , Tree
from copy import deepcopy         

def ifLeaf(board,i,j):
    '''
        To check if its leaf node 
        1 - If Its empty cell then it's not a leaf node
        2 - Checking for all possible positions of winning 
    '''
    if board[i][j] == -10:
        return False
    dimension = len(board)
    count = 1
    #Checking Horizontally
    for x in range(1,dimension):
        if board[i][j] == board[((i+x)%dimension)][j]:
            count+=1
    if count == dimension :
        return True
    count = 1
    #Checking Verticality
    for x in range(1,dimension):
        if board[i][j] == board[i][((j+x)%dimension)]:
            count+=1
    if count == dimension :
        return True
    count = 1
    #Checking diagonally
    for x in range(1,dimension):
        if board[i][j] == board[((i+x)%dimension)][((j+x)%dimension)]:
            count+=1
    if count == dimension :
        return True
    count = 1
    #Checking the opposite diagonal
    for x in range(1,dimension):
        if board[i][j] == board[((i+x)%dimension)][((j-x)%dimension)]:
            count+=1
    if count == dimension :
        return True
    return False
    
# Using Backtracking technique to build up the tree branch by branch
def traverse(board,turn,i=None,j=None):
    if ifLeaf(board,i,j):
        return Node(deepcopy(board))
    length = len(board)
    node = Node(deepcopy(board))
    for i in range(length):
        for j in range(length):
            if board[i][j] == -10:
                board[i][j] = turn
                turn = 0 if turn == 1 else 1
                node.add_child(traverse(board,turn,i,j))
                board[i][j] = -10
                turn = 0 if turn == 1 else 1
    return node

#Just for making board more readable
def printMatrix(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j],end=" ")
        print()

board = [[-10,-10,-10],[-10,-10,-10],[-10,-10,-10]]
root_node = traverse(board,1,0,0)
root = Tree(root_node)
#print(root.traverseBFS())
#root.traverseDFS()
#root.tree_depth()