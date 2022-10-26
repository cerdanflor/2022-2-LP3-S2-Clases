# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 10:12:03 2022

@author: UPEU
"""

noticia = open("noticia.txt", "rt",encoding='utf8')
datos_noticia = noticia.read()
print(datos_noticia)