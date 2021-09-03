# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:45:47 2021

@author: mafer
"""

#Listas condicionadas (ALL)
calificacion=93
asistencias=10
faltasTarea=0

lista_condicionada=[calificacion>=90,
                  asistencias>=15,
                  faltasTarea<=1
                  ]
if(all(lista_condicionada)):
    print("Alumno de Excelencia")

else:
    print("Alumno Regular")




