#Programacion Orientada a Objetos
trabajador1_nombre = "Jorge"
trabajador2_nombre = "Karina"
trabajador3_nombre = "Pedro"

trabajador1_apellido = "Perez"
trabajador2_apellido = "Tornero"
trabajador3_apellido = "Reyes"

trabajador1_edad = 22
trabajador2_edad = 20
trabajador3_edad = 30

#print(trabajador3_edad)

#CLASES
class Trabajador():
    nombre = "Jorge"
    apellido = "Perez"
    edad = 30

trabajador4 = Trabajador()
trabajador5 = Trabajador()
trabajador6 = Trabajador()

trabajador6.edad = 35

print(trabajador4.edad)
print(trabajador5.edad)
print(trabajador6.edad)

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def caminar (self):
      print (f"Mi nombre es {self.nombre} y estoy caminando")
    def correr(self):
      print (f"Estoy corriendo")
    def saludar(self):
      print (f"Estoy saludando")
    def cantar(self):
       print (f"Estoy cantando")
    def trabajar(self):
      print (f"Estoy trabajando")

persona1 = Persona("karina", "Tornero", 20)
persona2 = Persona("Pedro", "Reyes", 30)
persona3 = Persona("Jorge", "Perez", 22)

print(persona1.nombre)

persona2.caminar()

