name_list = ['Ryansh', 'Oliver', 'Edward', 'Daniel', 'Alex', 'Ares', 'Thomas', 'Andy', 'Charlie', 'Ryan', 'Lucas']
number = []

for i in range(3):
    name = input("Type in a name: ")
    name_list.append(name)
print(name_list)
print(name_list[2])
print(name_list[-7:])

for i in range(5):
    num = input("Type in a number: ")
    number.append(float(num))
number.sort()
print(number[-1],number[0],sum(number),sum(number)/len(number))

