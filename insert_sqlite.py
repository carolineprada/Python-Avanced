# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 21:53:21 2021

@author: Caroline
"""

#Import SQLite

import sqlite3

#Conexiòn
con = sqlite3.connect('my_database.sqlite')

query = "INSERT INTO 'prueba' ('id', 'nombre', 'edad') VALUES (2, 'Felipe', 21)"

con.execute(query)
con.commit()
con.close()