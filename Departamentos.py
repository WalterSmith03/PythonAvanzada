import os
os.system('cls' if os.name == 'nt' else 'clear')

# Solicitar la contraseña al usuario
contrasena = "UTH123"
ingresada = input("Ingresa la contraseña: ")

# Verificar si la contraseña ingresada es correcta
if ingresada == contrasena:

    print("Contraseña correcta. Acceso permitido.") 
else:

    print("Contraseña incorrecta. Acceso denegado.")
    exit()

departamentos = {
    "Cortés": {
        "San Pedro Sula": "0501",
        "Choloma": "0502",
        "Omoa": "0503",
        "Pimienta": "0504",
        "Potrerillos": "0505",
        "Puerto Cortés": "0506",
        "San Antonio cortés": "0507",
        "San Francisco De Yojoa": "0508",
        "San Manuel Cortes": "0509",
        "Santa Cruz De Yojoa": "0510",
        "Villanueva": "0511",
        "La Lima": "0512",
    },
    "Copan": {
        "Santa Rosa de Copan": "0401",
        "Cabañas": "0402",
        "Concepcion": "0403",
        "Copan Ruinas": "0404",
        "Corquin": "0405",
        "Cucuyagua": "0406",
        "Dolores": "0407",
        "Dulce Nombre": "0408",
        "El Paraiso": "0409",
        "Florida": "0410",
        "La Jigua": "0411",
        "La Union": "0412",
        "Nueva Arcdia": "0413",
        "San Agustin": "0414",
        "San Antonio": "0415",
        "San Jeronimo": "0416",
        "San Jose": "0417",
        "San Juan de Opoa": "0418",
        "San Nicolas": "0419",
        "San Pedro": "0420",
        "Santa Rita": "0421",
        "Trinidad de Copan": "0422",
        "Veracruz": "0423",
    },
    
    "Comayagua": {
        "Comayagua": "0301",
        "ajuterique": "0302",
        "El Rosario": "0303",
        "Esquias": "0304",
        "Humuya": "0305",
        "La Libertad": "0306",
        "Lamaní": "0307",
        "La Trinidad": "0308",
        "Lejamaní": "0309",
        "Meambar": "0310",
        "Minas de Oro": "0311",
        "Ojos de Agua": "0312",
        "San Jeronimo": "0313",
        "San Jose De comayagua": "0314",
        "San José del Potrero": "0315",
        "San Luis": "0316",
        "San Sebastian": "0317",
        "Sguatepeque": "0318",
        "Valle de San Antonio": "0319",
        "Las Lajas": "0320",
        "Taulabé": "0321",
    },
    
    "Francisco Morazán": {
        "Distrito Central": "0801",
        "Alubaren": "0802",
        "Cedros": "0803",
        "Curaren": "0804",
        "El Porvenir": "0805",
        "Guaimaca": "0806",
        "La Libertad": "0807",
        "La Venta": "0808",
        "Lepaterique": "0809",
        "Maraita": "0810",
        "Maraile": "0811",
        "Nueva Armenia": "0812",
        "Ojojona": "0813",
        "Orica": "0814",
        "Reitoca": "0815",
        "Sabanagrande": "0816",
        "San Antonio de Oriente": "0817",
        "San Buenaventura": "0818",
        "San Ignacio": "0819",
        "Cantarranas": "0820",
        "San Miguelito": "0821",
        "Santa Ana": "0822",
        "Santa Lucia": "0823",
        "Talanga": "0824",
        "Tatumbla": "0825",
        "Valle de Angeles": "0826",
        "Villa de San Francisco": "0827",
        "Vallecillo": "0828",
        
    },
    
    "El Paraíso": {
        "Yuscarán": "0701",
        "Alauca": "0702",
        "Danlí": "0703",
        "El Paraíso": "0704",
        "Guinope": "0705",
        "Jacaleapa": "0706",
        "Liure": "0707",
        "Morocelí": "0708",
        "Oropolí": "0709",
        "Potrerillos": "0710",
        "San Antonio De Flores": "0711",
        "San Lucas": "0712",
        "San Matías": "0713",
        "Soledad": "0714",
        "Teupasenti": "0715",
        "Texiguat": "0716",
        "Vado Ancho": "0717",
        "Yauyupe": "0718",
        "Trojes": "0719",
    },
    
    "Atlántida": {
        "La Ceiba": "0101",
        "El Porvenir": "0102",
        "Esparta": "0103",
        "Jutiapa": "0104",
        "La Masica": "0105",
        "San Francisco": "0106",
        "Tela": "0107",
        "Arizona": "0108",
    },
    
    "Choluteca": {
        "Choluteca": "0601",
        "Apacilagua": "0602",
        "Concepcion de Maria": "0603",
        "Duyure": "0604",
        "El Corpus": "0605",
        "El Triunfo": "0606",
        
    },
    
    "Santa Bárbara": {
        "Santa Barbara": "1601",
        "Arada": "1602",
        "Atima": "1603",
        "Azacualpa": "1604",
        "Ceguaca": "1605",
        "San José De Colinas": "1606",
        "Concepción Del Norte": "1607",
        "Concepción Del Sur": "1608",
        "Chinda": "1609",
        "El Nispero": "1610",
        "Gualala": "1611",
        "Ilama": "1612",
        "Macuelizo": "1613",
        "Naranjito": "1614",
        "Nuevo Celilac": "1615",
        "Petoa": "1616",
        "Protección": "1617",
        "Quimistán": "1618",
        "San Francisco De Ojuera": "1619",
        "San Luis": "1620",
        "San Marcos": "1621",
        "San Nicolas": "1622",
        "San Pedro Zacapa": "1623",
        "Santa Rita": "1624",
        "San Vicente Centenario": "1625",
        "Trinidad": "1626",
        "Las Vegas": "1627",
        "Nueva Frontera": "1628",
        
    },
    
    "Valle": {
        "Nacaome": "1701",
        "Alianza": "1702",
        "Amapala": "1703",
        "Aramecina": "1704",
        "Caridad": "1705",
        "Goascorán": "1706",
        "Langue": "1707",
        "San Francisco De Coray": "1708",
        "San Lorenzo": "1709",
    },
    
    "Colón": {
        "Trujillo": "0201",
        "Balfate": "0202",
        "Iriona": "0203",
        "Limón": "0204",
        "Sabá": "0205",
        "Santa Fé": "0206",
        "Santa Rosa de Aguan": "0207",
        "Sonaguera": "0208",
        "Tocoa": "0209",
        "Bonito Oriental": "0210",
    },
    
    "Islas De La Bahía": {
        "Roatán": "1101",
        "Guanaja": "1102",
        "José Santos Guardiola": "1103",
        "Utila": "1104",
    },
    
    "Olancho": {
        "Juticalpa": "1501",
        "Campamento": "1502",
        "Catacamas": "1503",
        "Concordia": "1504",
        "Dulce Nombre De Culmí": "1505",
        "El Rosario": "1506",
        "Esquipulas Del Norte": "1507",
        "Gualaco": "1508",
        "Guarizama": "1509",
        "Guata": "1510",
        "Guayape": "1511",
        "Jano": "1512",
        "La Unión": "1513",
        "Mangulile": "1514",
        "Manto": "1515",
        "Salamá": "1516",
        "San Esteban": "1517",
        "San Francisco De Becerra": "1518",
        "San Francisco De La Paz": "1519",
        "Santa María Del Real": "1520",
        "Silca": "1521",
        "Yocón": "1522",
        "Patuca": "1523",
    },
    
    "Ocotepeque": {
        "Nueva Ocotepeque": "1401",
        "Belén Gualcho": "1402",
        "Concepción": "1403",
        "Dolores Merendón": "1404",
        "Fraternidad": "1405",
        "La Encarnación": "1406",
        "La Labor": "1407",
        "Lucerma": "1408",
        "Mercedes": "1409",
        "San Fernando": "1410",
        "San Francisco Del Valle": "1411",
        "San Jorge": "1412",
        "San Marcoso": "1413",
        "Santa Fé": "1414",
        "Sensenti": "1415",
        "Sinuapa": "1416",
    },
    
    "Lempira": {
        "Gracias": "1301",
        "Belén": "1302",
        "Candelaria": "1303",
        "Cololaca": "1304",
        "Erandique": "1305",
        "Gualcince": "1306",
        "Guarita": "1307",
        "La Campa": "1308",
        "La Iguala": "1309",
        "Las Flores": "1310",
        "La Unión": "1311",
        "La Virtud": "1312",
        "Lepaera": "1313",
        "Mapulaca": "1314",
        "Piraera": "1315",
        "San Andrés": "1316",
        "San Francisco": "1317",
        "San Juan Guarita": "1318",
        "San Manuel Colohete": "1319",
        "San rafael": "1320",
        "San Sebastian": "1321",
        "Santa Cruz": "1322",
        "Talgua": "1323",
        "Tambla": "1324",
        "Tomala": "1325",
        "Valladolid": "1326",
        "Virginia": "1327",
        "San Marcos De Caiquin": "1328",
    },
    
    "Intibuca": {
        "La Esperanza": "1001",
        "Camasca": "1002",
        "Colomoncagua": "1003",
        "Concepción": "1004",
        "Dolores": "1005",
        "intibuca": "1006",
        "Jesus de Otoro": "1007",
        "Magdalena": "1008",
        "Masaguara": "1009",
        "San Antonio": "1010",
        "San Isidro": "1011",
        "San Juan": "1012",
        "San Marcos de la sierra": "1013",
        "San Miguel Guancapla": "1014",
        "Santa Lucia": "1015",
        "Yamaranguila": "1016",
        "San Francisco de Opalaca": "1017",
    },
    
    "Gracias a Dios": {
        "Puerto Lempira": "0901",
        "Brus Laguna": "0902",
        "Ahuas": "0903",
        "Juan Francisco Bulnes": "0904",
        "Ramón Villeda Morales": "0905",
        "Wampusirpe": "0906",
    },
    
    "La Paz": {
        "La Paz": "1201",
        "Aguanqueterique": "1202",
        "Cabañas": "1203",
        "Cane": "1204",
        "Chinacla": "1205",
        "guajiquiro": "1206",
        "Lauterique": "1207",
        "Marcala": "1208",
        "Mercedes de Oriente": "1209",
        "Opatoro": "1210",
        "San Antonio del Norte": "1211",
        "San Jose": "1212",
        "San Juan": "1213",
        "San Pedro de Tutule": "1214",
        "Santa Ana": "1215",
        "Santa Elena": "1216",
        "Santa María": "1217",
        "Santiago de Puringla": "1218",
        "Yarula": "1219",
    },
    
    "Yoro": {
        "Yoro": "1801",
        "Arenal": "1802",
        "El Negrito": "1803",
        "El Progreso": "1804",
        "Jocon": "1805",
        "Morazan": "1806",
        "Olanchito": "1807",
        "Santa Rita": "1808",
        "Sulaco": "1809",
        "Victoria": "1810",
        "Yorito": "1811",
    }
}
# Define una función "calcular_edad(dni)" que calcula la edad de una persona basado en su año de nacimiento, extraído del DNI (posiciones 4 a 8 del string).
def calcular_edad(dni):
    return 2024 - int(dni[4:8])


