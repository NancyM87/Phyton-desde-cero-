#1. Imprime el diccionario entero.
colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo"
}
print(colores)

'''
2. Presenta (imprimiendo) cada uno de los valores de ese mismo diccionario y que la salida se vea de esta forma:
1 - Rojo
2 - Azul
3 - Verde
4 - Amarillo

Por cierto, fíjate que los colores tienen la primera letra en mayúscula. 
No cambies esa letra directamente en el diccionario. Hazlo con un método.
'''
colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo"
}
for i in colores:
    print(f" {i} - {colores[i].capitalize()}")

#3. Añade un quinto color al diccionario.
colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo",
    5 :  "rosado"
}
print(colores)

#####SETS####
my_set=set([1,2,3,4,5,6,7,8,9])
print(my_set)
#Añadir
my_set.add(10)
print(my_set)
#Eliminar
my_set.remove(5)
print(my_set)
#Se utiliza discard tambien para utilizar eliminar un elemento del set
my_set.discard(1)
print(my_set)
#Vaciar un set
my_set.clear()
print(my_set)
#Union
my_set1=set([1,2,3,4,5])
my_set2=set([6,7,8,9,10,20,30])
my_set_union=my_set1.union(my_set2)
print(my_set_union)

             
