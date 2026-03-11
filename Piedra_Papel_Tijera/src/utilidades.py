import os 
import platform 

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')