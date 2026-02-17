# Integrantes del equipo:
# - Cano Nieto Carlos Arturo
# - Cortes Bolaños Angel David
# - Martinez Garcia Luis Angel
# - Rodriguez Jaramillo Alejandro
# - Urbano Meza Joseph Gael
# Fecha: 17 de febrero de 2026

#Definimos primero todo el alfabeto 
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Pedimos los datos al usuario y los convertimos a minúsculas para evitar problemas con mayúsculas. 
texto_original = input("Escribe el mensaje (en minúsculas): ").lower()
n = int(input("Introduce el número de desplazamiento: "))

# --- AQUI EMPIEZA EL PROCESO DE CIFRADO ---
texto_cifrado = ""

for letra in texto_original:
    if letra in abc:
        indice_actual = abc.index(letra)
        nuevo_indice = (indice_actual + n) % 26
        texto_cifrado += abc[nuevo_indice]
    else:
        texto_cifrado += letra

# --- PROCESO DE DESCIFRADO ---
texto_descifrado = ""

for letra in texto_cifrado:
    if letra in abc:
        indice_actual = abc.index(letra)
        nuevo_indice = (indice_actual - n) % 26
        texto_descifrado += abc[nuevo_indice]
    else:
        texto_descifrado += letra

# --- RESULTADOS ---
print("\n" + "="*30)
print(f"Original:   {texto_original}")
print(f"Cifrado:    {texto_cifrado}")
print(f"Descifrado: {texto_descifrado}")
print("="*30)