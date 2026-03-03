import random
from config.opciones import OPCIONES

def obtener_eleccion_computadora():
    return random.choice(list(OPCIONES.keys()))

def determinar_ganador(jugador, computadora):
    if jugador == computadora:
        return "empate"

    combinaciones_ganadoras = {
        ("1", "3"),
        ("2", "1"),
        ("3", "2")
    }

    if (jugador, computadora) in combinaciones_ganadoras:
        return "jugador"

    return "computadora"