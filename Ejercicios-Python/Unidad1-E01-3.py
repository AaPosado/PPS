class Persona:
    def __init__(self,nombre="", edad=0, dni="", telefono=0, email=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.telefono = telefono
        self.email = email
    def mayoredad(self):
        if(self.edad >= 18):
            return True
        else:
            return False

persona = Persona("Abel",21,"52265486A",1234567890,"abeposrey415@g.educaand.com")
print("Nombre: " + str(persona.nombre))
print("Edad: " + str(persona.edad))
print("DNI: " + str(persona.dni))
print("Teléfono: " + str(persona.telefono))
print("Email: " + str(persona.email))
print("La persona es mayor de edad: " + str(persona.mayoredad()))
