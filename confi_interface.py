# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:32:32 2021

@author: Caroline
"""

#Importar 

import wx

class Window_New(wx.Frame):
    
    def __init__(self, parent, title):
        super(Window_New, self).__init__(parent, title= "2da Ventana", size= (400, 400))
        #self.Center()
        self.SetPosition((10, 10))
        self.Show(True)
        
        
#Centrar la info. ventana en esta parte        
if __name__ == '__main__' :
    app = wx.App()
    Window_New(None, title='Nueva Ventana')
    app.MainLoop()
