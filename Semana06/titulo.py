# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 09:20:20 2022

@author: UPEU
"""
# Que pasaría si ahora el problema pidiera que el nombre de flor y león no se 
# muestre en formato título, para eso hemos utilizado una librería camelcase

# importamos la librería
import camelcase

nombre = "flor elizabeth cerdán león"
print(nombre.upper())
print(nombre.title())

# Creamos un objerto llamado cam
cam= camelcase.CamelCase()
print("Con camelcase...")

# imprimimos el nombre en formato titulo
# utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema, creamos otro objeto, incluímos los argumentos
# 'flor' y 'león'
cam2 = camelcase.CamelCase('flor','león')
print(cam2.hump(nombre))

