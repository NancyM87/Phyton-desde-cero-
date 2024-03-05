'''#Importar biblioteca
import tkinter
#Creación de la ventana principal
root=tkinter.Tk()
#Creación de etiqueta
mensaje=tkinter.Label(root, text="Mi primer programa con tkinter")
#Mostrar la etiqueta
mensaje.pack()
#Bucle de ejecución
root.mainloop()
'''
#Importaciones
from tkinter import *

#Creación de la ventana principal
root = Tk()
#Título de la ventana
root.title("Curso de Tkinter de Programación Fácil")
#Tamaño de la ventana
root.geometry("400x300+560+240")

#Creación de las etiquetas
mensaje = Label(root, text="Mi primer programa con Tkinter.")
mensaje_2 = Label(root, text="Esta es la segunda etiqueta.")
# Se muestran las etiquetas
mensaje.grid(row=10, column=10)
mensaje_2.grid(row=5, column=5)

#Bucle de ejecución
root.mainloop()

