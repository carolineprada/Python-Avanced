# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:46:22 2021

@author: Caroline
"""
#Importar 

import wx

app = wx.App()

#Contenedor
#None→ Elemento padre
frame = wx.Frame(None, -1, 'Primer Ventana', style=wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX )

#Mostrar Contenedor
frame.Show()


#Ciclo Infinito para acceder a otros elementos
app.MainLoop()