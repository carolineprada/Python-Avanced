# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:09:52 2021

@author: Caroline
"""

import wx

class EjemploMenu(wx.Frame):
    
    def __init__ (self, parent, title):
        super(EjemploMenu, self).__init__(parent, title=title)
        self.InitUI()
        
        
    #Definir el Menù    
    def InitUI(self):
        menubar = wx.MenuBar()
        
        #Opciones
        archivo = wx.Menu()
        archivo.Append(wx.ID_FILE, '&Archivo')
        archivo.Append(wx.ID_EDIT, '&Editar')
        archivo.Append(wx.ID_SAVE, '&Guardar')
        archivo.Append(wx.ID_HELP, '&Ayuda')
        archivo.AppendSeparator()
        
        
        #Opciòn 2
        edit = wx.Menu()
        edit.Append(wx.ID_ANY, "&Zitem")
        edit.Append(wx.ID_ANY, "&XItem")
        edit.Append(wx.ID_ANY, "&WItem")
        
        archivo.AppendMenu(wx.ID_ANY, '&editar', edit)
        
        opcion = wx.MenuItem(archivo, wx.ID_ANY, '&Salir')
        archivo.AppendItem(opcion)
        
        #Puerta de Enlace
        self.Bind(wx.EVT_MENU, self.onQuit, opcion)
        menubar.Append(archivo, '&Archivo')
        
        self.SetMenuBar(menubar)
        self.Show(True)
        
    #Salir    
    def onQuit(self, e):
        self.Close()
        
        
        
frame = wx.App()
EjemploMenu(None, 'Word')
frame.MainLoop() 



       
        