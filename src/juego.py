def mostrar_opciones():
    print("Elige una opción:")
    print("1 = Piedra")
    print("2 = Papel")
    print("3 = Tijera")


def obtener_eleccion_jugador():
    while True:
        try:
            opcion = int(input("Introduce el número de tu elección: "))
            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("Opción no válida. Debe ser 1, 2 o 3.")
        except ValueError:
            print("Entrada inválida. Introduce un número.")


def convertir_eleccion(numero):
    opciones = {
        1: "Piedra",
        2: "Papel",
        3: "Tijera"
    }
    return opciones[numero]


# Programa principal
mostrar_opciones()
eleccion_numero = obtener_eleccion_jugador()
eleccion_nombre = convertir_eleccion(eleccion_numero)

print(f"Has elegido: {eleccion_nombre}") 


import random

def eleccion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

# Generar elección
computadora = eleccion_computadora()

# Mostrar elección por pantalla
print("La computadora eligió:", computadora) 


def determinar_ganador(jugador, computadora):
    """
    Compara la elección del jugador con la de la computadora
    y devuelve el resultado: 'Victoria', 'Derrota' o 'Empate'
    """

    # Normalizamos texto
    jugador = jugador.lower()
    computadora = computadora.lower()

    if jugador == computadora:
        return "Empate"

    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "tijera" and computadora == "papel") or
        (jugador == "papel" and computadora == "piedra")
    ):
        return "Victoria"

    else:
        return "Derrota"


# Ejemplo de uso
if __name__ == "__main__":
    jugador = input("Elige piedra, papel o tijera: ")
    
    import random
    opciones = ["piedra", "papel", "tijera"]
    computadora = random.choice(opciones)

    resultado = determinar_ganador(jugador, computadora)

    print(f"\nJugador eligió: {jugador}")
    print(f"Computadora eligió: {computadora}")
    print(f"Resultado: {resultado}")


    def obtener_jugada():
     while True:
        try:
            print("Elige una opción:")
            print("1 - Piedra")
            print("2 - Papel")
            print("3 - Tijera")
            
            opcion = int(input("Introduce 1, 2 o 3: "))

            if opcion in [1, 2, 3]:
                return opcion
            else:
                print("❌ Error: Debes introducir solo 1, 2 o 3.\n")

        except ValueError:
            print("❌ Error: Debes introducir un número válido.\n")


# Uso de la función
jugada_jugador = obtener_jugada()
print(f"Has elegido: {jugada_jugador}") 


import random

opciones = ["piedra", "papel", "tijera"]

victorias = 0
derrotas = 0
empates = 0

while True:
    usuario = input("Elige piedra, papel o tijera (o salir): ").lower()
    
    if usuario == "salir":
        print("Juego terminado 👋")
        break
    
    if usuario not in opciones:
        print("Opción inválida.")
        continue

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if usuario == computadora:
        print("¡Es un empate!")
        empates += 1

    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "papel" and computadora == "piedra") or \
         (usuario == "tijera" and computadora == "papel"):
        print("¡Ganaste!")
        victorias += 1

    else:
        print("Perdiste...")
        derrotas += 1

    print("\n📊 Marcador actual:")
    print(f"Victorias: {victorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")
    print("-" * 20)


    import random

def obtener_rondas():
    while True:
        try:
            rondas = int(input("¿Cuántas rondas quieres jugar? "))
            if rondas > 0:
                return rondas
            else:
                print("⚠️ Debes ingresar un número entero positivo.")
        except ValueError:
            print("⚠️ Entrada inválida. Debes ingresar un número entero.")

def obtener_jugada_jugador():
    opciones = ["piedra", "papel", "tijera"]
    while True:
        jugada = input("Elige piedra, papel o tijera: ").lower()
        if jugada in opciones:
            return jugada
        else:
            print("⚠️ Opción inválida. Intenta nuevamente.")

def obtener_jugada_maquina():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_ganador(jugador, maquina):
    if jugador == maquina:
        return "empate"
    elif (
        (jugador == "piedra" and maquina == "tijera") or
        (jugador == "papel" and maquina == "piedra") or
        (jugador == "tijera" and maquina == "papel")
    ):
        return "jugador"
    else:
        return "maquina"

