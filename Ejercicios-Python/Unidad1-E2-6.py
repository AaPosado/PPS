#Definimos una funcion llamada reves si ningun parametro, pedimos al usuario una palabra y
#luego igualamos la palabra a palabra -1 que va a mirar letra por letra hacia detras.
#Imprimimos la palabra. (Tambien se puede realizar sacando el input y accediendo a la palabra por parametros.)
def reves():
    palabra = input("Dame una palabra: ")
    palabra = palabra[::-1]
    print(palabra)
reves()