# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 18:57:33 2021

@author: mafer
"""

#Listas condicionadas (ANY)
calificacion=93
asistencias=10
faltasTarea=0

lista_condicionada2=[calificacion>=90,
                  asistencias>=15,
                  faltasTarea<=1
                  ]
if(any(lista_condicionada2)):
    print("Alumno de Excelencia")

else:
    print("Alumno Regular")