productos = 5
dias = 7

nombres_dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

ventas = []

for i in range(productos):
    fila = []
    print("\nProducto", i + 1)

    for j in range(dias):
        cantidad = int(input("Ventas del dia " + nombres_dias[j] + ": "))
        fila.append(cantidad)

    ventas.append(fila)

precios = []

for i in range(productos):
    precio = float(input("Ingrese el precio del producto " + str(i + 1) + ": "))
    precios.append(precio)

ingresos_productos = []

for i in range(productos):
    total = 0

    for j in range(dias):
        total += ventas[i][j] * precios[i]

    ingresos_productos.append(total)

ingresos_dias = []

for j in range(dias):
    total = 0

    for i in range(productos):
        total += ventas[i][j] * precios[i]

    ingresos_dias.append(total)

print("\nMATRIZ DE VENTAS")

for fila in ventas:
    print(fila)

print("\nINGRESOS POR PRODUCTO")

for i in range(productos):
    print("Producto", i + 1, ":", ingresos_productos[i])

mayor_producto = ingresos_productos.index(max(ingresos_productos))

print("\nProducto que genera mas ingresos:")
print("Producto", mayor_producto + 1)

print("\nINGRESOS POR DIA")

for j in range(dias):
    print(nombres_dias[j], ":", ingresos_dias[j])

mayor_dia = ingresos_dias.index(max(ingresos_dias))

print("\nDia con mayores ingresos:")
print(nombres_dias[mayor_dia])