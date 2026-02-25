"""Actividad 3 - str
Reto 1 — Convertir una frase a snake_case
Descripción: Dada una frase, convertirla a minúsculas y reemplazar
los espacios por guiones bajos.
Dato de prueba: " Hola Mundo desde Python "
Resultado esperado: hola_mundo_desde_python"""
frase1 = " Hola Mundo desde Python "
frase1 = frase1.strip()
frase1 = frase1.replace(" ", "_")
frase1 = frase1.lower()
print("Reto 1:", frase1)

'''Reto 2 — Contar cuántas palabras tiene una frase
Descripción: Separar la frase en palabras y contar cuántas hay.
Dato de prueba: "Los métodos de string son muy útiles"
Resultado esperado: 7'''
frase2 = "Los métodos de string son muy útiles"
frase2 = frase2.split()
print("Reto 2:",len(frase2))

'''Reto 3 — Obtener las iniciales de una frase
Descripción: Tomar la primera letra de cada palabra, concatenarlas
y convertirlo todo a mayúsculas.
Dato de prueba obligatorio: "Universidad Autónoma de Nuevo León"
Resultado esperado: UADNL'''
frase3 = "Universidad Autónoma de Nuevo León"
frase3 = frase3.split()
siglas = ""
for palabra in frase3:
    siglas += palabra[0]
siglas = siglas.upper()
print("Reto 3:", siglas)


'''
Reto 4 — Invertir el orden de las palabras
Descripción: Invertir el orden de las palabras sin alterar su contenido.
Dato de prueba: "Programar en Python es divertido"
Resultado esperado: divertido es Python en Programar'''
frase4 = "Programar en Python es divertido"
frase4 = frase4.split()
frase4.reverse()
frase4inv = ""
for palabra in frase4:
    frase4inv += palabra + " "
frase4inv = frase4inv.strip()
print("Reto 4:", frase4inv)

'''
Reto 5 — Encontrar la palabra más larga
Descripción: Identificar la palabra con mayor longitud dentro de una frase.
Dato de prueba: "Aprender programación requiere práctica constante"
Resultado esperado: programación'''
frase5 = "Aprender programación requiere práctica constante"
frase5 = frase5.split()
palabra = frase5[0]
for p in frase5:
    if len(p) > len(palabra):
        palabra = p
print("Reto 5:", palabra)
