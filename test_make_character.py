from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestMakeCharacter(TestCase):
    @patch('game.validate_num_choice', return_value="2")
    @patch('game.GET_CLASS_NAMES',
           return_value=('instigator', 'lurker', 'protector', 'distributor'))
    @patch('game.get_class_attack_defense_levels',
           return_value=[0.66, 0.66, 0.66])
    @patch('builtins.input', side_effect=['xc', '2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_character(self, _, __, ___, ____, ______):
        expected = {'name': 'xc', 'class': 'lurker', 'level': 1, 'currentHP': 10.0,
                    'weapon': 'spear', 'currentXP': 0, 'levelUpXP': 100, 'X-coordinate': 0,
                    'Y-coordinate': 0, 'accuracy': 0.66, 'strength': 0.66, 'weaponMultiplier': 1,
                    'resistance': 0.66}
        actual = game.make_character()
        self.assertEqual(actual, expected)
