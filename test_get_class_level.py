from unittest import TestCase
from game import get_class_level


class TestGetClassLevel(TestCase):
    def test_get_class_level(self):
        expected = 'trainee'
        actual = get_class_level(1)
        self.assertEqual(actual, expected)
