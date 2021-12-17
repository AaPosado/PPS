#Definicion de dos listas(lista1,lista2), creación de bucle for, busqueda de los nombres de la lista1
#y busqueda de los nomnrbes de la lista dos, si el nombre coincide con alguno de la segunda lista,
#imprime por pantall "True, el nombre que coincide es: $NOMBRE", si no coincide, imprime por pantalla "False"
#Llamada de la función mediante parametros, donde tendremos que indicar que nombres estan en las listas.
def iguales(lista1,lista2):
    for nombres in lista1:
        for nombre in lista2:
            if nombres == nombre:
                print("True, el nombre que coincide es: " + nombre)
            else:
                print("False")
    print(lista1==lista2)
iguales(["Pepe","Juan"],["Juan","Nerea"])