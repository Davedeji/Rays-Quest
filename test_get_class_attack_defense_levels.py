from unittest import TestCase
from game import get_class_attack_defense_levels


class TestGetClassAttackDefenseLevels(TestCase):
    def test_get_class_attack_defense_levels(self):
        expected = [0.99, 0.66, 0.33]
        actual = get_class_attack_defense_levels('distributor')
        self.assertEqual(actual, expected)
