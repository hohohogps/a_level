class Error(Exception):
    pass
class Command_Not_Recognised(Error):
    pass

def read_f(file):
    with open(file,'r') as f:
        print(f.readlines())

def write_f(file):
    with open(file,'a') as f:
        while True:
            ui = str(input(''))
            if ui != 'out':
                f.write(ui)
            else:
                break

def menu(file):
    while True:
        ui = str(input('read or write? If exit enter exit.')).lower()[0]
            
        if ui == 'r':
            read_f(file)
        elif ui == 'w':
            write_f(file)
        elif ui == 'e':
            break
        else:
            raise Command_Not_Recognised

        

menu('dracula.txt')

