print('-------Menú-------')
print('1 - Sumar una serie de números')
print('2 - Multiplicar una serie de números')
print('3 - Salir')
sumar = 0
multiplicar = 1
while True:
    usuario = int(input('Por favor introduzca un número del 1 al 3: '))
    numeros = []
    numeros2 = []
    if usuario == 1:
        while True:
            numerosusuario = int(input('Dame los números que deseas sumar: '))
            if numerosusuario == 999:
                for numero in numeros:
                    sumar += numero
                print(sumar)
                break
            else:
                numeros.append(numerosusuario)
    elif usuario == 2:
        while True:
            numerosusuario = int(input('Dame los números que deseas multiplicar: '))
            if numerosusuario == 999:
                print(numeros2)
                for numero in numeros2:
                    print(numero)
                    multiplicar *= numero
                print(multiplicar)
            else:
                numeros2.append(numerosusuario)

    elif usuario == 3:
        break
    else:
        print('Usted no ha introducido un número válido')

