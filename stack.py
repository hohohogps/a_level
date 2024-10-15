class Node:
    def __init__(self, data=None, nnode=None):
        self.data = data
        self.nnode = nnode
    
    def __getdata__(self):
        return self.data
    
    def __setnnode__(self,node):
        self.nnode = node

class Stack:
    def __init__(self, hnode=None, size=0):
        self.hnode = hnode
        self.size = size

    def __pop__(self):
        v = self.hnode.data 
        self.hnode = self.hnode.nnode
        self.size -= 1
        return v
    
    def __push__(self,d):
       node = Node(data=d)
       node.nnode = self.hnode
       self.hnode = node
       self.size += 1

    def __size__(self): 
        return self.size
    

stack = Stack()
stack.__push__(234)
stack.__push__(345)
print(stack.hnode.data)
print(stack.hnode.nnode.data)