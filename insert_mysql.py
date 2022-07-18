# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:27:02 2021

@author: Caroline
"""

##Insert dats in database MySQL

#Conector

import mysql.connector

#Conexiòn BD
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="bd_python")


#Ejecutar
cursor=con.cursor()
#Crear insertar datos en tabla BD (sentencia Mysql)
cursor.execute("INSERT INTO prueba (id, nombre) VALUES ('1', 'Coffee')")

#Cambio en la BD
con.commit()

#Cerrar la conexiòn
con.close()