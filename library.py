from datetime import date

class Stock_Item:

    library = 'Abingdon library'

    def __init__(self,title=None,loan=False,date=date.today()):
        self.title = title
        self.loan = loan
        self.date = date

    @classmethod
    def change_libary(cls,s):
        cls.library = s

    def setloan(self):
        super.setloan()
    
    def returnloan(self):
        super.returnloan()


class Book(Stock_Item):

    def __init__(self,title,loan,date,author=None,ISBN=None):
        super().__init__(title,loan,date)
        self.author = author
        self.ISBN = ISBN

    def display(self):
        print(f'{self.title}\n{self.author}\n{self.ISBN}\n{self.loan}\n{self.date}')

    def check_ISBN(self):
        ISBN = [None] + list(str(self.ISBN))
    
        CalculatedDigit = 0
        Count = 1 

        while Count < 13:
            CalculatedDigit += ISBN[Count]
            Count += 1 
            CalculatedDigit += ISBN[Count]*3
            Count += 1

        while CalculatedDigit >= 10:
            CalculatedDigit -= 10

        CalculatedDigit = 10 - CalculatedDigit

        if CalculatedDigit == 10:
            CalculatedDigit = 0

        if CalculatedDigit == ISBN[13]:
            print('Valid ISBN')
        else:
            print('Invalid ISBN')

class CD(Stock_Item):

    def __init__(self,title=None,loan=False,date=None,artist=None,type=None):
        super().__init__(title,loan,date)
        self.artist = artist
        self.type = type

    

hp = Book('Harry Potter',False,date.today(),'Rowling',9781510405196)
hp.check_ISBN()
