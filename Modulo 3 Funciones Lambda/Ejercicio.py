'''
Crea con una función lambda, una calculadora de áreas de círculo.
El área de un círculo se calcula con la siguiente fórmula: PI * radio * radio

Te dejo el valor de PI:

PI = 3.14159265359
'''
PI=3.14159265359
def area_circulo(radio):
    return  PI*radio*radio
print(round(area_circulo(0.5),2))