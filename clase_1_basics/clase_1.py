#1) Escribir un código que permita imprimir por pantalla “Hola Mundo”. 
# print("HOLA MUNDO")
 
# 2) Repetir el punto anterior, pero declarando la cadena de texto “Hola Mundo” en una variable tipo string llamada texto y sin la función print (TIP: en una notebook, llamando directamente a la variable). 
msj = "Hola mundo"
msj #al parecer asi fuera de un .py prnitea igual

# 3) Si los puntos anteriores no salen, utilizar el comando help() en una línea de código o en la consola para acceder al apartado de ayuda. Indagar la documentación para lograr los ejercicios 1 y 2. 

# 4) Crear 3 variables llamadas x y z y asignarles los siguientes valores respectivamente: 3 ”esto es una cadena de texto” 1.5 
x = 3
y = 'esto es una cadena de texto'
z =  1.5

# 5) Mediante la función type averiguar qué tipos de variables son las declaradas en el punto anterior. 

arr = [x, y, z]
for var in arr:
    print(type(var))

# 6) Buscar en internet o en los archivos del curso 2 librerías/paquetes que vengan preinstalados en Python y cargarlos en la notebook/archivo .py. También hacer lo mismo, pero con 1 o 2 librerías que no vengan por defecto, por lo que será necesario instalarlas antes. 
# 

import math 
from datetime import datetime as date
import requests
import pandas as pd

print(math.floor(z))
print("hoy es ", date.now().strftime("%d/%m/%y"))

r = requests.get("https://github.com/francisco-allende?tab=repositories")
print(r.status_code)

datos = {"Nombre" :["pepe", "lorna"], "Edad": [20, 60] }
df = pd.DataFrame(datos)
print(df)

# 7) Crear y definir 2 variables llamadas a y b que tomen como valor 20 y 3 respectivamente. Luego realizar las siguientes operaciones: 
# a. La suma de a y b. 
# b. La resta de a y b como también b y a. 
# c. Multiplicar a y b 
# d. Dividir a y b, como también b y a.
# e. Buscar el resto de las operaciones realizadas en el punto d. 
# f. Crear una nueva variable tipo bool y que devuelva si a y b son iguales. 
# g. Repetir el punto f pero que devuelva si son distintas 
# h. Repetir el mismo punto, pero ahora si a es mayor a b 
# i. Ídem, pero si b es mayor que a 

a = 20
b = 3
operadores = ["+", "-", "*", "/", "%", "==", "!=", ">", "<"]

def calcular(numA, numB, operador):
    if operador == "+":
        return numA + numB
    elif operador == "-":
        return numA - numB
    elif operador == "*":
        return numA * numB
    elif operador == "/":
        return numA / numB
    elif operador == "%":
        return numA % numB
    elif operador == "==":
        return numA == numB
    elif operador == "!=":
        return numA != numB
    elif operador == ">":
        return numA > numB
    elif operador == "<":
        return numA < numB
    else:
        return "Operador no válido"

for op in operadores:
    print(calcular(a, b, op))

# 8) Realizar otros tipos de operaciones a elección, como por ejemplo: raíz, logaritmo, potencia, etc.. entre a y b. 
