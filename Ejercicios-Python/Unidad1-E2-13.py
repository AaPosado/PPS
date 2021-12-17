#Programa dedicado al contador de mayusculas en una frase o palabra.
#Pedimos al usuario que ingrese algún texto.
#Definimos la variable contador a 0. Realizamos un bucle por cada letra de ese texto.
#Si la letra es upper (Mayus), suma 1 al contador. Para finalizar Imprimimos contador.
palabra = input("Dame una palabra: ")
contador = 0
for letra in palabra:
    if letra == letra.upper():
        contador += 1
print(contador)
