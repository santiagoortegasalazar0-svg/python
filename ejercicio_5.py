
cantidad = int(input("¿Cuantas letras va a ingresar?: "))

letras = []

for i in range(cantidad):
    letra = input("Ingrese una letra: ").lower()
    letras.append(letra)

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in letras:
    if letra == "a":
        a += 1
    elif letra == "e":
        e += 1
    elif letra == "i":
        i += 1
    elif letra == "o":
        o += 1
    elif letra == "u":
        u += 1

print("a:", a)
print("e:", e)
print("i:", i)
print("o:", o)
print("u:", u)