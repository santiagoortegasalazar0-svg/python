
codigo = input("Ingrese el codigo: ")
nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")

dia = int(input("Ingrese el dia de nacimiento: "))
mes = int(input("Ingrese el mes de nacimiento: "))
anio = int(input("Ingrese el año de nacimiento: "))


fecha = (dia, mes, anio)

registro = (codigo, nombre, apellido, fecha)

print("Nombre completo:", registro[1], registro[2])
print("Año de nacimiento:", registro[3][2])
print("Cantidad de elementos:", len(registro))
print("Cuarto elemento:", registro[3])