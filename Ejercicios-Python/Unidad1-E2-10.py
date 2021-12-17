'''
Definimos la función max_in_list, donde vamos a pedir al usuario
que inserte una serie de numeros separados por espacios, vamos a añadir la variable numeros,
con un splint (separador de campos (que sera el espacio)).
Declaramos la variable a 0. Realizamos un bucle por cada numero en la lista,
y realizamos la comparación de numeros, si numero es mayor a vairable,
variable pasa a valer numero, realizamos un return y un print para imprimir por pantalla.


'''
def max_in_list():
    lista = input("Dame los números que deseas insertar en la lista, por separación de espacios: ")
    numeros = lista.split(" ")
    variable = 0
    for numero in numeros:
        if int(numero) > variable:
            variable = int(numero)
    return (variable)
print(max_in_list())