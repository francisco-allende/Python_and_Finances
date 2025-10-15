# ------------------------------------------------------------------------------------
# Ejercicio - Análisis del dataset de propinas (Seaborn)
# ------------------------------------------------------------------------------------
# Lo primero que deben hacer es abrir el archivo de la unidad llamado “Notebook_Ejercicios_Clase_4” 
# en el cual encontrarán un código ya escrito que les permitirá acceder al dataset de propinas 
# de la librería seaborn. A partir de ese DataFrame llamado `tips` se pide que hagan lo siguiente:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el conjunto de datos
tips = sns.load_dataset("tips")

# Ver las primeras filas para confirmar que se cargó
print(tips.head())

# Histograma de propinas
def mostrarEjemplo():
    plt.figure(figsize=(8, 6)) #este es el lienzo donde vamos a dibujar
    
    #sns.histplot Es la función de Seaborn para crear histograma
    
    #tips["tip"] Es el conjunto de datos numéricos que querés graficar.
        #En este caso, tips es el dataset de ejemplo de Seaborn con datos de propinas.
        #tips["tip"] selecciona la columna de propinas (un Series de pandas).

    #bins Define en cuántos intervalos (barras) se agrupan los datos.
        #Más bins → gráfico más detallado (pero puede volverse ruidoso)
        #bins=50 → muchas barras finas
        
        #Menos bins → gráfico más general o “suavizado”
        #bins=5 → 5 barras grandes
    
    #kde Kernel Density Estimate (Estimación de Densidad de Núcleo). es para que dibuje la curva de distribución. 
    # Si lo sacamos no hay curva, solo barras
    sns.histplot(tips["tip"], bins=20, kde=True) 
    plt.title("Distribución de Propinas")
    plt.xlabel("Propina ($)")
    plt.ylabel("Frecuencia")
    plt.show()

#mostrarEjemplo()

# 1) Histograma de propinas:
#    Crear un histograma que muestre la distribución de las propinas dadas en el restaurante.

def plot_histogram():
    plt.figure(figsize=(8, 6))
    sns.histplot(tips["tip"], bins=20, kde=True)
    plt.title("Distribución de Propinas")
    plt.xlabel("Propina ($)")
    plt.ylabel("Frecuencia")
    plt.show()

plot_histogram()

# 2) Gráfico de dispersión:
#    Realizar un gráfico de dispersión que muestre la relación entre el total de la factura y la propina.

#la propina depende del total de la factura. 
#por ende, propina es la variable dependiente (eje Y) y total_bill es la variable independiente (eje X).

def plot_scatter():
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=tips['total_bill'], y=tips['tip'], alpha=0.5)
    plt.title("Relación entre el total de la factura y la propina")
    plt.xlabel("Total de la Factura ($)")
    plt.ylabel("Propina ($)")
    plt.show()

plot_scatter()

# 3) Boxplot por día:
#    Crear un boxplot que compare la distribución de propinas para cada día de la semana.


def plot_boxplot():
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=tips, x='day', y='tip', palette='pastel')
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.title("Distribución de Propinas por Día")
    plt.xlabel("Día de la Semana")
    plt.ylabel("Propina ($)")
    plt.show()

plot_boxplot()

# 4) Gráfico de barras apiladas:
#    Generar un gráfico de barras apiladas que muestre la proporción de propinas en función del día 
#    y del momento del día (almuerzo o cena).

def plot_stacked_bar():
    # Agrupar los datos
    propinas_por_dia_y_momento = tips.groupby(['day', 'time'])['tip'].sum().unstack()

    # Crear gráfico de barras apiladas
    propinas_por_dia_y_momento.plot(
        kind='bar',
        stacked=True,
        figsize=(8,6),
        color=['skyblue', 'salmon']
    )

    plt.title("Propinas por Día y Momento del Día")
    plt.xlabel("Día de la Semana")
    plt.ylabel("Total de Propinas ($)")
    plt.legend(title="Momento del Día")
    plt.show()

plot_stacked_bar()

# 5) Gráfico de violín por género:
#    Crear un gráfico de violín que muestre la distribución de propinas para hombres y mujeres.

def plot_violin():
    plt.figure(figsize=(8, 6))
    sns.violinplot(data=tips, x='sex', y='tip', palette='pastel')
    plt.title("Distribución de Propinas por Género")
    plt.xlabel("Género")
    plt.ylabel("Propina ($)")
    plt.show()

plot_violin()

# 6) Mapa de calor de correlación:
#    Calcular la matriz de correlación entre las variables numéricas y crear un mapa de calor que 
#    visualice estas correlaciones.
#    (TIP: pueden hacerlo directamente con Pandas con el método `.corr()`)

def plot_correlation_map():
    plt.figure(figsize=(8, 6))
    numeric = tips.select_dtypes(include='number')
    corr = numeric.corr()    
    sns.heatmap(corr, annot=True, cmap='YlGnBu', fmt=".2f")
    plt.title("Mapa de Calor de Correlación")
    plt.xlabel("Variables")
    plt.ylabel("Variables")
    plt.show()

plot_correlation_map()