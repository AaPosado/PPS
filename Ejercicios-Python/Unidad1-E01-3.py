#Definición de clase (Persona) con sus distintos atributos (nombre,edad,dni,tlf) con valores a 0/nada.
class Persona:
    def __init__(self,nombre="", edad=0, dni="", telefono=0, email=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        self.tlf = telefono
        self.email = email
#Definimos la función para la verificación de edad, si un atributo de la clase anterior es mayor o igual a 18, pon true y si no no pon false.
    def mayoredad(self):
        if(self.edad >= 18):
            return True
        else:
            return False
#Inyección de la persona con sus aatributos
persona = Persona("Abel",21,"52265486A",1234567890,"abeposrey415@g.educaand.com")
#imprimimos los datos del usuario.
print("Nombre: " + str(persona.nombre))
print("Edad: " + str(persona.edad))
print("DNI: " + str(persona.dni))
print("Teléfono: " + str(persona.tlf))
print("Email: " + str(persona.email))
print("La persona es mayor de edad: " + str(persona.mayoredad()))
