# -*- coding: UTF-8 -*-
 
"""
La secuencia de Fibonacci es una secuencia de números con la relación:

Fn = Fn−1 + Fn−2, donde F1 = 1 y F2 = 1

Resulta que F_541 contiene 113 dígitos y es el primer número de Fibonacci donde los
últimos 9 dígitos son una secuencia pan-digital (que contiene todos los números del 1 al 9,
pero no es necesario que estén en orden). Por otro lado F_2749 contiene 757 dígitos y es el
primer número de Fibonacci donde los primeros 9 dígitos son una secuencia pan-digital.

F_k es el primer número de Fibonacci donde los primeros 9 dígitos son una secuencia pan-
digital y donde los últimos 9 dígitos también son una secuencia pan-digital.

¿Cuánto es K?

"""

"""

Correcion: F_2749 contiene 575 dígitos

"""
# Inicializamos variables, i de contador a y b como los primeros numeros de la serie de fibbo
i, a, b = 0,0,1
num = ""

while i >= 0: # el ciclo no se detiene hasta encontrar el numero deseado
    a, b = b, a + b # formula de recursión para construir la serie
    num = str(a) # convertimos a str para poder obtener la longitud y hacer un slicing para obtener los primeros y ultimos 9 digitos
    if len(str(a)) > 9:
        R = num[:9] # slicing de los primeros 9 digitos
        L = num[-9:]  # slicing de los ultimos 9 digitos
        
        pan_digital = "123456789" # secuencia pan_digital

        pandigital_R = True # Partimos con la condicion de que son pandigitles para lado Derecho e Izquierdo
        pandigital_L = True 

        # Para cada uno de los slicing o partes del numero a travez de un for se busca que cumplan la condicion pan_digital
        for digito in pan_digital:
            if digito not in R: # primeros 9 digitos
                pandigital_R = False

        for digito in pan_digital:
            if digito not in L: # ultimos 9 digitos
                pandigital_L = False
        # se imprime una linea cada 50 pasos para asegurar que el codigo sigue corriendo ya que se demora mucho
        if i % 50 == 0:
            print("paso {}".format(i+1))
        
        if pandigital_L == True and pandigital_R == True: # comprobación de pan_digital al final y al inicio
            print("Es pan digital {} y es K_{} con longitud {}".format(a,i+1,len(str(a))))
            break # rompemos el while al obtener el resultado
    
    i += 1 # +1 en el ciclo
       


"""

El K es K_329468 con longitud 68855
El codigo en un equipo core i5 8 Gb Ram tarde mas de 6 horas en encontrar el numero de 68855 digitos

"""