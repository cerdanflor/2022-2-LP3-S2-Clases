# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:15:36 2022

@author: UPEU
"""

archivo = open("archivo_de_prueba.txt","wt")
contenido = "Línea1 Hola Amigos cómo están?\nLínea2 Bienvenido a la Untels."
archivo.write(contenido)
archivo.close()