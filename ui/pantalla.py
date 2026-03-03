from config.opciones import OPCIONES
from utils.helpers import limpiar_pantalla


def mostrar_bienvenida():
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


def mostrar_resultado_ronda(jugador, computadora, resultado):
    # 🔹 (5) Limpiar antes de mostrar resultado
    limpiar_pantalla()

    print("\n🎲 RESULTADO DE LA RONDA")

    # 🔹 (1) Validación defensiva
    nombre_jugador, emoji_jugador = OPCIONES.get(jugador, ("Desconocido", "❓"))
    nombre_cpu, emoji_cpu = OPCIONES.get(computadora, ("Desconocido", "❓"))

    print(f"\n👤 Tú elegiste: {emoji_jugador} {nombre_jugador}")
    print(f"💻 Computadora eligió: {emoji_cpu} {nombre_cpu}")

    if resultado == "jugador":
        print("\n🏆 ¡Ganaste la ronda!")
    elif resultado == "computadora":
        print("\n💻 La computadora ganó la ronda.")
    else:
        print("\n🤝 ¡Es un empate!")


# 🔹 (2) Ahora recibe el porcentaje desde juego.py
def mostrar_resumen(victorias, derrotas, empates, porcentaje):

    limpiar_pantalla()

    print("=" * 40)
    print("📊 RESUMEN FINAL DE LA PARTIDA")
    print("=" * 40)
    print(f"🏆 Victorias: {victorias}")
    print(f"💻 Derrotas: {derrotas}")
    print(f"🤝 Empates: {empates}")
    print(f"📈 Porcentaje de victorias: {porcentaje:.2f}%")

    # 🔹 (3) Mensaje dinámico según rendimiento
    if porcentaje >= 70:
        print("\n🔥 ¡Eres un maestro del juego!")
    elif porcentaje >= 40:
        print("\n👍 Buen desempeño.")
    else:
        print("\n😅 Puedes mejorar. ¡Sigue practicando!")

    print("=" * 40)

    # 🔹 (4) Pausa final
    input("\nPresiona ENTER para salir...")