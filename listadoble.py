# ---------------------------------------------------------
# Ejemplo: Lista doble con tamaños variables
# ---------------------------------------------------------

ventas = []          # Lista doble: aquí guardaremos las ventas de cada día
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

print("CAPTURA DE VENTAS (0 para terminar cada día)\n")

# ---------------------------------------------------------
# CAPTURA DE DATOS
# ---------------------------------------------------------
'''
for dia in dias:
    print(f"Capturando ventas del día {dia}:")
    ventas_diarias = []     # Lista temporal para las ventas de este día
    while True:
        venta = int(input("  Ingresa venta (0 para terminar el día): "))
        if venta == 0:
            break           # Termina la captura de este día
        elif venta < 0:
            print("Valor no válido")
            continue
        ventas_diarias.append(venta)  # Agregar venta a la lista del día
    ventas.append(ventas_diarias)# Guardar la lista del día en la lista doble
    print(f"  Ventas capturadas para {dia}: {ventas_diarias}\n")
'''
ventas = [[10,20,30,40],
          [5,10,15,20,25,30,35,40],
          [10,100],
          [25,50,75],
          [100,80,60,40]]
# ---------------------------------------------------------
# SUMA DE VENTAS (FORMA 1: recorriendo elementos)
# ---------------------------------------------------------

print("\nSUMA DE VENTAS (FORMA 1: recorriendo elementos)\n")

venta_total = 0
venta_por_dia = []
for dia in ventas:
    suma_dia = 0
    for venta in dia:       # Recorremos directamente los elementos
        suma_dia += venta
    venta_por_dia.append(suma_dia)
    venta_total += suma_dia

print("Venta diaria:", venta_por_dia)
print("Venta total de la semana:", venta_total)

# ---------------------------------------------------------
# SUMA DE VENTAS (FORMA 2: recorriendo por índices)
# ---------------------------------------------------------

print("\nSUMA DE VENTAS (FORMA 2: recorriendo por índices)\n")

venta_total = 0
venta_por_dia = [0,0,0,0,0]
for i in range(len(ventas)):          # i = índice del día
    suma_dia = 0
    for j in range(len(ventas[i])):   # j = índice de la venta dentro del día
        suma_dia += ventas[i][j]
    print(f"{dias[i]}: {suma_dia}")
    venta_por_dia[i] = suma_dia
    venta_total += suma_dia

print("Venta diaria:", venta_por_dia)
print("Venta total de la semana:", venta_total)
