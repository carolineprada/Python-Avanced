# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 20:44:18 2021

@author: Caroline
"""

##Delete dats in database MySQL

#Conector

import mysql.connector

#Conexiòn BD
con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="bd_python")

#Ejecutar
cursor=con.cursor()

#Sentencia MySQL
cursor.execute("DELETE FROM `prueba`;")


con.commit()
cursor.close()
con.close()