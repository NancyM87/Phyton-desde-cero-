'''
1. Añade cualquier color con un input al principio de la lista mediante una función. 
Debes comprobar fuera de la función, con un print(), que el color se ha añadido correctamente.
'''
colores = ["rojo", "verde", "amarillo"]
def aniadir(color):
    colores.insert(0, color)
aniadir(input("Ingrese cualquier color:" "\n"))
print(f"El color {colores} fue agredado correctamente ")

