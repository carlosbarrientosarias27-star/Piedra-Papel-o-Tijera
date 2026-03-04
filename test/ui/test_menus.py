import unittest
from unittest.mock import patch, io
import sys
import os

# Ajuste de path para reconocer la raíz del proyecto
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from ui.menus import mostrar_menu, obtener_opcion_valida
from config.opciones import OPCIONES

class TestUIMenus(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mostrar_menu_contenido(self, mock_stdout):
        """Verifica que el menú imprima el título y todas las opciones del config."""
        mostrar_menu()
        output = mock_stdout.getvalue()
        
        self.assertIn("PIEDRA - PAPEL - TIJERA", output)
        self.assertIn("0 - Salir", output)
        # Verifica que cada opción de OPCIONES esté en el print
        for nombre, emoji in OPCIONES.values():
            self.assertIn(nombre, output)
            self.assertIn(emoji, output)

    @patch('builtins.input', side_effect=['1'])
    def test_obtener_opcion_valida_directa(self, mock_input):
        """Verifica que retorna la opción si es válida a la primera."""
        resultado = obtener_opcion_valida()
        self.assertEqual(resultado, '1')

    @patch('builtins.input', side_effect=['', '9', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_obtener_opcion_reintento(self, mock_stdout, mock_input):
        """Verifica que reintenta tras entradas vacías o inválidas hasta dar una correcta."""
        resultado = obtener_opcion_valida()
        output = mock_stdout.getvalue()
        
        self.assertEqual(resultado, '2')
        self.assertIn("No puedes dejar el campo vacío", output)
        self.assertIn("Opción inválida", output)

    @patch('builtins.input', side_effect=KeyboardInterrupt)
    def test_obtener_opcion_keyboard_interrupt(self, mock_input):
        """Verifica que Ctrl+C devuelve '0' para salir limpiamente."""
        resultado = obtener_opcion_valida()
        self.assertEqual(resultado, '0')

if __name__ == "__main__":
    unittest.main()