'''1. Verdadero o falso. El método grid() sirve para ordenar los elementos en orden de aparición en el código.
Falso, este método permite posicionar los widgets en una celda en especifico;crea una tabla de posiciones que permite colocar los elementos en forma de filas y columnas.
2. Verdadero o falso. El método para mantener el programa Tkinter en marcha, es mainloop().
Verdadero
'''
#Creamos una ventana básica:
from tkinter import *
root=Tk()
#Título de la
root.title=('Ventana Básica')   
#Tamaño de la ventana
root.geometry('600x450+50+75')
#Creación de la etiqueta
mensaje=Label(root, text="Hola Nancyta")
mensaje.grid(row=0, column=40)
mensaje1=Label(root, text="Como te trata la vida")
mensaje1.grid(row=0, column=60)
#Bucle de ejecución
root.mainloop()
