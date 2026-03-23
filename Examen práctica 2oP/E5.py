"""Ejercicio 5 — Programación Modular. Supón que existe un archivo
llamado conversiones.py con este contenido:
def km_a_millas(km):
    return km * 0.621371

def millas_a_km(mi):
    return mi / 0.621371
En un archivo main.py, escribe la importación selectiva de ambas
funciones. Y, dentro de if __name__ == "__main__":,
pide al usuario un número e imprime la conversión a millas y a
kilómetros usando las funciones importadas. Escribe el contenido
completo de main.py."""
from conversiones import km_a_millas, millas_a_km

if __name__ == "__main__":
    num = float(input("Dame un número: "))
    print(f"{num} km equivalen a {km_a_millas(num)} millas")
    print(f"{num} millas equivalen a {millas_a_km(num)} km")

