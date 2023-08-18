#Creamos funciones
def saludar():
    print("Hola!")

saludar()

from datetime import datetime

def mostrarHora():
    hora = datetime.now()
    print("Hola Actual: " + hora.strftime("%H:%M:%S"))
mostrarHora()

from random import randint
def numeroAleatorio():
    return randint(0, 100)

print(numeroAleatorio())

#Creacion una funcion que pueda hallar el area del rectangulo
# base * altura

def areaRectangulo(base, altura):
    area = base * altura
    return area

print("El area del rectangulo es: " + str(areaRectangulo(8,3)) )

#Actividad crear dos funciones una que calcule el area del cuadrado 
# y otro del triangulo

# (base * altura) / 2

def areaTriangulo(base, altura):
    area = (base * altura) / 2
    return area
print("El area del triangulo es: " + str(areaTriangulo(8,3)) )

#FUNCINONES DE UNA CALCULADORA
#Crea una funcion que sume, reste, multiplique y divida dos numeros|