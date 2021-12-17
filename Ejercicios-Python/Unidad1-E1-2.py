#Realizamos dos inputs de enteros para que el usuario inserte dos numeros, los añadimos a la variable num1 y num2.
num1 = int(input('Dame un primer número: '))
num2 = int(input('Dame un segundo número: '))
#Realizamos la comparación de números, si el primer número que ha añadido el usuario es menor que el segundo.
if num1 < num2:
    #Imprimimos por pantalla que el número mayor es el segundo.
    print('El número mayor es:' , num2 , '(Número 2)')
else:
    # Imprimimos por pantalla que el número mayor es el primero.
    print('El número mayor es:' , num1 , '(Número 1)')