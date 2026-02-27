import os
import random
import time


OPCIONES = {
    "1": ("Piedra", "🪨"),
    "2": ("Papel", "📄"),
    "3": ("Tijera", "✂️")
}


def limpiar_pantalla():
    """
    Limpia la consola dependiendo del sistema operativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_bienvenida():
    """
    Muestra la pantalla de bienvenida y las reglas del juego.
    """
    limpiar_pantalla()
    print("=" * 40)
    print("🎮  BIENVENIDO A PIEDRA, PAPEL O TIJERA  🎮")
    print("=" * 40)
    print("\n📜 Reglas del juego:")
    print("🪨 Piedra vence a ✂️ Tijera")
    print("📄 Papel vence a 🪨 Piedra")
    print("✂️ Tijera vence a 📄 Papel")
    print("=" * 40)
    input("\nPresiona ENTER para comenzar...")


def mostrar_menu():
    """
    Muestra el menú principal de opciones del juego.
    """
    print("=" * 40)
    print("🎮  PIEDRA - PAPEL - TIJERA  🎮")
    print("=" * 40)
    for clave, valor in OPCIONES.items():
        print(f"{clave} - {valor[1]} {valor[0]}")
    print("0 - Salir")
    print("=" * 40)


def obtener_opcion_valida():
    """
    Solicita al usuario una opción válida del menú.

    Returns:
        str: Opción elegida ("1", "2", "3" o "0").
    """
    while True:
        opcion = input("👉 Elige una opción: ").strip()

        # Edge case: entrada vacía
        if opcion == "":
            print("⚠️ No puedes dejar el campo vacío.")
            continue

        # Edge case: número negativo
        if opcion.startswith("-"):
            print("⚠️ No se permiten números negativos.")
            continue

        if opcion in OPCIONES or opcion == "0":
            return opcion

        print("⚠️ Opción inválida. Debes elegir 1, 2, 3 o 0.")


def obtener_eleccion_computadora():
    """
    Genera aleatoriamente una elección para la computadora.

    Returns:
        str: Clave de la opción elegida ("1", "2" o "3").
    """
    return random.choice(list(OPCIONES.keys()))


def determinar_ganador(jugador, computadora):
    """
    Determina el ganador de una ronda.

    Args:
        jugador (str): Opción elegida por el jugador.
        computadora (str): Opción elegida por la computadora.

    Returns:
        str: "jugador", "computadora" o "empate".
    """
    if jugador == computadora:
        return "empate"

    combinaciones_ganadoras = {
        ("1", "3"),  # Piedra gana a Tijera
        ("2", "1"),  # Papel gana a Piedra
        ("3", "2")   # Tijera gana a Papel
    }

    if (jugador, computadora) in combinaciones_ganadoras:
        return "jugador"

    return "computadora"


def mostrar_resultado_ronda(jugador, computadora, resultado):
    """
    Muestra el resultado de la ronda actual.

    Args:
        jugador (str): Elección del jugador.
        computadora (str): Elección de la computadora.
        resultado (str): Resultado de la ronda.
    """
    print("\n🎲 RESULTADO DE LA RONDA")
    print(f"\n👤 Tú elegiste: {OPCIONES[jugador][1]} {OPCIONES[jugador][0]}")
    print(f"💻 Computadora eligió: {OPCIONES[computadora][1]} {OPCIONES[computadora][0]}")

    if resultado == "jugador":
        print("\n🏆 ¡Ganaste la ronda!")
    elif resultado == "computadora":
        print("\n💻 La computadora ganó la ronda.")
    else:
        print("\n🤝 ¡Es un empate!")


def mostrar_resumen(victorias, derrotas, empates):
    """
    Muestra el resumen final de la partida.

    Args:
        victorias (int): Número de victorias del jugador.
        derrotas (int): Número de derrotas del jugador.
        empates (int): Número de empates.
    """
    total = victorias + derrotas + empates
    porcentaje = (victorias / total) * 100 if total > 0 else 0

    limpiar_pantalla()
    print("=" * 40)
    print("📊 RESUMEN FINAL DE LA PARTIDA")
    print("=" * 40)
    print(f"🏆 Victorias: {victorias}")
    print(f"💻 Derrotas: {derrotas}")
    print(f"🤝 Empates: {empates}")
    print(f"📈 Porcentaje de victorias: {porcentaje:.2f}%")
    print("=" * 40)

    if victorias > derrotas:
        print("🎉 ¡ERES EL GANADOR FINAL!")
    elif derrotas > victorias:
        print("💻 LA COMPUTADORA ES LA GANADORA FINAL.")
    else:
        print("🤝 LA PARTIDA TERMINÓ EN EMPATE GENERAL.")

    print("=" * 40)


def jugar():
    """
    Ejecuta una partida completa del juego hasta que el usuario decida salir.
    """
    victorias = 0
    derrotas = 0
    empates = 0

    while True:
        limpiar_pantalla()
        mostrar_menu()

        jugador = obtener_opcion_valida()

        if jugador == "0":
            break

        computadora = obtener_eleccion_computadora()
        resultado = determinar_ganador(jugador, computadora)

        if resultado == "jugador":
            victorias += 1
        elif resultado == "computadora":
            derrotas += 1
        else:
            empates += 1

        mostrar_resultado_ronda(jugador, computadora, resultado)
        input("\nPresiona ENTER para continuar...")

    mostrar_resumen(victorias, derrotas, empates)


def main():
    """
    Controla el flujo principal del programa y permite jugar múltiples partidas.
    """
    while True:
        mostrar_bienvenida()
        jugar()

        repetir = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()

        if repetir != "s":
            print("\n👋 ¡Gracias por jugar!")
            break


if __name__ == "__main__":
    main()


