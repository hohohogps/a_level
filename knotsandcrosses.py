from time import sleep as s
import random as r

class Error(Exception):
    pass
class CoordsOccupiedError(Error):
    pass
class SymbolDoesNotExistError(Error):
    pass
class CoordsDoesNotExistError(Error):
    pass


class Board:
    def __init__(self, dim=3, human=True, symbols=['O','X']):
        self.dim = dim
        self.human = human
        self.symbols = symbols
        self.list = [[None]*dim for n in range (dim)]
        self.curr = symbols[0]

    def display(self):
        for i in self.list:
            print(i)

    def set(self,coords,symbol):
        if (coords[0]<self.dim) and (coords[1]<self.dim) == False:
            print('Coords does not exist.')
            raise CoordsDoesNotExistError 
        if self.list[coords[0]][coords[1]] != None:
            print('Coords are occupied.')
            raise CoordsOccupiedError
        if symbol not in self.symbols:
            print('Symbols do not exist.')
            raise SymbolDoesNotExistError
        else:
            self.list[coords[0]][coords[1]] = symbol

    def win(self):
        for row in self.list:
            if row[0] is not None and all(symbol == row[0] for symbol in row):
                return True

        for col in range(self.dim):
            if self.list[0][col] is not None and all(self.list[row][col] == self.list[0][col] for row in range(self.dim)):
                return True

        if self.list[0][0] is not None and all(self.list[i][i] == self.list[0][0] for i in range(self.dim)):
            return True

        if self.list[0][self.dim - 1] is not None and all(
            self.list[i][self.dim - 1 - i] == self.list[0][self.dim - 1] for i in range(self.dim)
        ):
            return True

        return False

    def full(self):
        for i in self.list:
            for j in i:
                if j == None:
                    return False
        return True
    
    def available(self):
        #O(n^2)
        result = []
        for i in self.list:
            for j in self.list:
                if j != None:
                    result.append([i,j])
        return result

class Computer:
    def __init__(self,board):
        self.board = board

    def move(self):
        available = self.board.available()
        curr = self.board.curr
        y = self.board

        for i in available:
            y.set(i,y.curr)
            if y.win():
                return i
            y = self.board()
        
        return r.choice(available)
        
        
def procedure(I,board):
    board.set(I,board.curr)
           
    if board.win():
        print(f'{board.curr} won.')
        return True
    
    elif board.full():
        print('Draw.')
        return True
        
    else:
        return False
    board.curr = board.symbols[board.symbols.index(board.curr)-1]


def game():

    d = int(input('Dimension.'))
    s(0.5)
    s1 = input('First player symbol')
    s(0.5)
    s2 = input('Second player symbol')
    x = Board(d,True,[s1,s2])
    human = input('True or False?').lower()
    if human != 'true':
        c = Computer(x)

    while True:

        x.display()
        s(0.5)
        i = int(input('Row. Zero indexed.'))
        s(0.5)
        j = int(input('Column. Zero indexed.'))
        s(0.5)
        
        I = [i,j]
        
        procedure(I,x)
        if procedure:
            break

        if human != 'true':
            procedure(c.move,x)
            if procedure:
                break
game()