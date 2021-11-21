from unittest import TestCase
from unittest.mock import patch
import io
from game import print_enemy_stats


class TestPrintEnemyStats(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_enemy_stats(self, mock_stdout):
        test_foe = {'strength': 1, 'name': 'Champ', 'weapon': 'Spear', 'currentHP': 5}
        expected = "\nYour enemy has:\n5.00 HP\n"
        print_enemy_stats(test_foe)
        self.assertEqual(expected, mock_stdout.getvalue())
