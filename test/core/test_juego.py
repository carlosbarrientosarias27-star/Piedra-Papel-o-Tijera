import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Esto busca la ruta de la carpeta raíz (GitHub/Piedra-Papel-o-Tijera) 
# subiendo dos niveles desde test/core/
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

# Ahora sí puedes importar
from core.juego import jugar

class TestJuegoPrincipal(unittest.TestCase):

    @patch('core.juego.limpiar_pantalla')
    @patch('core.juego.mostrar_menu')
    @patch('core.juego.obtener_opcion_valida')
    @patch('core.juego.obtener_eleccion_computadora')
    @patch('core.juego.determinar_ganador')
    @patch('core.juego.mostrar_resultado_ronda')
    @patch('core.juego.mostrar_resumen')
    @patch('builtins.input', return_value='') # Simula presionar ENTER
    def test_flujo_victoria_jugador(self, mock_input, mock_resumen, mock_ronda, 
                                    mock_ganador, mock_pc, mock_opcion, 
                                    mock_menu, mock_limpiar):
        """
        Prueba que si el jugador gana una ronda y sale, 
        el resumen final muestra 1 victoria y 100% de éxito.
        """
        # Configuramos el comportamiento de los mocks
        # Simula: Jugador elige "1" (Piedra) la primera vez, y "0" (Salir) la segunda.
        mock_opcion.side_effect = ["1", "0"]
        mock_pc.return_value = "3" # Computadora elige Tijera
        mock_ganador.return_value = "jugador"

        # Ejecutamos la función
        jugar()

        # Verificaciones (Assertions)
        # 1. Comprobar que determinar_ganador se llamó con los datos correctos
        mock_ganador.assert_called_with("1", "3")
        
        # 2. Comprobar que mostrar_resumen recibió (victorias=1, derrotas=0, empates=0, porcentaje=100.0)
        mock_resumen.assert_called_once_with(1, 0, 0, 100.0)

    @patch('core.juego.obtener_opcion_valida', side_effect=["0"])
    @patch('core.juego.mostrar_resumen')
    @patch('core.juego.limpiar_pantalla')
    def test_salir_inmediatamente(self, mock_limpiar, mock_resumen, mock_opcion):
        """Verifica que el juego termine limpiamente si se pulsa '0' al inicio."""
        jugar()
        # El resumen debe ser 0 en todo
        mock_resumen.assert_called_once_with(0, 0, 0, 0)

if __name__ == "__main__":
    unittest.main()