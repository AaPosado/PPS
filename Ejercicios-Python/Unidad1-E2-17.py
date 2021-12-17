#El programa recibe una palabra ingresada por el usuario en su ejecutación. Con una variable contador con valor a 0.
#Bucle para realizar la desccomposición de la palabra. Si alguna de esas letras es igual a la lista de vocales.
#El contador suma 1. Imprimimos el contador.s
palabra = str(input('Dame una palabra: '))
contador = 0
for letra in palabra:
    if letra in ['a','e','i','o','u','A','E','I','O','U']:
        contador += 1
print(contador)
