n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

if n <= 0:
    print("El tamaño debe ser mayor que cero.")

else:
    matriz1 = []
    numero = 1

    for i in range(n):
        fila = []

        for j in range(n):
            fila.append(numero)
            numero += 1

        matriz1.append(fila)

    matriz2 = []

    for i in range(n):
        fila = []

        for j in range(n):
            if i % 2 == 0:
                fila.append(j + 1)
            else:
                fila.append(n - j)

        matriz2.append(fila)

    print("\nPRIMERA MATRIZ")

    for fila in matriz1:
        print(fila)

    print("\nSEGUNDA MATRIZ")

    for fila in matriz2:
        print(fila)