# Define la función imprimir_resultados() que:

# Solicita el nombre del ciudadano y su DNI.
def imprimir_resultados():
    nombre = input("Por favor ingresar el nombre del ciudadano: ")
    print("")
    dni = input("Ingrese su código de DNI: ")

# Extrae el código del municipio (los primeros 4 caracteres del DNI). 
    codigo_municipio = dni[:4]
    
# Busca el municipio correspondiente en el diccionario departamentos.
    for departamento, municipios in departamentos.items():
        for municipio, codigo in municipios.items():
            if codigo == codigo_municipio:
                nombre_municipio = municipio
                break
    
# Calcula la edad del ciudadano.
    edad = calcular_edad(dni)
    
# Imprime el nombre del ciudadano, el municipio correspondiente y su edad.
    print("")
    print(f"El nombre del ciudadano es: {nombre}")
    print(f"El DNI ingresado corresponde al municipio de: {nombre_municipio}")
    print(f"Edad: {edad} años")
    print("")

# Define la función calcular_promedio() que:

# Solicita las calificaciones del usuario.
def calcular_promedio():
    calificaciones = []
    for _ in range(3):
        print("")
        calificacion = float(input("Ingrese la calificación: "))
        calificaciones.append(calificacion)
    promedio = sum(calificaciones) / len(calificaciones)
    if promedio >= 95:
        print("")
        print(f"El promedio es de {promedio:.2f}. FELICIDADES alcanzaste la Excelencia academica.")
    else:
        print("")
        print(f"El promedio es de {promedio:.2f}. No es de excelencia académica.")

