'''Definimos la función filtrar_palabras, creamos la lista con valor nulo
realizamos un bucle por cada elemento en la lista, si la
longitud del elemento es mayor a numero(que es un
parametro que tenemos que añadir al llamar a la función,
luego imprimimos por pantalla con return la lista1)'''
def filtrar_palabras(lista,numero):
    lista1 = []
    for elemento in lista:
        if len(elemento) > numero:
            lista1.append(elemento)
    return (lista1)
print(filtrar_palabras(["Hello", "Bonjour", "Hallo", "Hola", "Que paza pisha"],5))