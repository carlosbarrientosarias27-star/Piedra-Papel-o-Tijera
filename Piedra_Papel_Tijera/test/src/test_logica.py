import unittest
from unittest.mock import patch
import sys
import os

# Aseguramos que Python encuentre la carpeta 'src' subiendo dos niveles
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.logica import obtener_eleccion_computadora, determinar_ganador

class TestLogica(unittest.TestCase):

    # --- Pruebas para obtener_eleccion_computadora ---

    def test_obtener_eleccion_computadora_valida(self):
        """Verifica que la PC siempre elija una opción válida"""
        opciones_validas = ["Piedra", "Papel", "Tijera"]
        for _ in range(100):  # Probamos 100 veces por aleatoriedad
            eleccion = obtener_eleccion_computadora()
            self.assertIn(eleccion, opciones_validas)

    # --- Pruebas para determinar_ganador ---

    def test_determinar_ganador_empate(self):
        """Verifica que elecciones iguales resulten en Empate"""
        self.assertEqual(determinar_ganador("Piedra", "Piedra"), "Empate")
        self.assertEqual(determinar_ganador("Papel", "Papel"), "Empate")
        self.assertEqual(determinar_ganador("Tijera", "Tijera"), "Empate")

    def test_determinar_ganador_victoria_usuario(self):
        """Verifica los casos donde el usuario debería ganar"""
        self.assertEqual(determinar_ganador("Piedra", "Tijera"), "Victoria")
        self.assertEqual(determinar_ganador("Tijera", "Papel"), "Victoria")
        self.assertEqual(determinar_ganador("Papel", "Piedra"), "Victoria")

    def test_determinar_ganador_derrota_usuario(self):
        """Verifica los casos donde el usuario debería perder"""
        self.assertEqual(determinar_ganador("Piedra", "Papel"), "Derrota")
        self.assertEqual(determinar_ganador("Tijera", "Piedra"), "Derrota")
        self.assertEqual(determinar_ganador("Papel", "Tijera"), "Derrota")

    # --- Prueba avanzada con Mock (Opcional) ---

    @patch('random.choice')
    def test_obtener_eleccion_computadora_mock(self, mock_random):
        """Forzamos a la PC a elegir algo específico para probar la consistencia"""
        mock_random.return_value = "Papel"
        self.assertEqual(obtener_eleccion_computadora(), "Papel")

if __name__ == '__main__':
    unittest.main()