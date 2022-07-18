# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:33:24 2021

@author: Caroline
"""

##Read dats in database MySQL

#Conector

import mysql.connector

#Conexiòn BD
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="bd_python")

#Ejecutar
cursor=con.cursor()

#Sentencia MySQL
cursor.execute("SELECT * FROM `prueba`")

#llama todas las filas
rows= cursor.fetchall()

for row in rows:
    print(row)
    
cursor.close()
con.close()
