import os
os.system('cls' if os.name == 'nt' else 'clear')

#Cliclo for
#for i in range(10):
#    print(i)

#range(inicio, fin, incremento)
#for i in range(2,22,2):
#   print(i)


#Ciclo for con listas
#lista=["uno","dos","tres","cuatro","cinco"]
#for item in lista:
#    print(item)


#inversión de una lista
#for item in reversed(lista):
#    print(item)

#Ciclo for con tuplas
#tupla=("uno","dos","tres","cuatro","cinco")
#for item in tupla:
#    print(item)


#Ciclo for con diccionarios
#diccionario = {
 #   "curso": "Python TOTAL",
  #  "clase": "Ciclos",
   # "tema": "for",
    #"duración": "1 trimestre",
    #"profesor": "Luis Teruel",
#}

#print(diccionario)
#for llave in diccionario:
#    print(llave, ":", diccionario[llave])


#tablas de multiplicar con for
tablas=int(input("Que tabla de multiplicar? "))
for i in range(1,11):
    print(f"{tablas} x {i} = {i*tablas}")
    print("")

factorial = int(input("Introduce un valor para calcular el factorial: "))
result = 1
for i in range(1, factorial + 1):
    result = result * i

print("El factorial de", factorial, "es", result)
print("")