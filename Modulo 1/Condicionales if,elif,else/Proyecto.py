#En los siguientes 5 ejercicios, quiero que pongas el operador de comparación o lógico que corresponda (donde aparece un interrogante «?») para que se cumpla la condición. Puede que en algunos casos, encajen diferentes operadores, da igual cuál pongas. Solo te pido que siempre sea True la expresión del IF.
#Ejercicio 1
# numero = 10
#if numero ? 7:
#    print("Verdadero.")
numero = 10
if numero > 7:
    print("Verdadero.")
#Ejercicio 2
#numero = 5
#if numero ? 7:
 #   print("Verdadero.")
numero = 5
if numero <7:
    print("Verdadero.")
#Ejercicio 3
#numero = 7
#if numero ? 7:
#   print("Verdadero.")
numero = 7
if numero == 7:
    print("Verdadero.")
#Ejercicio 4
color = "verde"
forma = "triangular"
if color == "verde" and forma == "triangular":
    print("Verdadero.")
else:
    print("Falso.")
#Ejercicio 5
color = "verde"
forma = "triangular"

if color == "verde" and forma == "triangular":
    print("Verdadero.")
else:
    print("Falso.")
#¿Es cierta esta afirmación? El bloque else, nunca lleva expresión de comparación. Está sujeto a las expresiones del if y elif si los hay.
#La afirmación es verdadera. El bloque else, no lleva expresión. Depende de las expresiones del if y los elif.
#Ejercicio 7 Sin ejecutar este código, ¿Qué crees que devuelve la consola?
numero_1 = 10
numero_2 = 10
numero_3 = 15
 
if numero_1 == numero_2 and numero_3 > numero_1:
    print('Se cumple la condición.')
else:
    print('No se cumple la condición.')
#Solución: Sí se cumple la condición
#Ejercicio 8
#En los siguientes fragmentos de código, encuentra el/los error/es, si los hay. Intenta primero no utilizar Visual Studio Code para que te los muestre. Si no los ves, revísalo con VSCode antes de mirar la solución.
numero = 7
if numero > 7:
    print("El número es mayor que 7.")
elif numero == 7:
    print("El numero es igual a 7.")
else:
    print("El número es menor o igual a 7.")
#Solución: colocar elif envez de else if
#Ejercicio 9: Colocar : despues de la condicion de if y else
numero = 5
if numero > 7:
    print("El número es mayor que 7.")
else:
    print("El número es menor o igual a 7.")
#Ejercicio 10 Solución: Colocar == en la condición if
numero = 5
if numero ==7:
    print("El número es mayor que 7.")
else:
    print("El número es menor o igual a 7.")
#Proyecto Calculadora con 2 numeros, dos decimales y un menú con sus operaciones
print("******Esta es una calculadora*****")
print("1- Suma.")
print("2- Resta.")
print("3- Multiplicación.")
print("4- División.")
print("5- Exponencial.")
print("6- Floor.")
operacion=int(input("Seleccione una opción:"))
n1=int(input("Ingresa el valor del numero 1: "))
n2=int(input("Ingresa el valor del numero 2: "))
operacion=int(input("Seleccione una operación:"))
match operacion:
    case 1:
        resp=round(n1+n2,2)
        print(resp)
    case 2:
        resp=round(n1-n2,2)
        print(resp)
    case 3:
        resp=round(n1*n2,2)
        print(resp)
    case 4:
        resp=round(n1/n2,2)
        print(resp)
    case 5:
        resp=round(n1**n2,2)
        print(resp)
    case 6:
        resp=round(n1//n2,2)
        print(resp)
    case defaul:
        print('Opción inválida.')

