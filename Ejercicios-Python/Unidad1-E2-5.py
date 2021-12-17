#Imprimimos por pantalla un Menú para que sea más visual para el usuario. Declaramos la variables a sumar a 0 y multiplicar a 1,
# realizamos un bucle, para comprobar que el usuario ha ingresado un número del 1 al 3. Si el bucle para que nos introduzca un número y
# tambien definimos dos variables listas números y numeros2. Luego realizamos una comparación, si el usuario ha ingresado 1 hacemos una cosa
#y si el usuario ha insertado 2 realizamos la otra. (Si el usuario ha puesto 3 realizamos un break.).
#Opción1 -> Le pedimos al usuario una lista de números, si desea acabar debe ingresar en la terminal '999', luego realizamos un bucle de esa lista y vamos sumando cada elemento.
#Opción2 -> Le pedimos al usuario una lista de números, si desea acabar debe ingresar en la terminal '999', luego realizamos un bucle de esa lista y vamos multiplicando cada elemento.
#Para finalizar imprimimos por pantalla el resultado.

print('-------Menú-------')
print('1 - Sumar una serie de números')
print('2 - Multiplicar una serie de números')
print('3 - Salir')
sumar = 0
multiplicar = 1
while True:
    usuario = int(input('Por favor introduzca un número del 1 al 3: '))
    numeros = []
    numeros2 = []
    if usuario == 1:
        while True:
            numerosusuario = int(input('Dame los números que deseas sumar: '))
            if numerosusuario == 999:
                for numero in numeros:
                    sumar += numero
                print(sumar)
                break
            else:
                numeros.append(numerosusuario)
    elif usuario == 2:
        while True:
            numerosusuario = int(input('Dame los números que deseas multiplicar: '))
            if numerosusuario == 999:
                print(numeros2)
                for numero in numeros2:
                    print(numero)
                    multiplicar *= numero
                print(multiplicar)
            else:
                numeros2.append(numerosusuario)
    elif usuario == 3:
        break
    else:
        print('Usted no ha introducido un número válido')

