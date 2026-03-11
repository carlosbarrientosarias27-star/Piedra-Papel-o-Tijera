import random 

def obtener_eleccion_computadora():
    """Genera una elección aleatoria para la computadora."""
    opciones = ["Piedra", "Papel", "Tijera"]
    return random.choice(opciones)

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