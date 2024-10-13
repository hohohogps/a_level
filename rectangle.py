import math

class Shape:
    
    coord_vector_space = 'R^2'
    dim = 2

    def __init__(self, colour = 'white', area = 0, shape = ''):
        self.colour = colour
        self.area = area
        self.shape = shape
    

    def enlargment(self, determinant):
        self.area *= determinant
    
    @classmethod
    def change_dim(cls, new_dim):
        cls.dim = new_dim
        cls.coord_vector_space = 'R'+'^'+str(cls.dim)

class Rectangle(Shape):

    def __init__(self,right_angle = True, width = 0, height = 0):
        super().__init__()
        self.right_angle = True
        self.width = width
        self.height = height
        self.diagonal = math.sqrt(self.width^2+self.height^2)
        self.square = width == height
        self.area = width*height
r = Rectangle(width = 10, height = 10)
print(r.square)