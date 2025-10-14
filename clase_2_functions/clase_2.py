numA = 10
numB = 5
numC = -3

# 1) Escribir un programa que determine si un número es positivo o no utilizando una estructura tipo if.
def numPositivo(num):
    if num > 0:
        print(f"El número {num} es positivo")
    else:
        print(f"El número {num} no es positivo")

numPositivo(numA)


#2) Escribir un programa que determine si un número es mayor que otro utilizando una estructura tipo if.
def numMayor(numA, numB):   
    if numA > numB:
        print(f"El número {numA} es mayor que {numB}")      

numMayor(numA, numB)
    
#3) Escribir un programa que imprima los números pares entre 1 y 20 utilizando un bucle for.
def numPares():
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
numPares()

#4) Escribir un programa que calcule la suma de los números naturales del 1 al 100 utilizando un bucle while.
def sumaNaturales():
    suma = 0
    i = 1
    while i < 101:
        suma = suma + i
        i = i + 1
    print(suma)

sumaNaturales()

#5) Escribir un programa que determine si un número es positivo, negativo o cero utilizando una estructura tipo else if.
def numPosNegCero(num):
    if num > 0:            
        print(f"El número {num} es positivo")
    elif num < 0:
        print(f"El número {num} es negativo")
    else:
        print(f"El número {num} es cero")

numPosNegCero(numC)

#6) Escribir un programa que determine si un año es bisiesto o no utilizando estructuras de control condicionales.
import datetime
def esBisiesto():
    if datetime.datetime.now().year % 4 == 0 and (datetime.datetime.now().year % 100 != 0 or datetime.datetime.now().year % 400 == 0):
        print(f"El año {datetime.datetime.now().year} es bisiesto")     
    else:
        print(f"El año {datetime.datetime.now().year} no es bisiesto")

esBisiesto()

#7) Dados 3 números y asumiendo que corresponden a los lados de un triángulo, clasificarlo en
#equilátero, isósceles o escaleno.

#8) Una vez realizados todos los puntos anteriores, declarar todos esos programas como funciones y 
#prueben corriéndolos como tal. Pueden aprovechar y hacer lo mismo con los ejercicios de la guía 1 y 
#también con las siguientes más adelante.

#9) Escribir una función llamada areatriangulo que acepte como argumentos 2 valores numéricos y 
#por consiguiente devuelva el área del triángulo.

#10) Escribir una función que verifique si un número es primo o no. La respuesta de salida debería ser 
#de la siguiente forma: “El número XXX es/no es un numero primo”. Donde XXX debería ser el 
#valor del argumento pasado a la función.

def esPrimo(num):
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                print(f"El número {num} no es un número primo")
                break
        else:
            print(f"El número {num} es un número primo")
    else:
        print(f"El número {num} no es un número primo")

esPrimo(numA)
esPrimo(numB)   
esPrimo(numC)

#11) Escribir una función llamada espalindromo que tome como argumento de entrada una cadena de
#texto y que devuelva si la misma es un palíndromo.

#12) Escribir funciones que permitan hacer pasaje de unidades, por ejemplo:
#a) De Celsius a Fahrenheit
#b) De km a millas
#c) De libras a kilogramos.
#d) De atmosferas a hectopascales
#e) De km/h a m/
