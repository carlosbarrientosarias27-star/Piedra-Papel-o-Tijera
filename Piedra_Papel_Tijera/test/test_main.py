import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Ajuste robusto de rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from main import jugar

class TestMain(unittest.TestCase):

    # Es CRUCIAL que el path del patch coincida exactamente con cómo se importa en main.py
    # En tu main.py usas: from src.utilidades import limpiar_pantalla
    @patch('main.limpiar_pantalla') 
    @patch('main.obtener_eleccion_usuario')
    @patch('main.obtener_eleccion_computadora')
    @patch('main.determinar_ganador')
    @patch('main.mostrar_estadisticas')
    @patch('builtins.input')
    def test_flujo_jugar_una_ronda_victoria(self, mock_input, mock_stats, mock_ganador, mock_pc, mock_usuario, mock_limpiar):
        """Simula una partida de 1 ronda donde el usuario gana."""
        # Configuramos los retornos
        mock_input.return_value = "1" 
        mock_usuario.return_value = "Piedra"
        mock_pc.return_value = "Tijera"
        mock_ganador.return_value = "Victoria"

        jugar()

        # Verificaciones
        mock_limpiar.assert_called()
        mock_ganador.assert_called_with("Piedra", "Tijera")
        mock_stats.assert_called_once_with(1, 0, 0)

    @patch('main.mostrar_estadisticas')
    @patch('main.obtener_eleccion_usuario')
    @patch('main.obtener_eleccion_computadora')
    @patch('main.determinar_ganador')
    @patch('main.limpiar_pantalla')
    @patch('builtins.input')
    def test_rondas_invalidas_luego_valida(self, mock_input, mock_limpiar, mock_ganador, mock_pc, mock_usuario, mock_stats):
        """Verifica el bucle de validación de rondas inicial."""
        
        # Proporcionamos suficientes valores para que el Mock no lance StopIteration
        # 1. "abc" (invalido), 2. "15" (invalido), 3. "1" (valido para rondas)
        mock_input.side_effect = ["abc", "15", "1"]
        
        # Mocks para el resto de la ejecución
        mock_usuario.return_value = "Papel"
        mock_pc.return_value = "Papel"
        mock_ganador.return_value = "Empate"
            
        jugar()
            
        # Verificamos que al final se procesó 1 ronda con empate
        mock_stats.assert_called_once_with(0, 0, 1)

if __name__ == '__main__':
    unittest.main()