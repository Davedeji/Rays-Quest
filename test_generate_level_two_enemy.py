from unittest import TestCase
from game import generate_level_two_enemy


class TestGeneralLevelTwoEnemy(TestCase):
    def test_generate_level_two_enemy(self):
        expected = {'name': "Heat", 'weapon': "Melee", 'accuracy': 0.7, 'resistance': 0.7,
                    'strength': 0.7, 'currentHP': 4, 'is_boss': False}
        actual = generate_level_two_enemy("Heat", "Melee")
        self.assertEqual(actual, expected)
