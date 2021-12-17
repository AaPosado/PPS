#Definimos la función biniesto. Si el numero pasado por parametros es divisible entre 4 y ese numero no es divisible entre 100 con resto 0 o
#la division de ese año es dividido por 400 con resto 0 y año dividido entre 100 con resto 0. Es bisiesto. Si la acción anterior no se cumple,
#no es bisiesto.
def bisiesto(año):
    if año%4 == 0 and (año%100 != 0 or (año%400 == 0 and año%100 == 0)):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
bisiesto(2020)
