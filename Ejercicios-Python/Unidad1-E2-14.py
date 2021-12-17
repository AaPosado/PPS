'''Pedimos al usuario que inserte un numero para realizar la conversión.
Definimos una lista a nada.
Realizamos un while del numero que sea mayor/igual que dos.
Insertamos el string al inicio de la lista creada anteriormente y
insertamos el resto de la división. Dividimos el numero entre dos.
Y realizamos el proceso nuevamente, hasta que se cumpla la condición.
Luego recolectamos el ultimo numero que sera 0 o 1 para añadirlo en la primera posición.
Realizamos una imprimición de la lista concatenandolo en un solo string.
'''
numero = int(input("Dame un numero para convertirlo a binario: "))
binario = []
while numero >= 2:
    binario.insert(0,str(numero%2))
    numero = numero//2
binario.insert(0,str(numero))
print("".join(binario))