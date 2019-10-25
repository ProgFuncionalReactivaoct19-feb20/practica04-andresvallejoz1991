"""
andresvallejoz1991
"""

import codecs #Importe para abrir los archivos
import json #Importacion para los archivos de librerias

archivo = codecs.open("datos.txt","r") #Abrir el arhivo datos
lineas = archivo.readlines() #Leer todas las lineas del archivo

linea_diccionario = [json.loads(l) for l in lineas] #Iterar todas las lineas del archivo a un diccionario

funcion1 = lambda x: list(x.items())[1][1]>=3 #Funcion 1 con la condicional para obtener los jugadores con más de 3 goles

print("Los jugadores que han marcado mas de tres goles son: \n")#Print para mejorar las presentacion 
print(list(filter(funcion1,linea_diccionario))) #Print para filtrar y mostras a los jugadores en base a la funcion lambda
print("\nLos jugadores pertenecientes a nigeria son: \n")#Print para mejorar las presentacion 

funcion2 = lambda x: list(x.items())[0][1] == "Nigeria"#Funcion lambda para mostrar los jugadores pertenecientes a Nigeria
print(list(filter(funcion2,linea_diccionario))) #Print para filtrar y mostras a los jugadores en base a la funcion lambda
print("\nLos valores Maximo y minimo de altura de los jugadores son \n")#Print para mejorar las presentacion 

funcion3 = lambda x: list(x.items())[2][1]#Funcion lambda para ubicarnos en la posicion donde se encuentrar la altura de los jugadores.
print(min(list(map(funcion3,linea_diccionario)))) #Print con map para la iteracion y con min para encontre el valor mas bajo
print(max(list(map(funcion3,linea_diccionario))))#Print con map para la iteracion y con max para encontre el valor mas bajo