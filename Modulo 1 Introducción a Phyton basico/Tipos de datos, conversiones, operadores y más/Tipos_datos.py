#Strings(str)->Se utiliza para almacenar cadenas de caracteres.Ejemplos: Letras, símbolos,textos,números.
#Los Strings van dentro de comillas simples('') o dobles("").
print('"Red" es rojo en español')
print("'Red' es rojo en español")
#Función len()->Devuelve el número de caracteres que tiene un string.
print(len("Nancyta"))
#len en un número entero
numeros="12345678"
print(len(numeros))
#En una variable
nombre="Nancyta"
print(len(nombre))
#Posiciones de un string, la posición de la letra a es 0.
color="azul"
print(color[0])
#Integers-> Es un tipo de dato que representa valores numéricos enteros.
#Operaciones con enteros
#Suma
numero1=100
numero2=20
suma=numero1+numero2
print(suma)
#Resta
numero1=20
numero2=-100
resta=numero1-numero2
print(resta)
#Multiplicación
numero1=5
numero2=6
multiplicacion=numero1*numero2
print(multiplicacion)
#Division
numero1=20
numero2=5
division=numero1/numero2
print(division)
#Módulo
numero1=20
numero2=2
modulo=numero1%numero2
print(modulo)
##Exponente(**)
print(5**3)
#Float->Es un tipo de dato que sirve para representar valores con números decimales.
num_decimal=20.45
print(num_decimal)  
#Boolean->Es un tipo de dato que puede recibir 2 valores True o False.
#Como ver el tipo de dato en Phyton
num1=5
num2=89.78
texto="Hoa que tal como te va"
boolean=False
print(type(num1))
print(type(num2))
print(type(texto))
print(type(boolean))
#Transformar un integer a un string
num_entero=4567
num_str=str(num_entero)
print(len(num_str))
#Transformar string en integer
num1="20"
num2="40"
suma=int(num1) + int(num2)
print(suma)
#Truncamiento de números
n1=10.60
n2=10.40
suma=n1+n2
trunca_suma=int(suma)
print(trunca_suma)
#Redondeo de números
numeros=7.5678*6.943534
print(numeros)
print(round(numeros))
#Redondeo de números con 2 deciamles
num=7.5678*6.943534
print(round(num,2))
#Operador de floor division->Realiza divisiones y redondea el resultado al valor entero mas cercano.(//)
division=10//3
print(division)
#Operador módulo(%)->Devuelve el resto de la divisio entera
modulo=10%3
print(modulo)
#Operadores de incremento y decremento
#Operador (+=)
num=10
num+=30
print(num)
#Operador (-=)
num=6
num-=9
print(num)
#Formateo de strings
suma=20+12
print('La suma es:' + str(suma))
#Utilizando prefijo f
suma=90+45
print(f'La suma es:{suma}')
