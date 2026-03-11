from src.utilidades import limpiar_pantalla 
from src.logica import obtener_eleccion_computadora, determinar_ganador
from src.interfaz import obtener_eleccion_usuario, mostrar_estadisticas

def jugar():
    """Gestiona el flujo principal de una partida completa.

    Se encarga de:
    1. Solicitar el número de rondas.
    2. Ejecutar el bucle de juego llamando a la lógica y la interfaz.
    3. Mantener el contador de puntos (marcador).
    4. Llamar a la visualización de estadísticas finales.
    """
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
    """Punto de entrada del script. Ejecuta el juego y pregunta si se desea reanudar."""
    while True:
        jugar()
        jugar_de_nuevo = input("\n¿Quieres jugar otra partida? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("¡Gracias por jugar!")
            break
        limpiar_pantalla()