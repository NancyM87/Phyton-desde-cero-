'''1. Verdadero o falso. El método grid() sirve para ordenar los elementos en orden de aparición en el código.
Falso, este método permite posicionar los widgets en una celda en especifico;crea una tabla de posiciones que permite colocar los elementos en forma de filas y columnas.
2. Verdadero o falso. El método para mantener el programa Tkinter en marcha, es mainloop().
Verdadero
'''
#Creamos una ventana básica:
'''
Intenta realizar cada uno de estos ejercicios, primero sin mirar los ejemplos del temario. Intenta hacerlo de memoria. En cada ejercicio, ejecuta el programa a ver si cumples con lo que te pido.
Crea una ventana de Tkinter que se mantenga abierta.
Añade un título a la ventana.
Quiero que la ventana sea de 600 px de ancho por 450 px de alto.
Ahora, que la ventana aparezca en la pantalla en las siguientes coordenadas: 50+75.
Crea dos etiquetas que muestren un par de mensajes.
Con el uso de grid() muestra y coloca las dos etiquetas en la misma fila, la 0.
'''
from tkinter import *
root=Tk()
#Título de la
root.title=('Ventana Básica')   
#Tamaño de la ventana
root.geometry('600x450+50+75')
#Creación de la etiqueta
mensaje=Label(root, text="Hola Nancyta")
mensaje.grid(row=0, column=0)
mensaje1=Label(root, text="Como te trata la vida")
mensaje1.grid(row=0, column=1)
#Bucle de ejecución
root.mainloop()
