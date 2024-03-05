#Condicional IF
numero=20
if numero>20:
    print("El número es mayor que 20.")
elif numero==20:
    print("El número es igual a 20")
else:
    print("El número es menor o igual a 20")
#IFs anidados
# Se le pide la edad al usuario.
edad = int(input("Introduzca su edad:\n"))

# Se deja la variable sin valor.
respuesta = None

# Se evalúa si el usuario es mayor de edad. Si lo es, accede a
# la compra de alcohol.
if edad >= 18:
    print("Es mayor de edad, puede comprar alcohol. ¿Cuál desea? Introduzca un número de opción.")
    respuesta = input("1- ron.\n 2- whisky.\n 3- ginebra.\n")

    if respuesta == "1":
        print("Ha elegido comprar ron.")
    elif respuesta == "2":
        print("Ha elegido comprar whisky.")
    elif respuesta == "3":
        print("Ha elegido comprar ginebra.")
    else:
        print("Opción no válida.")
else:
    print("Es menor de edad, vuelva de aquí un tiempo o no empiece con el alcohol.")
#Operador AND->Sólo es verdad cuando las 2 condiciones son verdaderas caso contrario es falso
color = "rojo"
forma = "círculo"

if color == "rojo" and forma == "círculo":
    print("Es un círculo rojo.")
else:
    print("No se cumple la condición.")
#Operador OR-> Basta que exista un solo valor verdadero todos son verdaderos caao contrario es falso
color = "rojo"
forma = "círculo"
tamano = "grande"

if color == "rojo" or forma == "cuadrado" or tamano == "pequeño":
    print("Se cumple la condición.")
else:
    print("No se cumple la condición.")
#Operador NOT->Se cumple si la expresión no es igual, es diferente.
color = "rojo"
forma = "círculo"

if not color == "azul":
    print("Se cumple la condición.")
else:
    print("No se cumple la condición.")
#Combinación de expresiones
color = "rojo"
forma = "círculo"

if not(color == "azul" and forma == "cuadrado"):
    print("Se cumple la condición.")
else:
    print("No se cumple la condición.")
#Condicional match(switch)->Son similares a los condicionales if, pero sirven para simplificar comparaciones donde tenemos que escribir muchos elif.
error = input('Introduzca un código de error:\n')
match error:
    case "200":
        print('Todo ok.')
    case "301":
        print('Movimiento permanente de la página.')
    case "302":
        print('Movimiento temporal de la página.')
    case "404":
        print('Página no encontrada.')
    case "500":
        print('Error interno del servidor.')
    case "503":
        print('Servicio no disponible.')
    case _:
        print('Error no disponible.')
#Condicional switch (match) case vs if elif else
error = input('Introduzca un código de error\n')
 
if error == "200":
    print('Todo ok.')
elif error == "301":
    print('Movimiento permanente de la página.')
elif error ==  "302":
    print('Movimiento temporal de la página.')
elif error ==  "404":
    print('Página no encontrada.')
elif error ==  "500":
    print('Error interno del servidor.')
elif error == "503":
    print('Servicio no disponible.')
else:
    print('Error no disponible.')



