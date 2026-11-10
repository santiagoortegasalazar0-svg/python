import mailbox
from email.utils import parseaddr

archivo = r"C:\Users\USUARIO\Desktop\python\condicional\simulacioncorreo\mbox.txt"
archivo_salida = r"C:\Users\USUARIO\Desktop\python\condicional\simulacioncorreo\mensajes_enviados.txt"

correos = []

mbox = mailbox.mbox(archivo)

for mensaje in mbox:
    remitente = mensaje.get("From")

    if remitente:
        correo = parseaddr(remitente)[1]

        if correo:
            correos.append(correo)

with open(archivo_salida, "w", encoding="utf-8") as salida:

    for correo in reversed(correos):
        mensaje = f"{correo} enviado [ok]"

        print(mensaje)
        salida.write(mensaje + "\n")

print("\nProceso finalizado.")
print(f"Total de mensajes enviados: {len(correos)}")
print(f"Archivo creado: {archivo_salida}")