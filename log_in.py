# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:26:49 2021

@author: Caroline
"""

#Import
import wx

class EjemploAvan(wx.Frame):
    
    def __init__ (self, parent):
        wx.Frame.__init__(self, parent)
        self.Centre()
        
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3,2)
        
        self.textoU = wx.StaticText(self.panel, label="Usuario:")
        self.sizer.Add(self.textoU, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.textoP = wx.StaticText(self.panel, label="Password:")
        self.sizer.Add(self.textoP, pos=(1,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        self.textoR = wx.StaticText(self.panel, label="Respuesta")
        self.sizer.Add(self.textoR, pos=(2,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        
        #Modificadores
        self.textoeditU = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoeditU, pos=(0,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        self.textoeditP = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoeditP, pos=(1,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        
        #Botón
        self.boton = wx.Button(self.panel, label='Log in', size=(50,25))
        self.sizer.Add(self.boton, pos=(3,3), flag=wx.RIGHT|wx.BOTTOM)
        
        
        #Opción que activa el evento
        self.panel.Bind(wx.EVT_BUTTON, self.Validar, self.boton)
        self.panel.SetSizerAndFit(self.sizer)
        
    #Método que  activa el evento validador
    def Validar(self, event):
        usuario=self.textoeditU.GetValue()
        password=self.textoeditP.GetValue()
        
        if(usuario == 'lola' and password == 'lola123'):
            self.textoR.SetLabel('Correcto')
            nv = NuevaVentana(None)
            nv.Show()
        else:
            self.textoR.SetLabel('Incorrectos')
            
            
class NuevaVentana(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        panel = wx.Panel(self, -1)
        txt = wx.StaticText(panel, label="¡¡ Entramos yupii !!")
        
app= wx.App(False)
frame = EjemploAvan(None)
frame.Show() 
app.MainLoop()       
            
        
    
        
    
    
    
    