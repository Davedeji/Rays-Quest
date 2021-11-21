from unittest import TestCase
from unittest.mock import patch
import game


class TestFoeGenerator(TestCase):
    @patch('random.choice',
           return_value={'name': 'Militia', 'weapon': 'Spear', 'accuracy': 0.4, 'resistance': 0.4,
                         'strength': 0.4, 'currentHP': 3, 'is_boss': False})
    def test_foe_generator(self, _):
        expected = {'name': 'Militia', 'weapon': 'Spear', 'accuracy': 0.4, 'resistance': 0.4,
                    'strength': 0.4, 'currentHP': 3, 'is_boss': False}
        actual = game.foe_generator(1)
        self.assertEqual(actual, expected)
