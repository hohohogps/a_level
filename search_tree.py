class Tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def in_order(self):
        def traverse(node_index, result):
            if node_index == -1:
                return None
            traverse(self.left[node_index], result)
            result.append(self.data[node_index])
            traverse(self.right[node_index], result)

        result = []
        traverse(0, result)
        return result
    
    def post_order(self):
        def traverse(node_index, result):
            if node_index == -1:
                return None
            traverse(self.left[node_index], result)
            traverse(self.right[node_index], result)
            result.append(self.data[node_index])

        result = []
        traverse(0, result)
        return result

    def pre_order(self):
        def traverse(node_index, result):
            if node_index == -1:
                return None
            result.append(self.data[node_index])
            traverse(self.left[node_index], result)
            traverse(self.right[node_index], result)

        result = []
        traverse(0, result)
        return result
            

d = ['PJ', 'AP', 'RG', 'AJ', 'CK', 'SF', 'RA']
l = [1, 3, -1, -1, -1, 6, -1]
r = [2, 4, 5, -1, -1, -1, -1]

t = Tree(d, l, r)
print(t.in_order())
print(t.post_order())
print(t.pre_order())
