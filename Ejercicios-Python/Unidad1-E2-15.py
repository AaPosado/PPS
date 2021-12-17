#Definimos una tupla con varios numeros del 1 al 100. Definimos un contador con valor a 0. Realizamos un bucle por cada valor,
#si el valor es mayor a 20 sumamos uno al contador, si no es mayor a 20 no realizamos ninguna acción.
#Consecutivamente con todos los valores de la tupla. Para finalizar imprimimos la variable contador.
tupla = (2,4,8,34,24,12,46,43,21,67)
contador = 0
for numero in tupla:
    if numero >= 20:
        contador += 1
print(contador)