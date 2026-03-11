import random 

def obtener_eleccion_computadora():
    """Genera una elección aleatoria para la computadora.

    Returns:
        str: Una de las tres opciones posibles: "Piedra", "Papel" o "Tijera".
    """
    opciones = ["Piedra", "Papel", "Tijera"]
    return random.choice(opciones)

def determinar_ganador(usuario, pc):
    """Compara las elecciones y determina el resultado de la ronda.

    Utiliza un diccionario de reglas donde cada clave vence a su valor asociado.

    Args:
        usuario (str): La elección del jugador.
        pc (str): La elección generada por la computadora.

    Returns:
        str: El resultado de la ronda ("Victoria", "Derrota" o "Empate").
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