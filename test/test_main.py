import sys
import os

# Agregamos la carpeta raíz al PYTHONPATH
# Esto sube un nivel desde 'test/' para llegar a la raíz del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from unittest.mock import patch
from main import main  # Ahora sí lo encontrará

# ... resto de tu código de test ...

class TestMain(unittest.TestCase):

    @patch('main.mostrar_bienvenida')
    @patch('main.jugar')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main_sale_correctamente(self, mock_print, mock_input, mock_jugar, mock_bienvenida):
        """
        Simula una partida donde el usuario elige 'n' para no volver a jugar.
        """
        # Configuramos el input para que devuelva 'n' en la primera pregunta de repetir
        mock_input.return_value = 'n'
        
        # Ejecutamos main (se detendrá tras la primera iteración por el 'n')
        main()

        # Verificaciones
        mock_bienvenida.assert_called_once()
        mock_jugar.assert_called_once()
        mock_print.assert_any_call("\n👋 ¡Gracias por jugar!")

    @patch('main.mostrar_bienvenida')
    @patch('main.jugar')
    @patch('builtins.input')
    def test_main_repite_una_vez_y_sale(self, mock_input, mock_jugar, mock_bienvenida):
        """
        Simula que el usuario juega una vez, dice que 's' (sí), 
        juega otra vez y luego dice 'n' (no).
        """
        # Definimos una secuencia de entradas
        mock_input.side_effect = ['s', 'n']
        
        main()

        # Se debió llamar a jugar 2 veces y a bienvenida 2 veces
        self.assertEqual(mock_jugar.call_count, 2)
        self.assertEqual(mock_bienvenida.call_count, 2)

    @patch('main.mostrar_bienvenida')
    def test_main_keyboard_interrupt(self, mock_bienvenida):
        """
        Simula que el usuario presiona Ctrl+C (KeyboardInterrupt).
        """
        # Forzamos a que la primera función lanzada en el try lance la excepción
        mock_bienvenida.side_effect = KeyboardInterrupt
        
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_any_call("\n\n👋 Juego cerrado por el usuario.")

if __name__ == '__main__':
    unittest.main()