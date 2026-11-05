
mercado = []


cantidad = int(input("¿Cuantos productos desea ingresar?: "))


for i in range(cantidad):
    producto = input("Ingrese el producto: ")
    mercado.append(producto)


if cantidad > 0:
    print("Primer producto:", mercado[0])
    print("Ultimo producto:", mercado[-1])
    print("Total de productos:", len(mercado))
else:
    print("La lista esta vacia")