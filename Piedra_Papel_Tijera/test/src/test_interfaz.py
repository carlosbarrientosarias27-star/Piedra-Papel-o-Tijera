import unittest
from unittest.mock import patch
import io
import sys
import os

# --- ESTO SOLUCIONA EL ERROR DE IMPORTACIÓN ---
# Agregamos la raíz del proyecto al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Ahora ya puedes importar desde src
from src.interfaz import obtener_eleccion_usuario, mostrar_estadisticas
# ----------------------------------------------

class TestInterfaz(unittest.TestCase):

    # --- Pruebas para obtener_eleccion_usuario ---

    @patch('builtins.input', side_effect=['1'])
    def test_obtener_eleccion_piedra(self, mock_input):
        """Verifica que la opción 1 retorne 'Piedra'"""
        resultado = obtener_eleccion_usuario()
        self.assertEqual(resultado, "Piedra")

    @patch('builtins.input', side_effect=['2'])
    def test_obtener_eleccion_papel(self, mock_input):
        """Verifica que la opción 2 retorne 'Papel'"""
        resultado = obtener_eleccion_usuario()
        self.assertEqual(resultado, "Papel")

    @patch('builtins.input', side_effect=['5', '3'])
    def test_obtener_eleccion_invalida_luego_valida(self, mock_input):
        """Verifica que si se mete un número fuera de rango, vuelva a pedirlo hasta ser válido"""
        resultado = obtener_eleccion_usuario()
        self.assertEqual(resultado, "Tijera")

    # --- Pruebas para mostrar_estadisticas ---

    def test_mostrar_estadisticas_victoria(self):
        """Verifica que el resumen indique victoria si v > d"""
        # Capturamos la salida de la consola (stdout)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        mostrar_estadisticas(3, 1, 1) # 3 Victorias, 1 Derrota
        
        sys.stdout = sys.__stdout__ # Resetear la salida
        
        self.assertIn("¡Ganaste la partida!", captured_output.getvalue())
        self.assertIn("60.0%", captured_output.getvalue()) # 3/5 = 60%

    def test_mostrar_estadisticas_empate(self):
        """Verifica el caso de empate global"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        mostrar_estadisticas(1, 1, 1)
        
        sys.stdout = sys.__stdout__
        
        self.assertIn("Ha sido un empate global.", captured_output.getvalue())

if __name__ == '__main__':
    unittest.main()