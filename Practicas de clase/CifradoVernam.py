# Integrantes del equipo:
# - Cano Nieto Carlos Arturo
# - Cortes Bolaños Angel David
# - Martinez Garcia Luis Angel
# - Rodriguez Jaramillo Alejandro
# - Urbano Meza Joseph Gael
# Fecha: 10 de marzo de 2026


import random

def generar_clave(tamano):
    clave = ""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(tamano):
        clave = clave + random.choice(letras)

    return clave


def cifrar(mensaje, clave):
    cifrado = ""

    for i in range(len(mensaje)):
        letra_mensaje = mensaje[i]
        letra_clave = clave[i]

        valor = ord(letra_mensaje) ^ ord(letra_clave)
        cifrado = cifrado + chr(valor)

    return cifrado


def descifrar(cifrado, clave):
    descifrado = ""

    for i in range(len(cifrado)):
        letra_cifrada = cifrado[i]
        letra_clave = clave[i]

        valor = ord(letra_cifrada) ^ ord(letra_clave)
        descifrado = descifrado + chr(valor)

    return descifrado


mensaje = input("Ingresa el mensaje: ")

clave = generar_clave(len(mensaje))

print("Mensaje original:", mensaje)
print("Clave generada:", clave)

texto_cifrado = cifrar(mensaje, clave)
print("Texto cifrado:", repr(texto_cifrado))

texto_descifrado = descifrar(texto_cifrado, clave)
print("Texto descifrado:", texto_descifrado)