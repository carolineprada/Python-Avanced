# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 22:57:40 2021

@author: Caroline
"""

#W= escribir o crear si no existe

import csv

doc=open("archivo.csv", "w")

#convención
doc_csv_w= csv.writer(doc)

lista= ["Coffee", 1528, "Nana", 5589]

#Escribir en el doc, la lista
doc_csv_w.writerow(lista)
doc.close()
