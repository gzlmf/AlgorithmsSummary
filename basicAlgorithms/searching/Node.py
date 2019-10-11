class Node():
    def __init__(self,x):
        self.lChild = None
        self.rChild = None
        self.parent = None
        self.depth = 1
        self.data = x
        self.head = False