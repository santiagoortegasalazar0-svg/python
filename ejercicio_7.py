
cantidad = int(input("Cantidad de temperaturas: "))


temperaturas = []

for i in range(cantidad):
    temperatura = float(input("Ingrese una temperatura: "))
    temperaturas.append(temperatura)


if cantidad > 0:

    
    media = sum(temperaturas) / cantidad


    superiores = []


    for temperatura in temperaturas:
        if temperatura >= media:
            superiores.append(temperatura)


    print("Temperatura media:", media)
    print("Temperaturas >= media:", superiores)
    print("Total:", len(superiores))

else:
    print("No se ingresaron temperaturas")