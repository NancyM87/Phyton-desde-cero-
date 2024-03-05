#1. Crea un bucle for que imprima los valores del 7 al 14. Con una frase como esta:El valor del bucle es: 7.
numeros=[7,8,9,10,11,12,13,14]
for n in numeros:
    print(f"El valor del bucle es:{n}.")
#Utilizando la funcioón range()
for i in range(7,15):
    print(f"El valor del bucle es: {i}.")
#2. Haz un bucle while que imprima los valores del 5 al 10. Con una frase como esta:
i=5
while i<=10:
    print(f"El valor del bucle es: {i}")
    i+=1
#3. Crea un bucle for y luego un while que muestren una frase como las anteriores con los valores del 0 al -5000 en decrementos de 500.
#Bucle FOR
for i in range(0,-5001,-500):
    print(i)
#Bucle WHILE
i=0
while i>=-5000:
     print(i)
     i-=500
#4. Itera con un bucle, esta lista de países completamente.
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
for i in range(0,len(paises)):
    print(paises[i])
#Otra manera de resolver
for pais in paises:
    print(f'->{pais}<-')
'''
5. De la siguiente lista, con un bucle, itera todos sus valores y muestra una frase como «El valor del elemento es: 356».
Quiero que omitas todos los valores 10.
Además, quiero que rompas la ejecución del bucle cuando se encuentre el valor 356, pero se tienen que imprimir el resto de valores de la lista.
'''
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_numeros.sort()
for i in lista_numeros:
    if i !=10 and i!=356:
          print(f'El valor del elemento es: {i}')    
#Otra solución
lista_numeros = [10,45,356,10,10,10,46,67,45,10,10,43,10,65,10,10]
lista_numeros.sort()
for i in lista_numeros:
    if i==10:
        continue
    if i==356:
        break
    print(i)
'''
Proyecto:
El proyecto va a ser un pequeño programa de consola que permita al usuario hacer un pedido de pizza con ingredientes extra para añadir.
Requisitos del proyecto
    *Añade un título con un print() para la pizzería, algo como -> Pizzería PF <-.
    *El usuario introducirá el dinero que quiera. Guárdalo en una variable.
    *Crea una lista donde ir añadiendo los ingredientes extra. Pista: métodos de adición en listas.
    *Habrá mínimo tres tipos de pizzas para elegir (pon las que quieras).
    *Cada pizza tendrá un coste diferente.
    *El usuario podrá elegir solo una pizza.
    *Una vez elegida la pizza, se le informará al usuario del total que lleva por el momento.
    *Se le debe solicitar, si quiere o no, añadir ingredientes extra (estos harán subir el precio final).
    *Añade al menos 3 ingredientes extra. El usuario podrá elegir ninguno, uno o varios de estos. No hay límite de ingredientes extra. Si se pasa del dinero que tiene, se le dirá que no le llega y que vuelva a realizar el pedido.
    *Las pizzas e ingredientes, tendrán sus precios almacenados en variables o constantes (piensa que los precios son los que son y no deben variar en todo el programa).
    *Con cada ingrediente extra, se le debe ir sumando el precio al total y mostrárselo al usuario con el cambio que le queda.
    *Si el usuario no quiere ingredientes extra, puede pagar directamente sin añadir ninguno.
    *Finalmente, se le debe presentar el ticket (imprimido en la consola) con el total gastado, el cambio y todos los elementos que se han añadido al pedido, pizza, ingredientes extra y precios.
'''
print(" ->PIZZERIA TODO RICO<-")

dinero=float(input('Introduzca la cantidad de su dinero:'))
dinero_disponible=dinero
total=0
lista_ingredientes=[]
#ingredientes
peperoni=8.40
jamon=5.0
queso=7.0
salami=10.0
champiniones=6.0
chorizo=8.0

#Selección de ingredientes 
seleccion=int(input('Seleccione algún ingrediente extra:'))
match seleccion:
    case 1:
        print(f'Ha elegido peperoni {peperoni}$')
        dinero-=peperoni
        total+=peperoni
        print(f'Total {peperoni}$')       
        print(f"Le quedan {round(dinero,2)}$.")
        lista_ingredientes.append(f"jamon - {jamon}$")
    case 2:
        print(f'Ha elegido jamon {jamon}$')
        dinero-=jamon
        total+=jamon
        print(f'Total {jamon}$')       
        print(f"Le quedan {round(dinero,2)}$.")
        lista_ingredientes.append(f"jamon - {jamon}$")
    case 3:
        print(f'Ha elegido queso {queso}$')
        dinero-=queso
        total+=queso
        print(f'Total {queso}$')       
        print(f"Le quedan {round(dinero,2)}$.")
        lista_ingredientes.append(f"queso - {queso}$")
    case 4:
        print(f'Ha elegido salami {salami}$')
        dinero-=salami
        total+=salami
        print(f'Total {salami}$')       
        print(f"Le quedan {round(dinero,2)}$.")
        lista_ingredientes.append(f"salami - {salami}$")
    case 5:
        print(f'Ha elegido champiniones {champiniones}$')
        dinero-=champiniones
        total+=champiniones
        print(f'Total {champiniones}$')       
        print(f"Le quedan {round(dinero,2)}$.")
        lista_ingredientes.append(f"champiniones - {champiniones}$")
    case 6:
        print(f'Ha elegido chorizo {chorizo}$')
        dinero-=chorizo
        total+=chorizo
        print(f'Total {chorizo}$')       
        lista_ingredientes.append(f"chorizo - {chorizo}$")
    case 7:
        print("Listo,no se agrega ningún ingrediente extra")
    case _:
        print("La opción no existe, Por favor, seleccione del 1 al 7")
    
#Muestra el ticket
if total<=dinero_disponible:
    print("\n-- Su pedido--")
    print(f"El total del pedido es: {total}")
    print(f"Su cambio: {dinero}$")
    for i in lista_ingredientes:
        print(f"-{i}")
    print(f"Provecho")    
else:
    print("Dinero insuficiente:")    
     