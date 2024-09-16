class Multi_Table:
    def __init__(self,multiplicand=3,up_number=10,list_num = [2,4,6,8,10,12]):
        self.multiplicand = multiplicand
        self.up_number = up_number
        self.list_num = list_num
    try:
        def multiply(self):
            for i in range (1,self.up_number+1):
                print(f'{self.multiplicand} × {i} = {self.multiplicand*i}')
    except TypeError:
        print('Both the multiplicand and up number have.')
        
tom = Multi_Table(2,10)
tom.multiply()