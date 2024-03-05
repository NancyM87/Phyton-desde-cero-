'''
1. Añade cualquier color con un input al principio de la lista mediante una función. 
Debes comprobar fuera de la función, con un print(), que el color se ha añadido correctamente.
'''
colores = ["rojo", "verde", "amarillo"]
def aniadir(color):
    colores.insert(0, color)
aniadir(input("Ingrese cualquier color:" "\n"))
print(f"El color {colores} fue agredado correctamente ")
'''
2. Encuentra un posible error en esta función:
def saludar()
    nombre = input("Introduzca su nombre, por favor\n")
    print(f"¡Muy buenas, {nombre}!")
'''
def saludar():
    nombre = input("Introduzca su nombre, por favor\n")
    print(f"¡Muy buenas, {nombre}!")
print(saludar())

        #####PROYECTO FINAL######
# Se da un título a la calculadora.
print("--- CALCULADORA MEJORADA ---")

# Funciones de calculadora
# Suma
def suma(numero1,numero2):
    return numero1 + numero2
# Resta
def resta(numero1,numero2):
    return numero1 - numero2
# Multiplicación
def multiplicacion(numero1,numero2):
    return numero1 * numero2
# División
def division(numero1,numero2):
    return numero1 / numero2
# Módulo
def modulo(numero1,numero2):
    return numero1 % numero2
# Exponente
def exponente(numero1,numero2):
    return numero1 ** numero2

while True:

    # Se solicitan los dos números para cualquier operación que elija.
    numero_1 = float(input("Ingrese el primer valor:\n"))
    numero_2 = float(input("Ingrese el segundo valor:\n"))
    
    resultado = round(suma(numero_1, numero_2), 2)
    print(f"La suma de {numero_1} + {numero_2} es: {resultado}.")

    resultado = round(resta(numero_1, numero_2), 2)
    print(f"La resta de {numero_1} - {numero_2} es: {resultado}.")

    resultado = round(multiplicacion(numero_1, numero_2), 2)
    print(f"La multiplicación de {numero_1} por {numero_2} es: {resultado}.")

    resultado = round(division(numero_1, numero_2), 2)
    print(f"La división de {numero_1} entre {numero_2} es: {resultado}.")

    resultado = round(modulo(numero_1, numero_2), 2)
    print(f"El resto de la división entera de {numero_1} entre {numero_2} es: {resultado}.")

    resultado = round(exponente(numero_1, numero_2), 2)
    print(f"El número {numero_1} elevado a {numero_2} es: {resultado}.")