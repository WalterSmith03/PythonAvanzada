#Practica 2

import os
os.system('cls' if os.name == 'nt' else 'clear')

#Raiz cuadrada

import math

print("")
numero = int(input("Ingresa un numero: "))

while numero < 0:
    print("Error: El numero debe ser positivo")
    numero = int(input("Ingresa un numero: "))
print("")
print(f"Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")