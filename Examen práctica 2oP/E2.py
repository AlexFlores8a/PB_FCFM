"""Ejercicio 2 — Tuplas. Escribe un script que reciba la tupla:
puntos = ((2, 3), (5, -1), (0, 0), (-3, 4))
Calcule la distancia de cada punto al origen usando:
d=(x**2+y**2)**0.5
Genere una nueva tupla con las distancias y escriba la tupla resultante."""
puntos = ((2, 3), (5, -1), (0, 0), (-3, 4))
lista = []
for coord in puntos:
    d = (coord[0]**2 + coord[1]**2)**0.5
    lista.append(d)
tupla = tuple(lista)
print(tupla)

# Ejercicio 2 — Tuplas
# Calcula la distancia de cada punto al origen

puntos = ((2, 3), (5, -1), (0, 0), (-3, 4))
lista = []

for coord in puntos:
    d = (coord[0]**2 + coord[1]**2)**0.5
    lista.append(d)

tupla_distancias = tuple(lista)
print(tupla_distancias)
