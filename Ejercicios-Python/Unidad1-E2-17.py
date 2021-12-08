palabra = str(input('Dame una palabra: '))
contador = 0
for letra in palabra:
    if letra in ['a','e','i','o','u']:
        contador += 1
print(contador)
