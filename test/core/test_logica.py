import unittest
import sys
import os

# Aseguramos que el path incluya la raíz del proyecto para evitar ModuleNotFoundError
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from core.logica import determinar_ganador, obtener_eleccion_computadora
from config.opciones import OPCIONES

class TestLogicaJuego(unittest.TestCase):

    def test_empate(self):
        """Verifica que las mismas elecciones resulten en empate."""
        self.assertEqual(determinar_ganador("1", "1"), "empate")
        self.assertEqual(determinar_ganador("2", "2"), "empate")
        self.assertEqual(determinar_ganador("3", "3"), "empate")

    def test_jugador_gana(self):
        """Verifica todas las combinaciones donde el jugador gana."""
        self.assertEqual(determinar_ganador("1", "3"), "jugador") # Piedra vence a Tijera
        self.assertEqual(determinar_ganador("2", "1"), "jugador") # Papel vence a Piedra
        self.assertEqual(determinar_ganador("3", "2"), "jugador") # Tijera vence a Papel

    def test_computadora_gana(self):
        """Verifica todas las combinaciones donde la computadora gana."""
        self.assertEqual(determinar_ganador("3", "1"), "computadora") # Tijera pierde contra Piedra
        self.assertEqual(determinar_ganador("1", "2"), "computadora") # Piedra pierde contra Papel
        self.assertEqual(determinar_ganador("2", "3"), "computadora") # Papel pierde contra Tijera

    def test_eleccion_invalida(self):
        """Verifica que se lance una excepción si las opciones no existen."""
        with self.assertRaises(ValueError):
            determinar_ganador("9", "1")
        with self.assertRaises(ValueError):
            determinar_ganador("1", "X")

    def test_obtener_eleccion_computadora(self):
        """Verifica que la computadora siempre elija una opción válida del config."""
        opciones_validas = list(OPCIONES.keys())
        for _ in range(100): # Probamos 100 veces por aleatoriedad
            eleccion = obtener_eleccion_computadora()
            self.assertIn(eleccion, opciones_validas)

if __name__ == "__main__":
    unittest.main()