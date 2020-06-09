# -*- coding: UTF-8 -*-

"""
Un método de seguridad comúnmente utilizado por los bancos es preguntar tres
caracteres aleatorios de una contraseña. Por ejemplo, si la contraseña es 531278, el banco
puede preguntar por el 2do, 3er, y 5to, carácter; esperando que el usuario responda con la secuencia 3-1-7.

El archivo keylog.txt contiene 50 secuencias correctas para una contraseña especifica.
Dado que cada una de las secuencias está en orden de primer carácter a ultimo carácter,
¿cuál es la contraseña más corta para la cual todas las secuencias son correctas?

R// Lo que se realizara es capturar el peso estadistico de cada valor de las contraseñas o intentos de la lista keylog
segun la posición de la misma es decir si estan en la primera[0] segunda[1] o tercera[2].
"""

from collections import defaultdict # libreria para crear y agrupar elementos en comun en diccionarios de python
import operator # para capturar el valor de los diccionarios y no la clave

array = [] # arreglo para almacenar los valores

# apertura del archivo, lectura de cada numero por linea y concatenación
f = open("keylog.txt", "r")
intento = [line.strip() for line in f.readlines()]
conteos = defaultdict(list) # creación del diccionario de elementos

"""
El siguiente fragmento de codigo es guia para utilizar la función defaultdict()
https://docs.python.org/2/library/collections.html

s = [('yellow', 1), ('blue', 2), ('yellow', 1), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d.items())

"""
# Con el ejemplo anterior lo que se hace es agrupar los digitos como claves con cada valor donde e encontro cada uno de los 
# numero de las secuencias
for x in intento:
    for i, n in enumerate(x):
        conteos[n].append(i) 

# inicializamos una lista para que agregue la clave valor de los digitos segun el promedio del peso que almacenan
promedio_conteo = {}
for k,v in list(conteos.items()):
    promedio_conteo[k] = float(sum(v))/float(len(v))

# organizamos el valor del promedio para obtener el numero
sort = sorted(promedio_conteo.items(), key=operator.itemgetter(1))
for name in enumerate(sort):
    array.append(name[1][0])

# concatenamos cada elemento del arreglo  
print(''.join(str(x) for x in array))   # Respuesta: 73162890