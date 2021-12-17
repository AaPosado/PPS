#En este script utilizamos una variable de un string que le pedimos al usuario,
# y realizamos una comparativa, si la variable que nos ha ofrecido el usuario esta dentro de la lista de vocales,
# imprime por pantalla es una vocal, si no se encuentra, imprime no es una vocal.
letra = str(input('Dame una carácter: '))
if letra in ['a','e','i','o','u']:
    print('Es una vocal')
else:
    print('No es una vocal')