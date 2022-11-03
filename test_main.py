from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

class Test(TestCase):
    def test_output(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            try:
                lines = mock_stdout.getvalue().split("\n")
                self.assertEqual(lines[1], "The current Real Madrid roster:") 
                self.assertEqual(lines[3], "Thibaut Courtois") 
                self.assertEqual(lines[35], "The new Real Madrid roster:") 
                self.assertEqual(lines[37], "Thibaut Courtois") 
                correct_output = """Thibaut Courtois
Dani Carvajal
Éder Militão
Jesús Vallejo
Nacho
Eden Hazard
Toni Kroos
Karim Benzema
Luka Modrić
Marco Asensio
Marcelo
Andriy Lunin
Casemiro
Federico Valverde
Luka Jović
Lucas Vázquez
Gareth Bale
Dani Ceballos
Vinícius Júnior
Rodrygo
Isco
Ferland Mendy
Mariano
Eduardo Camavinga
David Alaba"""

                correct_lines = correct_output.split("\n")
                for i, line in enumerate(lines[37:-2]):
                    self.assertEqual(line, correct_lines[i])

            finally:
                sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
