
cantidad = int(input("Cantidad de numeros: "))


numeros = []


for i in range(cantidad):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)


buscar = int(input("Numero a buscar: "))


posicion = -1


for i in range(len(numeros)):
    if numeros[i] == buscar:
        posicion = i
        break


if posicion != -1:
    print("El", buscar, "esta en la posicion", posicion)
else:
    print("El", buscar, "no esta en la lista")