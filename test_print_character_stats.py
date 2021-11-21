from unittest import TestCase
from unittest.mock import patch
import io
from game import print_character_stats


class TestPrintCharacterStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_character_stats(self, mock_stdout):
        test_character = {'name': 'xc', 'class': 'lurker', 'level': 1, 'currentHP': 10.0,
                          'weapon': 'spear', 'currentXP': 0, 'levelUpXP': 100, 'X-coordinate': 0,
                          'Y-coordinate': 0, 'accuracy': 0.66, 'strength': 0.66,
                          'weaponMultiplier': 1,
                          'resistance': 0.66}
        expected = "\nYou now have:\n10.00 HP\n0 XP\n\nYou are a(n) trainee.\nYou need to have " \
                   "100 XP to advance to the next level\n\n"
        print_character_stats(test_character, False)
        self.assertEqual(expected, mock_stdout.getvalue())
