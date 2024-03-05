#1.-¿Cuáles de estos strings son correctos?
#"Hoy es un gran día para programar"
#'El cielo está nublado"-> se debe usar un solo tipo de comillas ya sea ' ó ""
#'¿Qué día es hoy?'
#"Mañana, en inglés se dice "morning""->se debe convinar los tipos de comillas '""' ó "''"
#Lo correcto
print("Hoy es un gran día para programar")
print('El cielo está nublado') 
print('¿Qué día es hoy?')
print('Mañana, en inglés se dice "morning"')
#2.-¿Qué error devuelven los strings mal escritos?->Devuelve este error SyntaxError: unterminated string literal
#3.-Imprime en la consola el número de caracteres que tiene la palabra «automáticamente». Lo puedes hacer con variable o directamente en un print().
num_caracteres="automáticamente"
print(len(num_caracteres))
#4.-¿Sabrías mostrar en la consola solo el caracter de la «á» con acento de «automáticamente»? Lo debes hacer mediante las posiciones de string.
posicion="automáticamente"
print(posicion[5])
#5.-Realiza la operación de 10 elevado a 5 con el uso del operador exponente.
print(10**5)
#6.-Ahora, ¿cómo harías esa operación sin el operador de exponente?
variable=10
print(variable*variable*variable*variable*variable)
#7.-¿En qué dos estados puede estar un dato booleano?->Puede ser True ó False
#8.-Muestra en la consola el tipo de dato que contiene esta variable: «numero_1 = 675.87».
numero_1 = 675.87
print(type(numero_1))
#9.-Muestra la cantidad de dígitos que tiene este número (768763843) utilizando la función len().
numero='768763843'
print(len(numero))
#10.-Haz que estos datos float, se conviertan en integer mediante la conversión de tipos:
#numero_1 = "14.527" numero_2 = "560.92"
numero_1 = "14.527"
num_integer1=float(numero_1)
numero_2 = "560.92"
num_integer2=float(numero_2)
print(int(num_integer1))
print(int(num_integer2))
#11.- Redondea estos números con la cantidad de decimales indicada en los comentarios e imprímelos en la consola.
numero_1 = 10.897654876534 # 3 decimales
numero_2 = 7674.7886 # 2 decimales 
numero_3 = 68754.78 # 1 decimal
#Solución
print(round(numero_1,3))
print(round(numero_2,2))
print(round(numero_3,1))
#12.- ¿Cuál es la diferencia entre el operador módulo y floor division? Floor, devuelve la parte entera de la división; en cambio el módulo devuelve el resto de la división entera.
#13.- Asigna con los operadores de asignación de incremento o decremento los siguientes valores indicados en los comentarios.
numero_1 = 10 # +60
numero_2 = 24 # -100
numero_3 = 65.67 # +4.33
#Solución
numero_1 +=60
print(numero_1)
numero_2 -=100
print(numero_2)
numero_3 +=4.33
print(numero_3)
#14.-Mediante la técnica de formateo de strings (recuerda el prefijo f) muestra literalmente todos estos valores en una frase en el print(), sin utilizar la concatenación.
valor=769.97
numero=4
texto='¿Am I a string?'
bool=True
print(f'El valor {valor} es bastante más grande que {numero}. {texto} The answer is {bool}.')


