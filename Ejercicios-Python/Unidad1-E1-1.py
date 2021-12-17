#Pedimos a un usuario un número del 1 al 10, nos aseguramos que es un entero y lo añadimos a la variable num.
num = int(input('Dame un número del 1 al 10: '))
#Comparamos si el número es menor que 11.
if num <= int(10):
    #Si el numero es de 0 al 5 imprimimos por pantalla 'F'.
    if num < 6:
            print('F')
    # Si el numero es 6 imprimimos por pantalla 'D'.
    elif num <7:
            print('D')
    # Si el numero es de 7 imprimimos por pantalla 'C'.
    elif num <8:
            print('C')
    # Si el numero es de 8 imprimimos por pantalla 'B'.
    elif num <9:
            print('B')
    # Si el numero es de 9 o 10 imprimimos por pantalla 'A'.
    elif num <=10:
            print('A')
#Si el numero es mayor igual a 11, imprimimos por pantalla que no ha introducido un número válido.
else:
    print('No has introducido un número válido')