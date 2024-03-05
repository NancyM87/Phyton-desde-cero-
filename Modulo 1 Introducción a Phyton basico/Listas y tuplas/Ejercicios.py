#Para comentarios de varias lineas se utiliza ''' 
'''
1. Crea una lista llamada «lista_numeros» y almacena los siguientes valores integer:
10
45
55
76
'''
lista_numeros=[10,45,55,76]
print(lista_numeros)
#2. De la lista anterior, imprime el valor 76 en la consola.
print(lista_numeros[3])
#3. Utiliza el formateo de strings (f»») para imprimir esta frase en la consola. Utiliza la lista del ejercicio 1 para mostrar el 10 y el 76.
#El valor más pequeño en la lista es el 10. El más grande, el 76.
print(f'El valor más pequeño en la lista es el {lista_numeros[0]}.El más grande, es el {lista_numeros[3]}.')
'''
4. Encuentra los fallos:
lista_colores ["rojo", "azul", "verde", 'amarillo'] Solución:Se debe asignar con = la lista a la variable lista_colores
'''
lista_colores=["rojo", "azul", "verde", "amarillo"]
print(lista_colores)
'''
5. Encuentra los fallos:
lista_colores = ["rojo", "azul" "verde", "amarillo"]
print(lista_colores(0)) Solución: Para posiciones se utiliza []
'''
lista_colores=["rojo", "azul" "verde", "amarillo"]
print(lista_colores[0])
'''
6. Encuentra los fallos:
lista_colores = ["rojo", "azul", "verde"]
print(lista_colores[-0])
print(lista_colores[-4]) Solución: La posición -0 no existe.
'''
lista_colores = ["rojo", "azul", "verde"]
print(lista_colores[0])
print(lista_colores[-3])
'''
7. Imprime en la consola el carácter «u» de azul.
lista_colores = ["rojo", "azul", "verde", "amarillo"] Solución:  Con el valor [2], al carácter de la posición 2 del string (u).
'''
lista_colores = ["rojo","azul","verde","amarillo"]
caracter=lista_colores[1][2]
print(caracter)
''' 
8. Este es un listado de países. Imprime los dos últimos países, Zambia y Zimbabwe.
Solución: Se trabaja con las posiciones o también se puede utilizar la función len()
'''
paises = ["Afghanistan","Albania","Algeria",
"Andorra","Angola","Anguilla",
"Antigua and Barbuda",
"Argentina","Armenia",
"Aruba","Australia","Austria",
"Azerbaijan","Bahamas","Bahrain",
"Bangladesh","Barbados","Belarus",
"Belgium","Belize","Benin","Bermuda",
"Bhutan","Bolivia","Bosnia & Herzegovina",
"Botswana","Brazil","British Virgin Islands",
"Brunei","Bulgaria","Burkina Faso","Burundi",
"Cambodia","Cameroon","Cape Verde",
"Cayman Islands","Chad","Chile","China",
"Colombia","Congo","Cook Islands",
"Costa Rica","Cote D Ivoire","Croatia",
"Cruise Ship","Cuba","Cyprus","Czech Republic",
"Denmark","Djibouti","Dominica",
"Dominican Republic","Ecuador","Egypt",
"El Salvador","Equatorial Guinea",
"Estonia","Ethiopia","Falkland Islands",
"Faroe Islands","Fiji","Finland","France",
"French Polynesia","French West Indies","Gabon",
"Gambia","Georgia","Germany","Ghana","Gibraltar",
"Greece","Greenland","Grenada","Guam","Guatemala",
"Guernsey","Guinea","Guinea Bissau","Guyana",
"Haiti","Honduras","Hong Kong","Hungary","Iceland",
"India","Indonesia","Iran","Iraq","Ireland",
"Isle of Man","Israel","Italy","Jamaica","Japan",
"Jersey","Jordan","Kazakhstan","Kenya","Kuwait",
"Kyrgyz Republic","Laos","Latvia","Lebanon",
"Lesotho","Liberia","Libya","Liechtenstein",
"Lithuania","Luxembourg","Macau","Macedonia",
"Madagascar","Malawi","Malaysia","Maldives",
"Mali","Malta","Mauritania","Mauritius","Mexico",
"Moldova","Monaco","Mongolia","Montenegro",
"Montserrat","Morocco","Mozambique","Namibia",
"Nepal","Netherlands","Netherlands Antilles",
"New Caledonia","New Zealand","Nicaragua","Niger",
"Nigeria","Norway","Oman","Pakistan","Palestine",
"Panama","Papua New Guinea","Paraguay","Peru",
"Philippines","Poland","Portugal","Puerto Rico",
"Qatar","Reunion","Romania","Russia","Rwanda",
"Saint Pierre & Miquelon","Samoa","San Marino",
"Satellite","Saudi Arabia","Senegal","Serbia",
"Seychelles","Sierra Leone","Singapore","Slovakia",
"Slovenia","South Africa","South Korea","Spain",
"Sri Lanka","St Kitts & Nevis","St Lucia",
"St Vincent","St. Lucia","Sudan","Suriname","Swaziland",
"Sweden","Switzerland","Syria","Taiwan","Tajikistan",
"Tanzania","Thailand","Timor L'Este","Togo","Tonga",
"Trinidad & Tobago","Tunisia","Turkey","Turkmenistan",
"Turks & Caicos","Uganda","Ukraine",
"United Arab Emirates","United Kingdom","Uruguay",
"Uzbekistan","Venezuela","Vietnam",
"Virgin Islands (US)","Yemen","Zambia","Zimbabwe"]
imprimir=paises
print(imprimir[-2],imprimir[-1])
'''
9. Añade a la lista_colores los siguientes colores en los sitios donde se te pide. Lo tienes que hacer con algún método de adición de elementos, no puedes editar la lista manualmente.
Tienes que añadir los colores en el código en este orden:
*gris-Antes de «rojo».
*rosa-En último lugar.
*naranja-Entre «azul» y «verde».
lista_colores = ["rojo", "azul", "verde", "amarillo"]
'''
lista_colores = ["rojo", "azul", "verde", "amarillo"]
lista_colores.insert(0,"gris")
lista_colores.append("rosa")
lista_colores.insert(3,"naranja")
print(lista_colores)
'''
10. De la lista resultante del ejercicio anterior, elimina los valores «rojo», «verde» y «amarillo» con el método pop().
'''
lista_colores_anterior=['gris', 'rojo', 'azul', 'naranja', 'verde', 'amarillo', 'rosa']
print(lista_colores_anterior.pop(1),lista_colores_anterior.pop(3),lista_colores_anterior.pop(3))
'''
11. Duplica esta lista en otra.
'''
lista_colores = ["rojo", "azul", "verde", "amarillo"]
duplicar_lista=lista_colores
print(duplicar_lista)
#Método copy
duplicar_lista=lista_colores.copy()
'''
12. ¿Sabrías hacer que cuántas repeticiones del valor 10 hay en esta lista?
'''
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
repeticion=lista_numeros.count(10)
print(f"Existen {repeticion} repeticones del valor 10")
'''
13. Emplea un método de Python que muestre la posición del valor «Brazil» de la lista de países del ejercicio 8.
'''
posicion_pais=paises.index("Brazil")
print(posicion_pais)
'''
14. Ordena la lista_numeros del ejercicio 12 de menor a mayor.
'''
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_ordenada=lista_numeros.sort()
print(lista_numeros)
print(lista_ordenada)
'''
15. Ordena la lista_numeros del ejercicio 12 de mayor a menor.
'''
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_ordenada=lista_numeros.sort(reverse=True)
print(lista_numeros)
print(lista_ordenada)
#Utilizando sorted
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
print(sorted(lista_numeros, reverse=True))
'''
16. Muéstrame en la consola, la longitud en número de posiciones de la lista de países del ejercicio 8 con un método.
'''
posicion=len(paises)
print(f"La posición de la lista de paises es: {posicion}")
