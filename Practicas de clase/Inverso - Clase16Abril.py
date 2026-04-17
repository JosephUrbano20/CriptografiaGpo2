def calcular_inversos_limite_e(e, p):
    # n es tanto el número a evaluar como la cantidad de soluciones
    print(f"\n--- Calculando {e} soluciones para el inverso de {e} módulo {p} ---")
    try:
        # pow(base, -1, mod) calcula el inverso multiplicativo modular en Python 3.8+
        inverso_base = pow(e, -1, p)
        
        # Generamos exactamente 'n' soluciones
        for k in range(e):
            solucion = inverso_base + (k * p)
            print(f"Solución {k+1}: {solucion}")
            
    except ValueError:
        print(f"\nError: El número {e} no tiene inverso multiplicativo módulo {p}.")
        print("💡 Recuerda: Para que exista un inverso, el número y el módulo deben ser coprimos (su único divisor común debe ser el 1).")

# Bloque principal
try:
    print("Cálculo de Inversos Modulares")
    print("-" * 30)
    e = int(input("Ingresa el número a evaluar (n) y límite de soluciones: "))
    
    if e > 0:
        p = int(input("Ingresa el módulo (p): "))
        calcular_inversos_limite_e(e, p)
    else:
        print("Por favor, ingresa un número 'n' mayor a 0.")
except ValueError:
    print("Error: Entrada no válida. Debes ingresar números enteros.")