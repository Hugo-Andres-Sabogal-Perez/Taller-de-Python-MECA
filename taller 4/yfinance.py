# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 09:37:47 2024

@author: hugos
"""
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


Portafolio_inicial = {"AAPL":0.1, 
                      "PFE" : 0.05, 
                      "JPM" : 0.2, 
                      'HD' :0.25, 
                      'XOM' : 0.25,
                      'TSLA' : 0.15}

activos = list(Portafolio_inicial.keys())

# Descargar datos de cierre ajustado (ajustado por splits y dividendos)
acciones = yf.download(activos, start="2020-01-01", end="2023-12-01")
acciones  = acciones['Close']

benchmark = yf.download('VOO', start="2020-01-01", end="2023-12-01")
benchmark = benchmark['Close']

# Armamamos portafolio

pesos = list(Portafolio_inicial.values())
acciones['portafolio'] = acciones.dot(pesos)

# Evolución de $100
monto_inicial = 100
evol_100 = pd.DataFrame((acciones['portafolio'] / acciones['portafolio'].iloc[0]) * monto_inicial)
evol_100['Benchmark']  =  (benchmark['VOO'] / benchmark['VOO'].iloc[0]) * monto_inicial

# Establecememos tamaño de la figura
fig, ax = plt.subplots(dpi=150, figsize=(13,10))

# Inficamos un Gráfico de barras con los datos obtenidos del groupby y seleccionamos color de preferencia
ax.plot(evol_100.index,evol_100['portafolio'], color='dodgerblue', label='Portafolio')
ax.plot(evol_100.index,evol_100['Benchmark'], color='orange', label = 'Benchmark')


# Nombre del eje x Y tamaño  de latra 12
plt.xlabel('Sector', fontsize=12)

# Nombre del eje y Y tamaño  de latra 12
plt.ylabel('Numero de Contratos', fontsize=12)

# Titulo del gráfico con tamaño de letra 18
plt.title('Cantidad de contratos por sector', fontsize=18)

#
plt.legend()

plt.show()


#### 

lista= []

for i in  Portafolio_inicial:
    
    list_pesos = [yf.Ticker(i).info['sector'],Portafolio_inicial[i]]
    lista.append(list_pesos)

sector_distribution = pd.DataFrame(lista, columns=['Sector', 'Peso'])


sector_distribution = sector_distribution.groupby(by='Sector').sum()

# Crear el gráfico de pastel
fig, ax = plt.subplots(dpi=300)

# Crear un colormap de tonos azules
colors = plt.cm.Blues(np.linspace(0.35, 0.8, len(sector_distribution)))

# Crear el gráfico de pastel
wedges, texts, autotexts=ax.pie(sector_distribution['Peso'], 
       autopct='%1.1f%%', 
       colors=colors,
       wedgeprops={'width': 0.4},
       startangle=90, pctdistance=1.2)

labels = sector_distribution.index
ax.legend(wedges, labels, title="Sectores", loc="center left", bbox_to_anchor=(1.05, 0, 0.5, 1))


# Mostrar el gráfico
plt.title("Composición por sector")
plt.show()


# Moneda
lista= []

for i in  Portafolio_inicial:
    
    list_pesos = [yf.Ticker(i).info['currency'],Portafolio_inicial[i]]
    lista.append(list_pesos)

currency_distribution = pd.DataFrame(lista, columns=['Currency', 'Peso'])

currency_distribution = currency_distribution.groupby(by='Currency').sum()

# Crear el gráfico de pastel
fig, ax = plt.subplots(dpi=300)

# Crear un colormap de tonos azules
colors = plt.cm.Blues(np.linspace(0.35, 0.8, len(currency_distribution)))

# Crear el gráfico de pastel
wedges, texts, autotexts=ax.pie(currency_distribution['Peso'], 
       autopct='%1.1f%%', 
       colors=colors,
       wedgeprops={'width': 0.4},
       startangle=90, pctdistance=1.2)

labels = currency_distribution.index
ax.legend(wedges, labels, title="Currency", loc="center left", bbox_to_anchor=(1.05, 0, 0.5, 1))


# Mostrar el gráfico
plt.title("Composición por moneda")
plt.show()

lista=[]

for i in  Portafolio_inicial:
    
    list_pesos = [yf.Ticker(i).info['country'],Portafolio_inicial[i]]
    lista.append(list_pesos)

country_distribution = pd.DataFrame(lista, columns=['country', 'Peso'])

country_distribution = country_distribution.groupby(by='country').sum()


# Crear el gráfico de pastel
fig, ax = plt.subplots(dpi=300)

# Crear un colormap de tonos azules
colors = plt.cm.Blues(np.linspace(0.35, 0.8, len(country_distribution)))

# Crear el gráfico de pastel
wedges, texts, autotexts=ax.pie(country_distribution['Peso'], 
       autopct='%1.1f%%', 
       colors=colors,
       wedgeprops={'width': 0.4},
       startangle=90, pctdistance=1.2)

labels = country_distribution.index
ax.legend(wedges, labels, title="Country", loc="center left", bbox_to_anchor=(1.05, 0, 0.5, 1))


# Mostrar el gráfico
plt.title("Composición por País")
plt.show()
