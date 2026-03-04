import unittest
from unittest.mock import patch, io
import sys
import os

# Ajuste de path para reconocer la raíz del proyecto
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from ui.pantalla import mostrar_bienvenida, mostrar_resultado_ronda, mostrar_resumen

class TestUIPantalla(unittest.TestCase):

    @patch('ui.pantalla.limpiar_pantalla')
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostrar_bienvenida(self, mock_stdout, mock_input, mock_limpiar):
        """Verifica que se impriman las reglas y el título de bienvenida."""
        mostrar_bienvenida()
        output = mock_stdout.getvalue()
        
        self.assertIn("BIENVENIDO A PIEDRA, PAPEL O TIJERA", output)
        self.assertIn("Reglas del juego", output)
        mock_limpiar.assert_called_once()

    @patch('ui.pantalla.limpiar_pantalla')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostrar_resultado_ronda_victoria(self, mock_stdout, mock_limpiar):
        """Verifica la visualización cuando el jugador gana."""
        # "1" es Piedra, "3" es Tijera según tu config.opciones
        mostrar_resultado_ronda("1", "3", "jugador")
        output = mock_stdout.getvalue()
        
        self.assertIn("Tú elegiste: 🪨 Piedra", output)
        self.assertIn("Computadora eligió: ✂️ Tijera", output)
        self.assertIn("¡Ganaste la ronda!", output)

    @patch('ui.pantalla.limpiar_pantalla')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostrar_resultado_ronda_desconocido(self, mock_stdout, mock_limpiar):
        """Verifica la validación defensiva ante opciones inexistentes."""
        mostrar_resultado_ronda("99", "X", "empate")
        output = mock_stdout.getvalue()
        
        self.assertIn("Desconocido", output)
        self.assertIn("❓", output)

    @patch('ui.pantalla.limpiar_pantalla')
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostrar_resumen_maestro(self, mock_stdout, mock_input, mock_limpiar):
        """Verifica el mensaje dinámico para un porcentaje alto (>= 70%)."""
        mostrar_resumen(7, 2, 1, 70.00)
        output = mock_stdout.getvalue()
        
        self.assertIn("Victorias: 7", output)
        self.assertIn("Porcentaje de victorias: 70.00%", output)
        self.assertIn("¡Eres un maestro del juego!", output)

    @patch('ui.pantalla.limpiar_pantalla')
    @patch('builtins.input', return_value='')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostrar_resumen_mejora(self, mock_stdout, mock_input, mock_limpiar):
        """Verifica el mensaje dinámico para un porcentaje bajo (< 40%)."""
        mostrar_resumen(1, 8, 1, 10.00)
        output = mock_stdout.getvalue()
        
        self.assertIn("Puedes mejorar. ¡Sigue practicando!", output)

if __name__ == "__main__":
    unittest.main()