def jugar():
    rondas_totales = obtener_rondas()
    victorias_jugador = 0
    victorias_maquina = 0

    for ronda in range(1, rondas_totales + 1):
        print(f"\n--- Ronda {ronda} de {rondas_totales} ---")

        jugador = obtener_jugada_jugador()
        maquina = obtener_jugada_maquina()

        print(f"La máquina eligió: {maquina}")

        resultado = determinar_ganador(jugador, maquina)

        if resultado == "jugador":
            print("🎉 ¡Ganaste esta ronda!")
            victorias_jugador += 1
        elif resultado == "maquina":
            print("💻 La máquina ganó esta ronda.")
            victorias_maquina += 1
        else:
            print("🤝 ¡Es un empate!")

    # Resultado final
    print("\n=== RESULTADO FINAL ===")
    print(f"Jugador: {victorias_jugador} victorias")
    print(f"Máquina: {victorias_maquina} victorias")

    if victorias_jugador > victorias_maquina:
        print("🏆 ¡Ganaste la partida!")
    elif victorias_maquina > victorias_jugador:
        print("💻 La máquina ganó la partida.")
    else:
        print("🤝 La partida terminó en empate.")

if __name__ == "__main__":
    jugar()


import os
import random
import time

# Diccionario con opciones y emojis
opciones = {
    "1": ("Piedra", "🪨"),
    "2": ("Papel", "📄"),
    "3": ("Tijera", "✂️")
}

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"
    
    if (
        (jugador == "1" and computadora == "3") or
        (jugador == "2" and computadora == "1") or
        (jugador == "3" and computadora == "2")
    ):
        return "jugador"
    else:
        return "computadora"

def jugar():
    victorias = 0
    derrotas = 0
    empates = 0

    while True:
        limpiar_pantalla()
        print("=" * 40)
        print("🎮  PIEDRA - PAPEL - TIJERA  🎮")
        print("=" * 40)
        print("1 - 🪨 Piedra")
        print("2 - 📄 Papel")
        print("3 - ✂️ Tijera")
        print("0 - Salir")
        print("=" * 40)

        jugador = input("👉 Elige una opción: ")

        if jugador == "0":
            break

        if jugador not in opciones:
            print("\n⚠️ Opción inválida")
            time.sleep(1.5)
            continue

        computadora = random.choice(list(opciones.keys()))

        print("\n🎲 RESULTADO DE LA RONDA")
        print(f"\n👤 Tú elegiste: {opciones[jugador][1]} {opciones[jugador][0]}")
        print(f"💻 Computadora eligió: {opciones[computadora][1]} {opciones[computadora][0]}")

        resultado = determinar_ganador(jugador, computadora)

        if resultado == "jugador":
            print("\n🏆 ¡Ganaste la ronda!")
            victorias += 1
        elif resultado == "computadora":
            print("\n💻 La computadora ganó la ronda.")
            derrotas += 1
        else:
            print("\n🤝 ¡Es un empate!")
            empates += 1

        input("\nPresiona ENTER para continuar...")

    # === RESUMEN FINAL ===
    total_partidas = victorias + derrotas + empates

    if total_partidas > 0:
        porcentaje_victorias = (victorias / total_partidas) * 100
    else:
        porcentaje_victorias = 0

    limpiar_pantalla()
    print("=" * 40)
    print("📊 RESUMEN FINAL DE LA PARTIDA")
    print("=" * 40)
    print(f"🏆 Victorias: {victorias}")
    print(f"💻 Derrotas: {derrotas}")
    print(f"🤝 Empates: {empates}")
    print(f"📈 Porcentaje de victorias: {porcentaje_victorias:.2f}%")
    print("=" * 40)

    # Determinar ganador final
    if victorias > derrotas:
        print("🎉 ¡ERES EL GANADOR FINAL!")
    elif derrotas > victorias:
        print("💻 LA COMPUTADORA ES LA GANADORA FINAL.")
    else:
        print("🤝 LA PARTIDA TERMINÓ EN EMPATE GENERAL.")

    print("=" * 40)

# Ejecutar juego
mostrar_bienvenida()
jugar()


