# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 18:07:06 2022

@author: Caroline
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
import seaborn as sns
import scipy
from scipy import stats




#Abrir archivo
df = pd.read_csv('cars.csv', delimiter=";")
df.head()


X = df['x'].tolist() #Lista
Y = df['y'].tolist() #Lista
V = df['Year'].tolist() #Lista


w= np.array([X]) #Arreglo
z= np.array([Y]) #Arreglo

e = X[0:20]
f = Y[0:20]
g = V[0:20]


#---PARTE 1 [General]
#Diagrama de dispersion
#plt.title("Diagrama de Dispersión")
#plt.scatter(X, Y, c='grey')
#plt.xlabel("Años");
#plt.ylabel("Automoviles Importados")


#---PARTE 1.1 [1969 a 1988]
#Diagrama de dispersion
plt.title("Diagrama de Dispersión de 1969 a 1988")
plt.scatter(e, f, c='grey')
plt.xlabel("Años");
plt.ylabel("Automoviles Importados")



#---PARTE 2 [1969 a 1988]
#Minimos cuadrados
m = np.amin(e) #Minimo
n = np.amax(e) #Maximo
a = np.array([np.ones(len(e)), e]).T
j = inv(a.T @ a) @ a.T @ f #Fórmula de minimos cuadrados

x_pred = np.linspace(m, n)
y_pred = j[0] + j[1] * x_pred

plt.title("Regresión Líneal de Mínimos Cuadrados ")
plt.scatter(e, f, c='grey')
plt.plot(x_pred, y_pred, 'r')
plt.xlabel("Años");
plt.ylabel("Automoviles Importados")



#---PARTE 3 [Analisis Varianza ANOVA]
df_anova= df[['decada', 'y']]
grop_anova= df_anova.groupby(['decada'])

f_val, p_val =stats.f_oneway(grop_anova.get_group('70s')['y'], grop_anova.get_group('80s')['y'] )
print("ANOVA results 70's y 80's': F=", f_val, ", P =", p_val)  

f_val, p_val =stats.f_oneway(grop_anova.get_group('80s')['y'], grop_anova.get_group('90s')['y'] )
print("ANOVA results 80's y 90's': F=", f_val, ", P =", p_val)   


#---Parte 4 [Regresión Lineal]


