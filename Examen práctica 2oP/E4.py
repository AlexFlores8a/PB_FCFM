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
    
