import math

class Vector:
    
    global d
    d = 2

    def __init__(self):
        self.vec = [0]*d
        self.mag = 0
    
    def __setvec__(self,i,value):
        self.vec [i-1] = value

    def __calmag__(self):
        self.mag = math.sqrt(sum([i**2 for i in self.vec]))
    
    def __add__(self,next):
        if len(self.vec) != len(next.vec):
            raise ValueError('Vectors must be in the same vector space (same dim).')
        else:
            final = Vector()
            for i in range (len(self.vec)):
                final.vec[i] = self.vec[i] + next.vec[i]
            return final
    
    def __dot__(self,next):
        if len(self.vec) != len(next.vec):
            raise ValueError('Vectors must be in the same vector space (same dim).')
        else:
            value = 0
            for i in range (len(self.vec)):
                value += self.vec[i]*next.vec[i]
            return value
        
    def __cross__(self,next):
        pass 
    #will think of how to implement this

A = Vector()
print(A.vec)
A.__setvec__(1,0)
A.__setvec__(2,1)
print(A.vec)
B = Vector()
print(B.__add__(A).vec)
A.__calmag__()
print(A.mag)
        