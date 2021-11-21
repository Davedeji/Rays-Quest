from unittest import TestCase
from game import generate_level_one_enemy


class TestGenerateLevelOneEnemy(TestCase):
    def test_generate_level_one_enemy(self):
        expected = {'name': "Heat", 'weapon': "Spear", 'accuracy': 0.4, 'resistance': 0.4,
                    'strength': 0.4, 'currentHP': 3, 'is_boss': False}
        actual = generate_level_one_enemy("Heat", "Spear")
        self.assertEqual(actual, expected)
