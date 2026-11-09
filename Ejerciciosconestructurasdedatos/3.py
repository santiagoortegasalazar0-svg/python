inventario = []

while True:

    print("\n===== INVENTARIO DE LA TIENDA =====")
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto mas reciente")
    print("5. Ordenar productos alfabeticamente")
    print("6. Mostrar numero total de productos")
    print("7. Mostrar inventario")
    print("8. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":

        producto = input("Ingrese el nombre del producto: ").strip()

        if producto != "":
            inventario.append(producto)
            print("Producto agregado correctamente.")
        else:
            print("El nombre no puede estar vacio.")

    elif opcion == "2":

        cantidad = int(input("Cuantos productos desea agregar?: "))

        if cantidad > 0:

            for i in range(cantidad):
                producto = input("Ingrese el producto " + str(i + 1) + ": ").strip()

                if producto != "":
                    inventario.append(producto)
                else:
                    print("Producto vacio, no se agrego.")

            print("Lote registrado correctamente.")

        else:
            print("La cantidad debe ser mayor que cero.")

    elif opcion == "3":

        producto = input("Ingrese el producto que desea eliminar: ").strip()

        if producto in inventario:
            inventario.remove(producto)
            print("Producto eliminado correctamente.")
        else:
            print("El producto no existe en el inventario.")

    elif opcion == "4":

        if len(inventario) > 0:
            eliminado = inventario.pop()
            print("Producto eliminado:", eliminado)
        else:
            print("El inventario esta vacio.")

    elif opcion == "5":

        inventario.sort(key=str.lower)
        print("Inventario ordenado alfabeticamente.")

    elif opcion == "6":

        print("Total de productos:", len(inventario))

    elif opcion == "7":

        if len(inventario) > 0:

            print("\nPRODUCTOS DISPONIBLES")

            for i in range(len(inventario)):
                print(i + 1, "-", inventario[i])

        else:
            print("El inventario esta vacio.")

    elif opcion == "8":

        print("Saliendo del sistema de inventario.")
        break

    else:
        print("Opcion no valida. Intente nuevamente.")