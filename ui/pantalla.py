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