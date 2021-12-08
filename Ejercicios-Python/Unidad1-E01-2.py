import random
numero = random.randrange(25)
condicion = True
while condicion:
    print(numero)
    numerousuario = int(input("Vamos a jugar a un juego, estoy pensando en un número del 1 al 25, ¿Eres capaz de adivinarlo? Prueba con un número: "))

    if numerousuario < numero:
        print("El número que estoy pensando es mayor")
    elif numerousuario > numero:
        print("El número que estoy pensando es menor")
    elif numerousuario == numero:
        print("Buenaaa, has dado en el clavo")
        condicion = False
