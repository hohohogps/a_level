from math import sqrt, floor

while True:
    num = input('Enter a natural number bigger than 1: ')
    try:
        num = int(num)
        if num > 1:
            break
        else:
            print('Can you read instructions?')
    except ValueError:
        print('Enter an INTEGER bozo')


nums = [True] * (num + 1) 

for i in range(2, floor(sqrt(num)) + 1):
    if nums[i]:  
        for j in range(i * i, num + 1, i):  
            nums[j] = False 

print([i for i in range(2, num + 1) if nums[i]])

