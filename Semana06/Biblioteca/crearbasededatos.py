# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 11:25:10 2022

@author: UPEU
"""
import sqlite3

# Con el comando connect buscará la base de datos
# que tenga ese nombre, de lo contrario lo creará.

conexion = sqlite3.connect("bdbiblioteca.db")
tabla_pais =""" CREATE TABLE pais(
            idpais INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE,
            estado TEXT
            )
       """
tabla_editorial=""" CREATE TABLE editorial(
                ideditorial INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                estado TEXT
                )
            """
tabla_autor=""" CREATE TABLE autor(
                idautor INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                f_nacimiento TEXT
                )
            """
tabla_libro = """ CREATE TABLE libro(
                    idlibro INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    cantidad INTEGER,
                    anio INTEGER,
                    precio REAL,
                    estado TEXT,
                    idpais INTEGER REFERENCES pais,
                    ideditorial INTEGER REFERENCES editorial,
                    idautor INTEGER REFERENCES autor
                    )
            """

cursor = conexion.cursor()
cursor.execute(tabla_pais)
cursor.execute(tabla_editorial)
cursor.execute(tabla_autor)
cursor.execute(tabla_libro)

conexion.close()


