import random
import os
import platform

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def obtener_eleccion_computadora():
    """Genera una elección aleatoria para la computadora."""
    opciones = ["Piedra", "Papel", "Tijera"]
    return random.choice(opciones)

def obtener_eleccion_usuario():
    """Captura y valida la entrada del usuario."""
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

def determinar_ganador(usuario, pc):
    """
    Compara las elecciones y devuelve el resultado.
    Reglas: Piedra > Tijera, Tijera > Papel, Papel > Piedra.
    """
    if usuario == pc:
        return "Empate"
    
    reglas = {
        "Piedra": "Tijera",
        "Tijera": "Papel",
        "Papel": "Piedra"
    }
    
    if reglas[usuario] == pc:
        return "Victoria"
    else:
        return "Derrota"

def mostrar_estadisticas(v, d, e):
    """Muestra el resumen final y el porcentaje de victorias."""
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

def jugar():
    """Bucle principal que gestiona las rondas y el estado del juego."""
    limpiar_pantalla()
    print("🎮 BIENVENIDO A PIEDRA, PAPEL O TIJERA")
    
    while True:
        try:
            rondas_totales = int(input("\n¿Cuántas rondas quieres jugar? (1-10): "))
            if 1 <= rondas_totales <= 10:
                break
            print("⚠️ Introduce un número entre 1 y 10.")
        except ValueError:
            print("⚠️ Entrada no válida.")

        # Marcadores
    victorias, derrotas, empates = 0, 0, 0

    for r in range(1, rondas_totales + 1):
        print(f"\n--- Ronda {r} de {rondas_totales} ---")
        
        usuario = obtener_eleccion_usuario()
        pc = obtener_eleccion_computadora()
        
        print(f"\n👤 Tú elegiste: {usuario}")
        print(f"🤖 La computadora eligió: {pc}")
        
        resultado = determinar_ganador(usuario, pc)
        
        if resultado == "Victoria":
            print("✨ ¡Ganaste esta ronda!")
            victorias += 1
        elif resultado == "Derrota":
            print("💀 Perdiste esta ronda.")
            derrotas += 1
        else:
            print("⚖️ ¡Es un empate!")
            empates += 1
            
        print(f"Marcador -> Tú: {victorias} | PC: {derrotas} | Empates: {empates}")

    mostrar_estadisticas(victorias, derrotas, empates)

if __name__ == "__main__":
    while True:
        jugar()
        jugar_de_nuevo = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("¡Gracias por jugar!")
            break
        limpiar_pantalla()