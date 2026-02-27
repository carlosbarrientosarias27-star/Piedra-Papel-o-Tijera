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
