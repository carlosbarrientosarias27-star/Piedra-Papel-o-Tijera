import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import time
from core.logica import determinar_ganador, obtener_eleccion_computadora
from ui.menus import mostrar_menu, obtener_opcion_valida
from ui.pantalla import mostrar_resultado_ronda, mostrar_resumen
from utils.helpers import limpiar_pantalla

def jugar():
    victorias = 0
    derrotas = 0
    empates = 0

    try:
        while True:
            limpiar_pantalla()
            mostrar_menu()

            jugador = obtener_opcion_valida()

            if jugador == "0":
                break

            print("\n💻 La computadora está eligiendo...")
            time.sleep(2)

            computadora = obtener_eleccion_computadora()
            resultado = determinar_ganador(jugador, computadora)

            if resultado not in ("jugador", "computadora", "empate"):
                print("⚠ Error inesperado en el resultado.")
                input("Presiona ENTER para continuar...")
                continue

            if resultado == "jugador":
                victorias += 1
            elif resultado == "computadora":
                derrotas += 1
            else:
                empates += 1

            mostrar_resultado_ronda(jugador, computadora, resultado)
            input("\nPresiona ENTER para continuar...")

    except KeyboardInterrupt:
        print("\n\nJuego interrumpido por el usuario.")

    limpiar_pantalla()

    total = victorias + derrotas + empates
    porcentaje = (victorias / total) * 100 if total > 0 else 0

    mostrar_resumen(victorias, derrotas, empates, porcentaje)