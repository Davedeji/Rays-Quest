from unittest import TestCase
from game import generate_level_three_enemy


class TestGenerateLevelThreeEnemy(TestCase):
    def test_generate_level_three_enemy(self):
        expected = {'name': "Champion", 'weapon': "Sword", 'accuracy': 1.2, 'resistance': 1.5,
                    'strength': 1.2, 'currentHP': 6, 'is_boss': False}
        actual = generate_level_three_enemy("Champion", "Sword")
        self.assertEqual(actual, expected)
