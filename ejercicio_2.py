
canciones = []


cantidad = int(input("¿Cuantas canciones desea ingresar?: "))


for i in range(cantidad):
    cancion = input("Ingrese el nombre de la cancion: ")
    canciones.append(cancion)


if cantidad >= 5:
    print("Apertura:", canciones[0:3])
    print("Cierre:", canciones[-2:])
    print("Momento de bailar:", canciones[2:5])
else:
    print("Debe ingresar minimo 5 canciones")