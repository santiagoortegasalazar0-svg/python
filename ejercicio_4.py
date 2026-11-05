
numeros = []

while True:
    numero = int(input("Ingrese un numero (99999 para terminar): "))

    if numero == 99999:
        break

    numeros.append(numero)


pares = []
impares = []


for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)


print("Pares:", pares, "(total", len(pares), ")")
print("Impares:", impares, "(total", len(impares), ")")