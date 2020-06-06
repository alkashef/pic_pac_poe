import queue
class Node:
    
    def __init__(self,board=None):
        self.board = board
        self.child = []
    def add_child(self,node):
        self.child.append(node)

class Tree:
    
    def __init__(self,root):
        self.root = root
    
    def append(self,board):
        self.root.child.append(board)
    
    def traverseBFS(self,node=None):
        node = self.root if not node else node
        state_count = len(node.child) 
        q = queue.Queue()
        depth = 0
        [q.put(i) for i in node.child]
        while not q.empty():
            node = q.get()
            print(node.board)
            print()
            if node.child :
                depth +=1
            for board in node.child:
                state_count+=1
                q.put(board) 
        return state_count   
    
    def traverseDFS(self,node=None):
        node = self.root if not node else node
        for child in node.child:
            print(self.traverseDFS(child))
        return node.board        
    
    def tree_depth(self,node=None):
        node = self.root if not node else node
        depth = 0
        if not node.child:
            return 1
        for children in node.child: 
            depth = max(depth,self.tree_depth(children))
            return depth+1
        