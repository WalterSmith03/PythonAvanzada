#import os
#os.system('cls' if os.name == 'nt' else 'clear')

#saludo="Hola_Mundo"

#try:
    #print(saludo.index('o',4,7))
#except ValueError:
    #print('No se encontro la subcadena')

#index() devuelve la posición de la ultima ocurrencia de una subcadena
#print(saludo.index('o'))


#print(saludo[0:4])


#cedula="1615200300122"
#departamento=cedula[0:2]
#print(departamento)
#municipio=cedula[0:4]

#islower() devuelve True si todos los caracteres de la cadena son minusculas
#print("hola".islower())


#print(saludo[2:6])

#print(saludo[3::3])
#saludo="Hol14a5 8m8u8n8d8o"

#print(saludo[2::2])

#saludo=saludo[::-1]


#print(saludo[::-1])

import os
os.system('cls' if os.name == 'nt' else 'clear')

mensaje="Hola12345"
mensaje2="Hola Mundo"
numero="123455"
decimales="12345.555"

#print(mensaje.isdigit())
#print(numero.isdigit())
#print(decimales.isdigit())


#print(mensaje.isnumeric())
#print(numero.isnumeric())
#print(decimales.isnumeric())


#print(mensaje.isdecimal())
#print(numero.isdecimal())
#print(decimales.isdecimal())

#print(mensaje.isalnum())
#print(mensaje2.isalnum())

#mensaje3=mensaje2.replace("Hola","hello")

#print(mensaje3)


mensaje="adios mundo cruel"
print(mensaje.split(" "))

nombre="Walter*Eduardo*Raplao*Smith"
print(nombre.split("*"))
print(nombre.count("*"))

nombre4=nombre.replace("*"," ")
print(nombre4)




