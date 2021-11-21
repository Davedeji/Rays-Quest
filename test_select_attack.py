from unittest import TestCase
from unittest.mock import patch
import io
import game


class TestSelectAttack(TestCase):
    @patch('builtins.input', side_effect=['2'])
    def test_select_attack_choice(self, _):
        test_character = {'resistance': 3, 'currentHP': 10, 'currentXP': 0, 'strength': 1,
                          'name': 'Champ', 'weapon': 'Sword', 'weaponMultiplier': 2, 'level': 1}
        expected_character = {'resistance': 3, 'currentHP': 10, 'currentXP': 0, 'strength': 1,
                              'name': 'Champ', 'weapon': 'Special spear', 'weaponMultiplier': 1.2,
                              'level': 1}
        game.select_attack(test_character)
        self.assertEqual(expected_character, test_character)

    @patch('builtins.input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_select_attack_output(self, mock_stdout, _):
        test_character = {'resistance': 3, 'currentHP': 10, 'currentXP': 0, 'strength': 1,
                          'name': 'Champ', 'weapon': 'Sword', 'weaponMultiplier': 2, 'level': 1}
        expected_print = "\nNO Attack - strength:\n1 melee - 1\n2 Special spear - 1.2\n"
        game.select_attack(test_character)
        self.assertEqual(expected_print, mock_stdout.getvalue())
