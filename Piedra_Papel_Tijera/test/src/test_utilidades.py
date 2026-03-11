import sys
import os

# Añade la carpeta raíz al path de búsqueda de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import unittest
from config.opciones import OPCIONES

class TestConfigOpciones(unittest.TestCase):

    def test_estructura_diccionario(self):
        """Verifica que OPCIONES sea un diccionario y tenga 3 elementos."""
        self.assertIsInstance(OPCIONES, dict)
        self.assertEqual(len(OPCIONES), 3)

    def test_claves_validas(self):
        """Verifica que las claves sean las esperadas ('1', '2', '3')."""
        claves_esperadas = ["1", "2", "3"]
        self.assertListEqual(list(OPCIONES.keys()), claves_esperadas)

    def test_contenido_valores(self):
        """Verifica que cada valor sea una tupla con (Nombre, Emoji)."""
        for clave, valor in OPCIONES.items():
            self.assertIsInstance(valor, tuple)
            self.assertEqual(len(valor), 2)
            # Verifica que el primer elemento sea un string (Piedra, Papel o Tijera)
            self.assertIsInstance(valor[0], str)

    def test_valores_especificos(self):
        """Prueba un valor específico para asegurar la integridad de los datos."""
        self.assertEqual(OPCIONES["1"], ("Piedra", "🪨"))
        self.assertEqual(OPCIONES["2"], ("Papel", "📄"))
        self.assertEqual(OPCIONES["3"], ("Tijera", "✂️"))

if __name__ == "__main__":
    unittest.main()