def iguales(lista1,lista2):
    for nombres in lista1:
        for nombre in lista2:
            if nombres == nombre:
                print("True, el nombre que coincide es: " + nombre)
            else:
                print("False")
    print(lista1==lista2)
iguales(["Pepe","Juan"],["Juan","Nerea"])