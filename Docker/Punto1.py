# -*- coding: UTF-8 -*-
 
"""
Existe solo una tripleta de Pitágoras para la cual a + b + c = 1000.
¿Cuál es el producto de abc?
"""

m = 0  # inicializacion de variable
n = 0
at = [] # un arreglo adicional para almacenar los numeros que completan la terna o tripleta

def tripleta(m,n): # funcion de recurrencia
    a = n**2 - m**2 # utilizamos la propiedad euclidea para la contrucción de ternas 
    b = 2*m*n       # a = n2 - m2, b = 2nm, c = n2 + m2
    c = n**2 + m**2
    
    if a > 0: # se asegura que el primer valor que puede llegar a ser negativo siempre sea positivo
        if a + b + c == 1000: # cuando la condición de cumpla arreojamos el resultados
            at.extend([a,b,c])  # agregamos una tpascal de las soluciones al array
            at.sort() # organizamos e imprimimos
            return print("es la tripleta a: {}, b: {} y c: {} y su producto es: {} ".format(at[0],at[1],at[2], at[0]*at[1]*at[2]))
            # es la tripleta a: 200, b: 375 y c: 425 y su producto es: 31875000

# Recurrencia para encontrar el valor
for n in range(1000):
    for m in range(1000): 
        tripleta(n,m)

