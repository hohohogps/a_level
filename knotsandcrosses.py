from time import sleep as s

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


class Computer:
    def __init__(self,difficulty):
        pass

    def move(self):
        pass


def game():

    d = int(input('Dimension.'))
    s(0.5)
    s1 = input('First player symbol')
    s(0.5)
    s2 = input('Second player symbol')
    x = Board(d,True,[s1,s2])

    while True:
        x.display()
        s(0.5)
        i = int(input('Row. Zero indexed.'))
        s(0.5)
        j = int(input('Column. Zero indexed.'))
        s(0.5)

        x.set([i,j],x.curr)
        
        
        if x.win():
            print(f'{x.curr} won.')
            break
        
        elif x.full():
            print('Draw.')
            break
    
        x.curr = x.symbols[x.symbols.index(x.curr)-1]

game()