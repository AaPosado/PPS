#Definimos la función lon
def lon(pal):
    #Definimos la variable count y el valor que es 0.
    count = 0
    #Realizamos un bucle por cada letra en la cadenade carácteres.
    for a in pal:
        #Por cada letra sumamos 1 al contador.
        count = count + 1
    #Imprimimos por pantalla el contador.
    print(count)
#Llamamos a la función con la variable pal.
lon("hola")