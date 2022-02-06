# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 21:06:39 2022

@author: Isma
"""

"""
Calculadora Condicionales 

1. Suma de 2 números
    Introduce el primer número:
                segundo número:
    Resultado _+_= 
2. Resta
3. Multiplicación
4. División
    error: division by zero=> Indeterminación
5. Cociente a//b
6. Resto de la división a%b
7. Exponención a**b pow(a,b)
8. Salir
"""

print("Calculadora de condicionales")
print("----------------------------------------")
print("\t1.- Suma de dos números             --")
print("\t2.- Resta de dos números            --")
print("\t3.- Multiplicación de dos números   --")
print("\t4.- División de dos números         --") 
print("\t5.- Cociente                        --")
print("\t6.- Resto                           --") 
print("\t7.- Exponenciación de dos números   --")
print("\t8.- Salir")
#print)"\t9.- ")

if(opc==1):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    if (y==0):
        print("Error")
    else:
        print(f"La suma es: {x}+{y}={x+y}")
elif(opc==2):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    if (y==0):
        print("Error")
    else:
        print(f"La resta es: {x}-{y}={x-y}")

elif(opc==3):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    if (y==0):
        print("Error")
    else:
        print(f"La multiplicación es: {x}*{y}={x*y}")
elif(opc==4):
    x=int(input("Introduzca el primer número: "))
    y=int(input("Introduzca el segundo número: "))
    if (y==0):
        print("Error")
    else:
        print(f"La división es: {x}/{y}={x/y}")