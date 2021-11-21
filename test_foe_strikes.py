from unittest import TestCase
from unittest.mock import patch
import io
from game import foe_strikes


class TestFoeStrikes(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_foe_strikes(self, mock_stdout):
        test_character = {'resistance': 3, 'currentHP': 10, 'currentXP': 0}
        test_foe = {'strength': 1, 'name': 'Champ', 'weapon': 'Spear'}

        expected_print = "\x1b[1;31;40mChamp strikes you with Spear\nChamp does 0.33 " \
                         "damage\n\x1b[0m\n"
        foe_strikes(test_character, test_foe)
        self.assertEqual(mock_stdout.getvalue(), expected_print)
