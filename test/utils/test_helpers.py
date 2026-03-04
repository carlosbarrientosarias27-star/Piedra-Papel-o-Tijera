import unittest
from unittest.mock import patch
import sys
import os

# Agregamos la raíz del proyecto al sistema de rutas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from utils.helpers import limpiar_pantalla
# ... resto de tus imports

class TestHelpers(unittest.TestCase):

    @patch('subprocess.call')
    def test_limpiar_pantalla_windows(self, mock_subproc):
        """Prueba que en Windows se llame a 'cls'"""
        with patch('os.name', 'nt'):
            limpiar_pantalla()
            # Verifica que se llamó a subprocess con 'cls'
            mock_subproc.assert_called_once_with('cls', shell=True)

    @patch('subprocess.call')
    def test_limpiar_pantalla_linux_mac(self, mock_subproc):
        """Prueba que en Linux/Mac se llame a 'clear'"""
        with patch('os.name', 'posix'):
            limpiar_pantalla()
            # Verifica que se llamó a subprocess con 'clear'
            mock_subproc.assert_called_once_with('clear', shell=True)

    @patch('subprocess.call')
    @patch('builtins.print')
    def test_limpiar_pantalla_exception(self, mock_print, mock_subproc):
        """Prueba que si subprocess falla, se impriman saltos de línea"""
        # Simulamos que subprocess lanza una excepción
        mock_subproc.side_effect = Exception("Error de sistema")
        
        limpiar_pantalla()
        
        # Verifica que se usó el fallback de imprimir 100 líneas
        mock_print.assert_called_once_with("\n" * 100)

if __name__ == '__main__':
    unittest.main()