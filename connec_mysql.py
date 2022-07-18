# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:16:28 2021

@author: Caroline
"""

##Connect database

#Conector

import mysql.connector

#Conexiòn BD
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="bd_python")


#Ejecutar
cursor=con.cursor()
#Crear insertar datos en tabla BD (sentencia Mysql)
cursor.execute("CREATE TABLE prueba (id INT, nombre VARCHAR(100));")

#Cerrar la conexiòn
con.close()
