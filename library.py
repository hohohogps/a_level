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

class CD(Stock_Item):

    def __init__(self,title=None,loan=False,date=date.today(),artist=None,type=None):
        super().__init__(title,loan,date)
        self.artist = artist
        self.type = type


hp = Book('Harry Potter',False,date.today(),'Rowling',None)
hp.display()
