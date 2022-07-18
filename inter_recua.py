# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 21:29:51 2021

@author: Caroline
"""

#Importar
import wx

#Clase
class EjemploTexto(wx.Frame):
    
    def __init__(self, parent):
        #Inicializar
        wx.Frame.__init__(self, parent)
        self.InitUI()
        self.Center()
        
    #Panel    
    def InitUI(self):
        self.panel = wx.Panel(self)
        self.sizer = wx.GridBagSizer(3,2)
        
        self.texto = wx.StaticText(self.panel, label="Nombre:")
        self.sizer.Add(self.texto, pos=(0,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        
        self.textonuevo = wx.StaticText(self.panel, label="Me llamo")
        self.sizer.Add(self.textonuevo, pos=(1,0), flag=wx.TOP|wx.LEFT|wx.BOTTOM)
        
        self.textoedit = wx.TextCtrl(self.panel)
        self.sizer.Add(self.textoedit, pos=(0,1), span=(1,3), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)
        
        #Botón
        self.boton = wx.Button(self.panel, label='Enviar', size=(90,50))
        self.sizer.Add(self.boton, pos=(3,3), flag=wx.RIGHT|wx.BOTTOM)
        
        self.panel.Bind(wx.EVT_BUTTON, self.TomarTexto, self.boton)
        self.panel.SetSizerAndFit(self.sizer)
        
    #Tomar Texto del recuadro
    def TomarTexto(self, event):
        textotomado='Hola Universo'
        textotomado=self.textoedit.GetValue()
        self.textonuevo.SetLabel(textotomado)
        

app = wx.App(False)
frame = EjemploTexto(None)
frame.Show() 
app.MainLoop()       
        