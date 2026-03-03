import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__))) 

from core.juego import jugar
from ui.pantalla import mostrar_bienvenida

def main():
   
    while True: 
        mostrar_bienvenida 
        jugar()

        repetir = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()

        if repetir != "s":
            print("\n👋 ¡Gracias por jugar!")
            break


if __name__ == "__main__":
    main()
