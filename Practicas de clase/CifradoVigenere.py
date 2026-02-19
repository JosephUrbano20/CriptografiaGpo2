# Integrantes del equipo:
# - Cano Nieto Carlos Arturo
# - Cortes Bolaños Angel David
# - Martinez Garcia Luis Angel
# - Rodriguez Jaramillo Alejandro
# - Urbano Meza Joseph Gael
# Fecha: 19 de febrero de 2026

# Definición de variables globales (L = {a, b, c, ..., z})
ALFABETO = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

MODULO = len(ALFABETO)

def E(mensaje, clave):
    resultado = ""
    mensaje = mensaje.lower()
    clave = clave.lower()
    l_k = len(clave)
    
    for i in range(len(mensaje)):
        char_m = mensaje[i]
        
        if char_m in ALFABETO:
            x_i = ALFABETO.index(char_m)
            k_i = ALFABETO.index(clave[i % l_k])
            indice_c = (x_i + k_i) % MODULO
            resultado += ALFABETO[indice_c]
        else:
            resultado += char_m
    return resultado



def D(cripto, clave):
    resultado = ""
    cripto = cripto.lower()
    clave = clave.lower()
    l_k = len(clave)
    
    for i in range(len(cripto)):
        char_c = cripto[i]
        
        if char_c in ALFABETO:
            c_i = ALFABETO.index(char_c)
            k_i = ALFABETO.index(clave[i % l_k])
            indice_m = (c_i - k_i) % MODULO
            resultado += ALFABETO[indice_m]
        else:
            resultado += char_c
            
    return resultado


m = "abcdef"
k = "bcd"

c = E(m, k)
d = D(c, k)

print(f"Mensaje:    {m}")
print(f"Clave:      {k}")
print(f"Cifrado:    {c}")
print(f"Descifrado: {d}")