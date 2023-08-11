# =====================================
#             VARIABLES
# =====================================
nombre = "Saul"
numero1 = 23
numero2 = 10.5
abc = True

# print(type(numero2))

# Multiplicando letras con numeros
print(nombre * 5)

# =====================================
#         ESTRUCTURA DE FLUJO
# =====================================
#Condicionales if

guisante = 5
if guisante > 10 :
    print("La condicion es verdadera")
else:
    print("La condicion es falsa")

tomas = input("Escribe el numero 10, 20 o 30: ")
if tomas == "10" :
    print("elegiste el numero 10")
elif tomas == "20" :
    print("elegiste el numero 20")
elif tomas == "30":
    print("elegiste el numero 30")
else:
    print("elegiste un valor incorrecto")

#Actividad
#El usuario va a elegir un numero del 1 al 7 y cuando elija 
#el numero se imprimira el dia iniciando del lunes
# --------------------------------------------------------------------------------------------
#                                        VARIABLES
# --------------------------------------------------------------------------------------------
variable1 = "Esta es una variable de tipo String"
variable2 = 20
variable3 = 5.3
variable4 = True

# Los elementos de una lista pueden ser de distinto tipo e, incluso, otras listas
variable5 = [variable1, variable2, variable3, variable4]

# Variables numéricas de distinto tipo pueden operar entre sí
print(type(variable2), type(variable3))

print(variable2 + variable3)

# El tipo de dato que acepta una variable es mutable, es decir, se puede cambiar sin problemas
print(type(variable4))

variable4 = "Verdadero"
print(type(variable4))

# Las cadenas de caracteres (string) se pueden multiplicar por números enteros
print(variable1 * 3)
print("=================================================================================")
# --------------------------------------------------------------------------------------------
#                                   ESTRUCTURAS DE FLUJO
# --------------------------------------------------------------------------------------------
# Condicionales if
condicion = True
if condicion == True:
    print("Bloque de código que solo se ejecuta si se cumple la condición")
else:
    print("Bloque de código que se ejecuta si no se cumple la condición")

print("=================================================================================")
# Actividad
diaEnNumero = input("Ingrese un número entre 1 y 7: ")
if diaEnNumero == "1":
    print("Lunes")
elif diaEnNumero == "2":
    print("Martes")
elif diaEnNumero == "3":
    print ("Miércoles")
elif diaEnNumero == "4":
    print("Jueves")
elif diaEnNumero == "5":
    print("Viernes")
elif diaEnNumero == "6":
    print("Sábado")
elif diaEnNumero == "7":
    print("Domingo")
else:
    print("Valor no reconocido. Inténtelo nuevamente.")
