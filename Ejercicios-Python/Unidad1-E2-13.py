palabra = input("Dame una palabra: ")
contador = 0
for letra in palabra:
    if letra == letra.upper():
        contador += 1
print(contador)
