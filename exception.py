usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    try:
        number = int(usernumber)
    except TypeError:
        print('Number must be an intger.')
    except ValueError:
        print('Number must be int.')
    try:
        print("Welcome", usernames[number], "user number", number,".")
    except IndexError:
        print(f'{number} not in range of usernames.')
    try:
        division = 301 / number
    except ZeroDivisionError:
            print(f'{number} cannot be zero.')
    else:
        print(f"301 divided by {number} = {division}")



while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)
