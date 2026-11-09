def superReducedString(s):

    pila = []

    for letra in s:

        if len(pila) > 0 and pila[-1] == letra:
            pila.pop()

        else:
            pila.append(letra)

    if len(pila) == 0:
        return "Empty String"

    else:
        return "".join(pila)


cadena = input("Ingrese una cadena de letras minusculas: ")

resultado = superReducedString(cadena)

print("Resultado:", resultado)