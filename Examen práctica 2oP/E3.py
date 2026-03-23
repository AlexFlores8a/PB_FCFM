"""Ejercicio 3 — Conjuntos. Escribe un script que reciba el conjunto:
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Cree un conjunto B con los cuadrados de cada elemento de A.
Calcule la intersección entre A y B. Escribe el conjunto resultante."""
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
B = set()
for ele in A:
    B.add(ele**2)
inter = A.intersection(B)
print(inter)
