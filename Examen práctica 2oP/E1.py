"""Ejercicio 1 — Listas. Escribe un script que reciba la lista:
datos = [3, 10, 5, 10, 2, 8, 3, 7]
Construya una nueva lista que contenga: solo los números únicos
(sin repetir), ordenados de mayor a menor y sin usar set.
Escribe el contenido final de la lista resultante."""
datos = [3, 10, 5, 10, 2, 8, 3, 7]
datos.sort(reverse=True)
i = 0
while i < len(datos):
    while datos.count(datos[i]) > 1:
        datos.remove(datos[i])
        i += 1
    i += 1
print(datos)

