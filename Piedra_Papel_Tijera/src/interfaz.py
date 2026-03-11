def obtener_eleccion_usuario():
    """Captura y valida la entrada del usuario a través de la consola.

    Muestra un menú con las opciones (Piedra, Papel, Tijera) y asegura 
    que el usuario introduzca un número válido entre 1 y 3.

    Returns:
        str: La jugada elegida ("Piedra", "Papel" o "Tijera").
    """
    while True:
        print("\nElige tu jugada:")
        print("1. 🪨 Piedra")
        print("2. 📄 Papel")
        print("3. ✂️ Tijera")
        
        try:
            opcion = int(input("Tu elección (1-3): "))
            if opcion == 1: return "Piedra"
            if opcion == 2: return "Papel"
            if opcion == 3: return "Tijera"
            print("⚠️ Por favor, elige un número entre 1 y 3.")
        except ValueError:
            print("⚠️ Entrada no válida. Introduce un número entero.")

def mostrar_estadisticas(v, d, e):
    """Muestra el resumen final de la partida y el rendimiento del jugador.

    Calcula el porcentaje de victorias y determina si el jugador ganó, 
    perdió o empató el cómputo global de las rondas.

    Args:
        v (int): Número total de victorias.
        d (int): Número total de derrotas.
        e (int): Número total de empates.
    """
    total = v + d + e
    porcentaje = (v / total * 100) if total > 0 else 0
    
    print("\n" + "="*20)
    print("📊 RESUMEN FINAL")
    print(f"Victorias: {v} | Empates: {e} | Derrotas: {d}")
    print(f"Porcentaje de victorias: {porcentaje:.1f}%")
    
    if v > d:
        print("🏆 ¡Ganaste la partida!")
    elif v < d:
        print("❌ Perdiste la partida.")
    else:
        print("🤝 Ha sido un empate global.")
    print("="*20)