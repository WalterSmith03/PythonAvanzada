alumnos = {
    "Walter Eduardo Rápalo Smith": 20,
    "Anthony Amaya": 19,
    "Ronald Bustillo": 24,
}

print(alumnos["Walter Eduardo Rápalo Smith"])

alumnos["Tommy Montufar"] = 19,
alumnos["Angel Perez"] = 19,
alumnos["Lucas Bautistas"] = 19,
alumnos["Stanley Ford"] = 18,


del(alumnos["Ronald Bustillo"])

for alumno, años in alumnos.items():
    print(f"El alumno {alumno} tiene {años} años")

print("")