"""Ejercicio 4 — Diccionarios.
Escribe un script que reciba el diccionario:
alumnos = {
    "Ana": [90, 80, 100],
    "Luis": [70, 85, 90],
    "Mia": [100, 95, 98]
}
Construya un nuevo diccionario donde cada alumno tenga su promedio.
Encuentre el alumno con el promedio más alto. Escribe el nombre del
alumno y su promedio.
"""
alumnos = {
    "Ana": [90, 80, 100],
    "Luis": [70, 85, 90],
    "Mia": [100, 95, 98]
}
alum_prom = dict()
for nombre in alumnos.keys():
    prom = 0
    cant = len(alumnos[nombre])
    for cal in alumnos[nombre]:
        prom += cal
    prom /= cant
    alum_prom[nombre] = prom
for a,p in alum_prom.items():
    print(a,p)

# Ejercicio 4 — Diccionarios
# Calcula el promedio de cada alumno y encuentra el que tiene el promedio más alto

alumnos = {
    "Ana": [90, 80, 100],
    "Luis": [70, 85, 90],
    "Mia": [100, 95, 98]
}

alum_prom = dict()

# Calcular promedios
for nombre in alumnos.keys():
    suma = 0
    cant = len(alumnos[nombre])
    for cal in alumnos[nombre]:
        suma += cal
    promedio = suma / cant
    alum_prom[nombre] = promedio

# Encontrar al alumno con el promedio más alto
mejor_alumno = ""
mejor_promedio = 0

for nombre, promedio in alum_prom.items():
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_alumno = nombre

# Mostrar resultado
print(f"El alumno con el promedio más alto es {mejor_alumno} con {mejor_promedio:.2f}")
    
