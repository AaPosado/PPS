#Definimos la función max3 con 3 parametros.
def max3(num1,num2,num3):
    #Empezamos la comparación. Si el número mayor de los tres es el 1.
    if num1 > num2 and num1 > num3:
        #Realizamos la comparación de los dos números restantes.
        if num2 > num3:
            #Realizamos el return del número 1 es mayor que el número 2. Y el número 2 es mayor al número 3.
            return num1,num2,num3
        else:
            #Si el número dos no es mayor al 3. El número 1 es el mayor, a continuación el número 3 y para finalizar el número 2.
            return num1,num3,num2
    #Si el número mayor de los tres es el 2.
    elif num2 > num1 and num2 > num3:
        #Realizamos la comparación de los dos números restantes.
        if num1 > num3:
            #Realizamos el return del número 2 es mayor que el número 1. Y el número 1 es mayor al número 3.
            return num2,num1,num3
        else:
            #Si el número 1 no es mayor al 3. El número 2 es el mayor, a continuación el número 3 y para finalizar el número 1.
            return num2,num3,num1
    # Si el número mayor de los tres es el 3.
    elif num3 > num1 and num3 > num2:
        #Realizamos la comparación de los dos números restantes.
        if num1 > num2:
            #Realizamos el return del número 3 es mayor que el número 1. Y el número 1 es mayor al número 2.
            return num3,num1,num2
        else:
            #Si el número 1 no es mayor al 2. El número 3 es el mayor, a continuación el número 2 y para finalizar el número 1.
            return num3,num2,num1
#Imprimimos por pantalla la función con los números como parámetros.
print(max3(5,8,40))