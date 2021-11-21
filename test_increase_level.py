from unittest import TestCase
from game import increase_level


class TestIncreaseLevel(TestCase):
    def test_increase_level(self):
        test_character = {'name': 'xc', 'class': 'lurker', 'level': 1, 'currentHP': 10.0,
                          'weapon': 'spear', 'currentXP': 102, 'levelUpXP': 100, 'X-coordinate': 0,
                          'Y-coordinate': 0, 'accuracy': 0.66, 'strength': 0.66,
                          'weaponMultiplier': 1,
                          'resistance': 0.66}
        expected_character = {'name': 'xc', 'class': 'lurker', 'level': 2, 'currentHP': 10.0,
                              'weapon': 'spear', 'currentXP': 2, 'levelUpXP': 100,
                              'X-coordinate': 0,
                              'Y-coordinate': 0, 'accuracy': 1.32, 'strength': 1.32,
                              'weaponMultiplier': 1,
                              'resistance': 1.32}
        increase_level(test_character)
        self.assertEqual(test_character, expected_character)
