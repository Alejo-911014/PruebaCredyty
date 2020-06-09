# -*- coding: UTF-8 -*-
 
"""

Es fácil verificar que ninguno de los 28 números en las primeras 7 filas del Triángulo de
Pascal es divisible por 7:

      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1
 1 5 10 10 5 1
1 6 15 20 15 6 1

Si hacemos este mismo ejercicio para las primeras 100 filas del triángulo, encontraremos
que, de 5050 entradas existentes, tan solo 2361 entradas no son divisibles por 7.
¿Cuántas entradas de las primeras mil millones de filas (10^9) no son divisibles por 7?

"""

# Creamos una función que captura el numero de filas a crear
def Pascal(n):
 
    tpascal = [[1],[1,1]]    # añadimos las dos primeras filas
    contador = 3             # el contador inicia en 3 debido a los 3 numeros anteriores
    for i in range(1,n):     # generamos cada una de los pisos del triangulo
        linea = [1]          # inicializamos cada fila siempre con un 1
        for j in range(0,len(tpascal[i])-1):
            # añadimos al arreglo los nuevos valores y agregamos la suma de los dos anteriores numeros de la anterior fila
            linea.extend([ tpascal[i][j] + tpascal[i][j+1] ])
            # de cada numero generado realizamos conteo si no es divisible por 7
            if (tpascal[i][j] + tpascal[i][j+1]) % 7 != 0:
                contador += 1
        
        linea += [1] # Finalizamos la fila o piso con un 1. 
        contador += 2 # sumamos al contador el primer y ultimo 1 que no fueron incluidos en el anterior ciclo
        tpascal.append(linea) # finalmente para cada fila añadimos la linea al arreglo
        
        if i % 50 == 0: # Print de cada paso para seguimiento.
            print("Paso No: {}".format(i))
        
    return contador

# n 10^9 fila
n = 10**2
"""
Con n = 100 el resultado es 2361 
"""
contador = Pascal(n-1)      # Imprimimos el resultado buscado
print(contador)             # Dado que son demasiados pasos el resultado no puede ser obtenido rapidamente