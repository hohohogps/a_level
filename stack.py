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
        if self.hnode != None:
            v = self.hnode.data 
            self.hnode = self.hnode.nnode
            self.size -= 1
            return v
        else:
            return None
        
    def __push__(self,d):
       node = Node(data=d)
       node.nnode = self.hnode
       self.hnode = node
       self.size += 1

    def __len__(self): 
        return self.size
    
    def __str__(self):
        s = ''
        n = self.hnode
        while n != None:
            s += str(n.data)
            n = n.nnode
        return s[::-1]

stack = Stack()
stack.__push__('a')
stack.__push__('b')
stack.__push__('c')
print(stack.__str__())