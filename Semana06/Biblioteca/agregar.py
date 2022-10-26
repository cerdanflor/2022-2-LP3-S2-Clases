# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:58:44 2022

@author: UPEU
"""

import sqlite3

conexion = sqlite3.connect("bdbiblioteca.db")

consulta = """ INSERT INTO
                PAIS(NOMBRE, ESTADO)
                VALUES('Brasil', 'A')
           """
cursor = conexion.cursor() 
cursor.execute(consulta)
conexion.commit() 

conexion.close()         
           

