def solution(a):

    equipo1 = 0
    equipo2 = 0

    for i in range(len(a)):

        if i % 2 == 0:
            equipo1 += a[i]
        else:
            equipo2 += a[i]

    return [equipo1, equipo2]


cantidad = int(input("Ingrese la cantidad de personas: "))

if cantidad <= 0:
    print("Debe ingresar una cantidad mayor que cero.")

else:

    pesos = []

    for i in range(cantidad):

        peso = int(input("Ingrese el peso de la persona " + str(i + 1) + ": "))

        while peso <= 0:
            print("El peso debe ser mayor que cero.")
            peso = int(input("Ingrese nuevamente el peso: "))

        pesos.append(peso)

    resultado = solution(pesos)

    print("Pesos ingresados:", pesos)
    print("Resultado:", resultado)