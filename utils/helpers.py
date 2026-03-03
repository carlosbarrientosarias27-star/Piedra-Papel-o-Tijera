import os
import subprocess

def limpiar_pantalla():
    """
    Limpia la pantalla de la consola según el sistema operativo.
    Utiliza subprocess para mayor control.
    """
    comando = 'cls' if os.name == 'nt' else 'clear'
    try:
        subprocess.call(comando, shell=True)
    except Exception:
        print("\n" * 100)