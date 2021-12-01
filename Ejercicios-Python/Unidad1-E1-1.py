num = int(input('Dame un número del 1 al 10: '))
if num <= int(10):
    if num < 6:
            print('F')
    elif num <7:
            print('D')
    elif num <8:
            print('C')
    elif num <9:
            print('B')
    elif num <=10:
            print('A')
else:
    print('No has introducido un número válido')