# Define la función imprimir_numeros_impares() que:

# Solicita un número entero positivo del usuario.
def imprimir_numeros_impares():
    print("")
    numero = int(input("Ingrese un número entero positivo: "))
    print("\nNumeros impares desde 1 hasta", numero, ":")
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i)

# Inicia un bucle while True: que muestra un menú con cinco opciones:
while True:
    print("\nMenu:")
    print("1. Inspeccionar los departamentos")
    print("2. Inspeccionar los municipios")
    print("3. EJERCICIO 8 EXAMEN")
    print("4. EJERCICIO 18 EXAMEN")
    print("5. Salir")
    print("")
    opcion = input("Seleccione una opción: ")
    
# Opción 1: Solicita el nombre de un departamento y muestra sus municipios y códigos.
    if opcion == "1":
        print("")
        departamento = input("Ingrese el nombre del departamento: ")
        if departamento in departamentos:
            print("\nMunicipios del departamento:")
            print("")
            for municipio, codigo in departamentos[departamento].items():
                print(f"{municipio} - {codigo}")
        else:
            print("Departamento no encontrado.")
    
# Opción 2: Llama a la función imprimir_resultados().
    elif opcion == "2":
        imprimir_resultados() 

# Opción 3: Llama a la función calcular_promedio().
    elif opcion == "3":
        calcular_promedio()

# Opción 4: Llama a la función imprimir_numeros_impares().
    elif opcion == "4":
        imprimir_numeros_impares()

# Opción 5: Salir del programa.
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion no válida. Por favor, seleccione una opción del menú.")