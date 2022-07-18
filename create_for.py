# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:05:44 2021

@author: Caroline
"""
#FOR
#W= escribir o crear si no existe

import csv

doc=open("archivo.csv", "w")

#convención
doc_csv_w= csv.writer(doc)

lista= [["Coffee", 1528], ["Nana", 2583], ["louis", 5312], ["Jaime", 1024]]

for x in lista:
    doc_csv_w.writerow(x)

doc.close()