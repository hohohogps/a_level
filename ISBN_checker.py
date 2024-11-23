ISBN = [None]
for i in range (0,13):
    ISBN.append(int(input()))

def check_ISBN(self):
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

 
