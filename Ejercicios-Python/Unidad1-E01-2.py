#Importación de la libreria random, creamos una variable con un numero aleatorio en un rango de 0 a 25,
#explicamos al usuario que el numero esta dentrodel rango de 1 a 25, y su respuesta la guardamos en la variable numerosusuario.
#Si el numerousuario es menor al numero generado decimos que es mayor el numero, si es mayor decimos si es menor y si es igual al numero que ha dado el usuario.
#Felicitamos al usuario por aceptar el acertijo.
import random
numero = random.randrange(25)
condicion = True
while condicion:
    numerousuario = int(input("Vamos a jugar a un juego, estoy pensando en un número del 1 al 25, ¿Eres capaz de adivinarlo? Prueba con un número: "))

    if numerousuario < numero:
        print("El número que estoy pensando es mayor")
    elif numerousuario > numero:
        print("El número que estoy pensando es menor")
    elif numerousuario == numero:
        print("Buenaaa, has dado en el clavo")
        condicion = False
