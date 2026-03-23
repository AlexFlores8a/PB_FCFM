"""Ejercicio 6 — Programación Orientada a Objetos.
Dado el módulo rectangulo.py:
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)
En un archivo main.py, importa la clase Rectangulo.
Además, dentro de if __name__ == "__main__":, crea dos rectángulos
con los valores (5, 3) y (10, 2). Imprime el área y perímetro de ambos.
Escribe el contenido completo de main.py."""
from rectangulo import Rectangulo

if __name__ == "__main__":
    rect1 = Rectangulo(5,3)
    rect2 = Rectangulo(10,2)
    print(f"""El rectangulo con base de {rect1.base} u y altura de
    {rect1.altura} u, tiene un perimetro de {rect1.perimetro()} u
    y un área de {rect1.area()} u^2""")
    print(f"""El rectangulo con base de {rect2.base} u y altura de
    {rect2.altura} u, tiene un perimetro de {rect2.perimetro()} u
    y un área de {rect2.area()} u^2""")
