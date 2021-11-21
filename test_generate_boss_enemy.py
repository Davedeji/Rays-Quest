from unittest import TestCase
from game import generate_boss_enemy


class TestGenerateBossEnemy(TestCase):
    def test_generate_boss_enemy(self):
        expected = {'name': "Megatron", 'weapon': "Sword", 'accuracy': 1.0, 'resistance': 3.0,
                    'strength': 3.0, 'currentHP': 7, 'is_boss': True}
        actual = generate_boss_enemy("Megatron", "Sword")
        self.assertEqual(actual, expected)
