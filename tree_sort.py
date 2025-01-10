class Node:

    def __init__(self, value: str):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value:str):
        if value < self.value:
                
            if self.left == None:
                self.left = Node(value)
                
            else:
                self.left.insert(value)
        else:
                            
            if self.right == None:
                self.right = Node(value)
                
            else:
                self.right.insert(value)

    def display(self):

        if self.left:
            self.left.display()

        print(self.value)

        if self.right:
            self.right.display()


root = Node('this')
root.insert('is')
root.insert('a')
root.insert('test')
root.display()