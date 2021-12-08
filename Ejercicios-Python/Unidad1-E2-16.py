nombres = ['Abel', 'Pepe', 'Antonio', 'Helena', 'Elena']
letrausuario = str(input("Que letra deseas buscar:"))
letrausuarioma = letrausuario.upper()
for nombre in nombres:
    for letra in nombre:
            if letra == letrausuarioma:
                print(nombre)
                break
