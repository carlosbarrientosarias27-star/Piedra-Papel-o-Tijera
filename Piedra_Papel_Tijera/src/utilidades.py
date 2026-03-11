import os 
import platform 

def limpiar_pantalla():
    """Limpia la terminal de comandos.

    Detecta el sistema operativo del usuario para ejecutar el comando 
    apropiado ('cls' para Windows o 'clear' para sistemas Unix/Linux/macOS).
    """
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')