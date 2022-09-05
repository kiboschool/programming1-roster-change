from unittest.mock import patch
from unittest import TestCase
import unittest
import sys
import io

class Test(TestCase):
    def test_output(self):
        with patch('sys.stdout', new=io.StringIO()) as mock_stdout:
            import main
            lines = mock_stdout.getvalue().split("\n")
            self.assertEqual(lines[1], "The current Real Madrid roster:") 
            self.assertEqual(lines[3], "Thibaut Courtois") 
            self.assertEqual(lines[35], "The new Real Madrid roster:") 
            self.assertEqual(lines[37], "Thibaut Courtois") 
            self.assertEqual("\n".join(lines[37:-1]), """Thibaut Courtois
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
David Alaba""")
            sys.modules.pop('main')

if __name__ == '__main__':
    unittest.main()
