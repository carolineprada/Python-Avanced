# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 21:56:13 2022

@author: Caroline
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm
import math
from texttable import Texttable
from numpy.polynomial.polynomial import polyfit
from scipy import stats

#Abrir archivo
df = pd.read_csv('cars.csv', delimiter=";")
df.head()


#Sumar variables desde x años
sx=df['x'].sum()
sy=df['y'].sum()
df['x2']= df['x'].apply(lambda x: pow(x,2))
df['y2']= df['y'].apply(lambda x: pow(x,2))

s2x=df['x2'].sum()
s2y=df['y2'].sum()

df['xy']= df['x']*df['y']
sxy=df['xy'].sum()

#Cantidad de datos
n= len(df['x'])

#Media
xp=(df['x'].mean())
yp=(df['y'].mean())


#Fórmula B1
b1= (sxy-(1/n)*(sx*sy))/((s2x)-(1/n)*pow(sx,2))
b0= yp-b1*xp

#Regresión
##ols: Método de mínimos cuadrados
reg= smf.ols('y~x', data=df)
res=reg.fit()

df['ypre']= res.predict(df['x'])


#Error
##SSR [Error de Regresión]
ssr= res.mse_model

##SSE [Error suma de Cuadrados]
sse= res.ssr

##SST [Cuadrados totales]
sst= ssr + sse

##MSE [Cuadrado medio del error]
mse = res.mse_resid

##SE [Estándar del error]
se= math.sqrt(mse)

##MSR [Grados de libertad del error]
msr= ssr/1

#Tabla
t=Texttable()
#Linea por línea, inicia con la cabecera
t.add_rows([['Fuente', 'DF', 'SS', 'MS', 'F'],
           ['Regresión', 1, ssr, msr, (msr/mse)],
           ['Error', n-2, sse, sse/(n-2), ''],
           ['Total', n-1, sst, '', '']           
           ])
print(t.draw())

#Anova
anova=sm.stats.anova_lm(res, typ=2)
#print(anova)

##Coeficiente de Correlación
R=ssr/sst

print('R: ', res.rsquared)

#Variables
x= df['x']
y= df['y']

##Intersección y Pendiente
b,m = polyfit(x,y,1)


#Graficar
plt.plot(x, y, 'o')
plt.plot(x, b+m*x, '-')
plt.show()



#Hipotesis Nula
#Hipotesis Alternativa
rmse= math.sqrt(mse)
sb1= rmse/math.sqrt(s2x-(1/n)*pow(sx,2))
t= b1/sb1


#Prueba t
##95% Confianza
print('t: ', t)
a=0.05/2
q= 1-a
gld= n-2
p=stats.t.ppf(q,gld)

if p<t:
    print('Se rechaza H0, por lo tanto si existe relación entre los datos')
if p>t:
    print('Se acepta H0, por lo tanto no existe relación entre los datos')
    
#Prueba f
##95% Confianza
F= msr/mse
print('F: ', F)    
   
#Grados de libertad 
gln= 1
a=0.05/2
q= 1-a
c=stats.f.ppf(q, dfn=gln, dfd=gld)
print('C: ',c)

if F>c:
    print('Se rechaza H0, por lo tanto el modelo es significativo')

if F<c:
    print('Se rechaza H0, pero el modelo no es significativo')


#Residuales
fig,ax= plt.subplots(figsize=(12, 8))
#fig= sm.graphics.plot_fit(res, 'x', ax=ax)


#Intervalo de confianza 95%
ax= sns.regplot(x=df['x'], y=df['y'], color='g', ci=95)
plt.title('Gráfica Residual de 1969 a 2009', fontsize= 20)

#Prediccion
df['ips']=df['x'].apply(lambda x: p*rmse*math.sqrt(1+1/n+(pow((x-xp),2))/(s2x-1/n*pow(sx,2))))
df['ics']=df['x'].apply(lambda x: p*rmse*math.sqrt(1/n+(pow((x-xp),2))/(s2x-1/n*pow(sx,2))))

df['sup']=df['ypre']+df['ips']
df['inf']=df['ypre']-df['ips']

print(df[['ypre','ips','sup','inf']])

#Intervalos de confianza
df['sup']=df['ypre']+df['ics']
df['inf']=df['ypre']-df['ics']

print(df[['ypre','ics','sup','inf']])

ax.plot(x,y)
plt.show()

