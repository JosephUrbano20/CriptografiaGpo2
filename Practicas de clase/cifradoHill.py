# --- DEFINICIÓN DE ABECEDARIOS (Sin funciones de conversión) ---
# L = {a, b, c, ..., z}
alfabeto_letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# L = {0, 1, 2, ..., 25}
alfabeto_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 
                    18, 19, 20, 21, 22, 23, 24, 25]

# --- UTILIDADES MATEMÁTICAS ---
def calcular_determinante_3x3(m):
    a, b, c = m[0][0], m[0][1], m[0][2]
    d, e, f = m[1][0], m[1][1], m[1][2]
    g, h, i = m[2][0], m[2][1], m[2][2]
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
    return det

def inverso_modular(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def obtener_adjunta_3x3(m, mod):
    adj = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(3):
        for j in range(3):
            sub = []
            for r in range(3):
                if r != i:
                    fila = [m[r][c] for c in range(3) if c != j]
                    sub.append(fila)
            signo = 1 if (i + j) % 2 == 0 else -1
            det_2x2 = (sub[0][0] * sub[1][1] - sub[0][1] * sub[1][0])
            adj[j][i] = (signo * det_2x2) % mod
    return adj

def imprimir_matriz(nombre, matriz):
    print(f"{nombre}:")
    for fila in matriz:
        print(f"  [ {' '.join(str(x).rjust(3) for x in fila)} ]")

# --- PROCESO PRINCIPAL ---
def ejecutar_hill():
    MOD = 26
    
    # 1. Definir Matriz Clave (gybnqkurp) usando búsqueda directa en la lista
    clave_str = "gybnqkurp"
    matriz_k = []
    temp_fila = []
    for char in clave_str:
        # Conversión directa: letra -> número
        temp_fila.append(alfabeto_letras.index(char))
        if len(temp_fila) == 3:
            matriz_k.append(temp_fila)
            temp_fila = []

    print("=== CIFRADO HILL 3x3 ===\n")
    imprimir_matriz("MATRIZ CLAVE (K)", matriz_k)
    
    # 2. Validar Determinante
    det = calcular_determinante_3x3(matriz_k)
    det_mod = det % MOD
    
    print(f"\nDeterminante: {det} (Mod {MOD}: {det_mod})")
    
    if det_mod == 0:
        print("ERROR: El determinante de la matriz es 0. El proceso se interrumpe.")
        return

    inv_det = inverso_modular(det_mod, MOD)
    if inv_det is None:
        print(f"La matriz no es invertible en módulo {MOD}. No se puede descifrar.")
        return

    # 3. CIFRADO (Mensaje: act)
    mensaje_inicial = "caz"
    # Conversión directa: letra -> número
    vec_p = [alfabeto_letras.index(c) for c in mensaje_inicial]
    
    # Multiplicación K * P mod 25
    vec_c = []
    for i in range(3):
        suma = sum(matriz_k[i][j] * vec_p[j] for j in range(3))
        vec_c.append(suma % MOD)
    
    # Conversión directa: número -> letra
    mensaje_cifrado = "".join([alfabeto_letras[n % 26] for n in vec_c])

    # 4. DESCIFRADO
    adjunta = obtener_adjunta_3x3(matriz_k, MOD)
    matriz_inversa = [[(inv_det * adjunta[i][j]) % MOD for j in range(3)] for i in range(3)]
    
    # Multiplicación K^-1 * C mod 25
    vec_d = []
    for i in range(3):
        suma = sum(matriz_inversa[i][j] * vec_c[j] for j in range(3))
        vec_d.append(suma % MOD)
        
    mensaje_descifrado = "".join([alfabeto_letras[n % 26] for n in vec_d])

    # --- SALIDA FINAL ---
    print("\n" + "="*40)
    print(f"MENSAJE INICIAL:    {mensaje_inicial.upper()}")
    print(f"MENSAJE CIFRADO:    {mensaje_cifrado.upper()}")
    print(f"MENSAJE DESCIFRADO: {mensaje_descifrado.upper()}")
    print("="*40 + "\n")
    
    imprimir_matriz("MATRIZ ADJUNTA", adjunta)
    print()
    imprimir_matriz("MATRIZ INVERSA", matriz_inversa)

if __name__ == "__main__":
    ejecutar_hill()