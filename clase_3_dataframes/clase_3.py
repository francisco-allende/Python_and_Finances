#Lo primero que deben hacer es abrir el archivo de la unidad llamado “Notebook_Ejercicios_Clase_3” en el 
#cual encontraran un código ya escrito que les permitirá acceder al dataset de vinos de la librería sklearn. A 
#partir de ese DataFrame se pide que hagan de forma secuencial:

import pandas as pd
from sklearn.datasets import load_wine   #obtenemos los datos de esta libreria

# Cargamos el conjunto de datos de vinos
wine = load_wine()

# Creamos un DataFrame con los datos
df_wine = pd.DataFrame(data=wine.data, columns=wine.feature_names)

# Mostramos las primeras filas del DataFrame
#print(df_wine.head())


#1) Crear un nuevo DataFrame llamado df_wine_acid que incluya todos los vinos cuya malic_acid sea  mayor a 1.5.

filtro_malic = df_wine['malic_acid'] > 1.5
df_wine_acid = df_wine[filtro_malic]
print("Malic acid mayor a 1.5:")
print(df_wine_acid[['malic_acid']]) #doble corchete para verlo como dataframe 


#2) Crear un nuevo DataFrame llamado df_wine_alcohol que tenga todos los vinos cuyo alcohol sea  mayor a 14.

filtro_alcohol  = df_wine['alcohol'] > 14
df_wine_alcohol = df_wine[filtro_alcohol]
print("Alcohol mayor a 14")
print(df_wine_alcohol[['alcohol']])

#3) Concatenar estos 2 DataFrames creados en uno nuevo llamado df_wine_acid_and_alcohol.

df_wine_acid_and_alcohol = pd.concat([df_wine_acid, df_wine_alcohol])
print("Concatenacion filtro malic acid & alcohol")
print(df_wine_acid_and_alcohol) #concat es un OR, por ende, tendremos alcohol > 14 o malic_acid > 1.5 

#4) Agregar una nueva columna al DataFrame df_wine_acid_and_alcohol llamada “acid_alcohol” cuyos 
#valores deben decir “Warning” en todos los registros.

df_wine_acid_and_alcohol['acid_alcohol'] = 'Warning'
print("Nueva columna Warning")
print(df_wine_acid_and_alcohol)

#5) Con la ayuda de un merge, traer esta nueva columna al DataFrame original llamado df_wine

merge_left = pd.merge(df_wine, df_wine_acid_and_alcohol, how='left') #position left porque no me pide filtrar, sino mantener el original con nueva info
print("Data frame original con la nueva columna Warning")
print(merge_left)

#6) Realizar un análisis de valores nulos en df_wine, los que terminen quedando (si hicieron todo bien, 
#solamente estarían en la nueva columna llamada “acid_alcohol”) reemplazarlos por “No Warning”

#Analizo valores no nulos
df_wine.isnull().sum()

#7) Hacer una agrupación por la columna “acid_alcohol” y calcular la media y desvío estándar para cada variable