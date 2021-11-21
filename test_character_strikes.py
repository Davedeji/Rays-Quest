from unittest import TestCase
from unittest.mock import patch
import io
from game import character_strikes


class TestCharacterStrikes(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_character_strikes(self, mock_stdout):
        test_character = {'resistance': 3, 'currentHP': 10, 'currentXP': 0, 'strength': 1,
                          'name': 'Champ', 'weapon': 'Sword', 'weaponMultiplier': 2}
        test_foe = {'strength': 1, 'name': 'Champ', 'weapon': 'Spear', 'resistance': 3,
                    'currentHP': 10, 'currentXP': 0, }
        expected_print = "\x1b[1;32;40mYou struck Champ with Sword\nYou did 0.67 damage\n\x1b[0m\n"
        character_strikes(test_character, test_foe)
        self.assertEqual(mock_stdout.getvalue(), expected_print)


