import unittest
from unittest.mock import patch
import sys
import os

# Aseguramos que Python encuentre la carpeta 'src'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.utilidades import limpiar_pantalla

class TestUtilidades(unittest.TestCase):

    @patch('platform.system')
    @patch('os.system')
    def test_limpiar_pantalla_windows(self, mock_os_system, mock_platform):
        """Verifica que en Windows se ejecute el comando 'cls'"""
        # Simulamos que el sistema operativo es Windows
        mock_platform.return_value = "Windows"
        
        limpiar_pantalla()
        
        # Verificamos que os.system haya sido llamado con 'cls'
        mock_os_system.assert_called_once_with('cls')

    @patch('platform.system')
    @patch('os.system')
    def test_limpiar_pantalla_unix(self, mock_os_system, mock_platform):
        """Verifica que en Linux/macOS se ejecute el comando 'clear'"""
        # Simulamos que el sistema operativo es Linux
        mock_platform.return_value = "Linux"
        
        limpiar_pantalla()
        
        # Verificamos que os.system haya sido llamado con 'clear'
        mock_os_system.assert_called_once_with('clear')

if __name__ == '__main__':
    unittest.main()