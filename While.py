# imprime 10 valores con el ciclo while

#i = 0
#while i < 10:
#    print(i)
#    i += 1

#print ("ciclo controlado por banderin")

#while True:
#    entrada = input("Ingresa S para salir")
#    if entrada == 'S':
#        break

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("ciclo controlado por bandera")
bandera = True
while bandera != False:
    bandera = input("Ingresa S para salir")
    print(bandera.upper())
    salir=bandera.upper()
    if salir == 'S':
        bandera = False
        print("Saliste del ciclo")