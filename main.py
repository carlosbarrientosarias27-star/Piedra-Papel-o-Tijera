from core.juego import jugar
from ui.pantalla import mostrar_bienvenida


def main():
    try:
        while True:
            mostrar_bienvenida()
            jugar()

            while True:
                repetir = input("\n¿Quieres jugar otra partida? (s/n): ").strip().lower()
                if repetir in ("s", "n"):
                    break
                print("⚠️ Debes escribir 's' o 'n'.")

            if repetir == "n":
                print("\n👋 ¡Gracias por jugar!")
                break

    except KeyboardInterrupt:
        print("\n\n👋 Juego cerrado por el usuario.")


if __name__ == "__main__":
    main()