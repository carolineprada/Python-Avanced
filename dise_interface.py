# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 23:06:21 2021

@author: Caroline
"""

import wx

class EjemploMenu(wx.Frame):
    
    def __init__ (self, parent, title):
        super(EjemploMenu, self).__init__(parent, title=title)
        self.InitUI()
        
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Salir', 'Salir de APP')
        menubar.Append(fileMenu, '&Archivo')
        self.SetMenuBar(menubar)
        #Enlace
        self.Bind(wx.EVT_MENU, self.onQuit, fileItem)
        self.Show(True)
        
        
    def onQuit(self, e):
        self.Close()


frame = wx.App()
EjemploMenu(None, 'word')
frame.MainLoop()