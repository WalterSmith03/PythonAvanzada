#EJERCICIO DE BUCLE FOR

#Ingresar N notas, mostrar en lista los numeros pares de forma ascendente y de forma descendente los numeros impares

n=input("Ingresa la cantidad de notas: ")

lista=[]
listo=[]

for i in range(n):
    num=int(input("Ingresa la nota: "))
    if num%2==0:
        lista.insert(i,num)
        lista.sort()
    else:
        listo.insert(i,num)
        listo.sort(reverse=True)

print("Las notas pares son: ",lista)
print("Las notas impares son: ",listo)