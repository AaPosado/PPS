#Realizamos una lista con varios nombres de personas. Pedimos una animación al usuario para que nos diga que nombre quiere buscar.
#Recogemos esa información proporcionada por el usuario. Pasamos esa información en mayuscula a una variable letrausuarioma.
#Por cada nombre realizamos una descomposición y si la primera letra es igual a la proporcionada por el usuario. Imprimimos el nombre.
nombres = ['Abel', 'Pepe', 'Antonio', 'Helena', 'Elena']
letrausuario = str(input("Que letra deseas buscar:"))
letrausuarioma = letrausuario.upper()
for nombre in nombres:
    for letra in nombre:
            if letra == letrausuarioma:
                print(nombre)
                break
