##Empecemos por algo fácil. Imprime esta frase en la consola. «Estoy en el día 1 del reto de Python.».
print('«Estoy en el día 1 del reto de Python.»')
##Almacena el texto anterior en una variable.
variable='«Estoy en el día 1 del reto de Python.»'
##Imprime el valor de la variable anterior
print(variable);
#Tenemos 4 variables. Presta atención a sus valores. En este ejercicio, no tienes que hacer nada.
a = "rojo"
b = "naranja"
c = "azul"
d = "verde"
#¿Podrías asignar el valor «verde» a la variable «a» sin escribir «verde»? Imprime el valor de «a» con el valor «verde».
a=d;
print(a);
#Ahora, quiero que hagas el siguiente reto. ¿Podrás hacerlo sin ver las soluciones? Debes asignar el valor «rojo» a la variable «c», sin asignar directamente «a» sobre «c». Es decir, no puedes hacer esto: c = a. Tampoco se permite escribir el valor literalmente.
b=a;
c=b;
print(b);
#¿Es correcta la siguiente instrucción?
frase_1 = "Esta es la primera frase"; 
frase_2 = "Esta es la segunda frase";
#La siguiente pregunta es para que apliques el sentido común, para que digas lo que piensas. ¿Hay algún error aquí? ¿O es solo estético?
print("¡Qué print más raro")
#¿Cómo sacarías estos dos strings (texto) juntos en el print()? Si ves que aparecen mal los espacios entre cada frase, arréglalo.
frase_1 = "Me llamo Sandra"
frase_2 = "y tengo 23 años."

print(frase_1 + ' '+ frase_2);
##Debes construir un programa que haga lo siguiente:
#Frase de saludo inicial.
print('Bienvenido/a a la clase de Phyton');
#Entrada del usuario preguntando el nombre.
nombre=input('Por favor, ingreza tu nombre:'+'\n');
#Entrada del usuario preguntando la edad.
edad=input('Por favor ingresa tu edad:'+'\n');
#También, una entrada del usuario preguntando el país de nacimiento.
pais_nacimiento=input('Por favor ingresa el país de nacimiento:'+'\n');
#Vas a tener que presentar los datos recogidos del usuario e imprimirlos en una frase final.
print('Estoy presentando los datos recogidos del usuario');
print('Hola como estas!'+' '+nombre +' '+'tu tienes'+ ' '+edad + ' '+'años'+' '+'y tu pais de nacimiento es'+' '+ pais_nacimiento );

