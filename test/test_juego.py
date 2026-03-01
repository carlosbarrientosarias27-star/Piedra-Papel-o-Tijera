import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from src.juego import determinar_ganador, obtener_eleccion_computadora, OPCIONES


class TestJuego(unittest.TestCase):

    # ==============================
    # Tests para determinar_ganador
    # ==============================

    def test_empate(self):
        self.assertEqual(determinar_ganador("1", "1"), "empate")
        self.assertEqual(determinar_ganador("2", "2"), "empate")
        self.assertEqual(determinar_ganador("3", "3"), "empate")

    def test_gana_jugador(self):
        self.assertEqual(determinar_ganador("1", "3"), "jugador")  # Piedra vs Tijera
        self.assertEqual(determinar_ganador("2", "1"), "jugador")  # Papel vs Piedra
        self.assertEqual(determinar_ganador("3", "2"), "jugador")  # Tijera vs Papel

    def test_gana_computadora(self):
        self.assertEqual(determinar_ganador("3", "1"), "computadora")
        self.assertEqual(determinar_ganador("1", "2"), "computadora")
        self.assertEqual(determinar_ganador("2", "3"), "computadora")

    # ==================================
    # Tests para obtener_eleccion_computadora
    # ==================================

    def test_eleccion_computadora_valida(self):
        for _ in range(100):  # Lo probamos varias veces
            eleccion = obtener_eleccion_computadora()
            self.assertIn(eleccion, OPCIONES.keys())


if __name__ == "__main__":
    unittest.main()