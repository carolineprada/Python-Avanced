# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:29:08 2021

@author: Caroline
"""

#

def lower(elementos):
    return elementos.lower()

lista=["NANa", "Orion", "COFFEe"]


#Programación Funcional
print(list(map(lower, lista)))
print([cad.lower() for cad in lista])

