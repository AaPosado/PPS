#Definicion de función mediante una lista ingresada por el usuario en la llamada.
#Definición de variable prueba a nada. Cada vez que se ejecute se volvera a 0/nada.
#Bucle de la lista, donde comparamos el lenght de cada palabra, si la primera palabra es mayor a la segunda,
# la variable prueba se convierte en palabra e imprimimos prueba.
def  mas_larga(lista):
	prueba = ""
	for palabra in lista:
		if len(palabra) > len(prueba):
			prueba = palabra
	print(prueba)
mas_larga(["pepe","juanillo","juanito"])