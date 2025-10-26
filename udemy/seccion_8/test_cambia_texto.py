import cambia_texto
import unittest

"""
This file contains unit tests for the 'todo_mayusculas'
function from the 'cambia_texto' module.
It uses the 'unittest' library to verify that the function correctly
converts a string to uppercase.
"""
""" Es integrada solo se necesita importar. """


class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        # Ejemplo de una palabra para ver como funciona
        palabra = 'buen dia'
        resultado = cambia_texto.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'Buen Dia')


if __name__ == '__main__':
    unittest.main()
