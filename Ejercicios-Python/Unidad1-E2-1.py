#Definimos la función ma
def ma(num1,num2):
    #Comparamos los números, si el primer número es menor al segundo
    if num1 < num2:
        #Imprimimos el segundo número si la condición anterior se comple.
        return num2
    #Si dicha condición no se cumple, imprimimos el primer número.
    else:
        return num1
#Imprimimos por pantalla la función con las dos variables integradas.
print(ma(2,7))