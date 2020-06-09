# -*- coding: UTF-8 -*-
 
"""
La siguiente información es provista, pero la puede completar con otras fuentes:
- El primero de enero de 1900 fue lunes.
- Los meses de abril, junio, septiembre y noviembre tienen 30 días; los meses de
enero, marzo, mayo, julio, agosto, octubre y diciembre tienen 31 días; y el mes de
febrero tiene 28 días menos en los bisiestos cuando tiene 29 días.
- Los años bisiestos ocurren cada 4 años
- Si es inicio de siglo (año divisible por 100), no hay bisiesto a menos de que dicho
año también sea divisible por 400. En dado caso, sí hay bisiesto.

¿Durante el siglo 20 (1 de enero de 1901 hasta 31 de diciembre de 2000), cuántos meses
han empezado un domingo?
"""
calendario =[] # iniciamos un arreglo par almacenar cada una de las fechas generadas 
año_inicial = 1901 
año_final = 2000
for año in range (año_inicial,año_final+1): # recorrido del siglo 20
    for mes in range (1,13): # recorrido de los 12 meses
        # para decidir en cuanto dias recorrer cada uno de los meses se realizan las siguientes condiciones:
        es_bisiesto = False # Iniciamos si el año es bisiesto
        # calendario gregoriano se repite cada 400 años y si es inicio de siglo 
        if año % 400 == 0:
            es_bisiesto = True
        elif año % 4 == 0:
            es_bisiesto = True
        # numero de los meses donde existen x numero de dias
        if mes in (1, 3, 5, 7, 8, 10, 12):
            dias_mes = 31
        elif mes == 2:
            if es_bisiesto:
                dias_mes = 29 # en caso de feb sea en un año bisiesto
            else:
                dias_mes = 28
        else:
            dias_mes = 30 # otros meses
        # recorrido de cada dia dependiendo el mes
        for dia in range(1,dias_mes+1):
            calendario.append([año, mes, dia]) # agregamos cada dia en formato año mes dia a un arreglo el cual sera recorrido

# contador de domingos
domingo = 0
# Recorrido del calendario que creamos, donde añadimos cada fecha generada.
for dom in range(len(calendario)):
    # el siguiente if indica si es un domingo a travez del modulo y si la fecha empieza en 1, es decir inicio de mes.
    " Importante: El 1ro de enero de 1901 empieza un Martes"
    if (dom+2) % 7 == 0 and calendario[dom][2] == 1: # El contador debe ser movido + 2 posiciones por iniciar un martes
        domingo += 1   
        #print(calendario[dom]) #ver todas las fechas y comprobaciones

# impresion 
print("Numero de meses que empiezan con domingo: {}".format(domingo))

# Respuesta 171