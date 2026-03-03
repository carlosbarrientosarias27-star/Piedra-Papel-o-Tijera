import time
from core.logica import determinar_ganador, obtener_eleccion_computadora
from ui.menus import mostrar_menu, obtener_opcion_valida
from ui.pantalla import mostrar_resultado_ronda, mostrar_resumen
from utils.helpers import limpiar_pantalla

def jugar():
    victorias = 0
    derrotas = 0
    empates = 0

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

        if resultado == "jugador":
            victorias += 1
        elif resultado == "computadora":
            derrotas += 1
        else:
            empates += 1

        mostrar_resultado_ronda(jugador, computadora, resultado)
        input("\nPresiona ENTER para continuar...")

    mostrar_resumen(victorias, derrotas, empates)