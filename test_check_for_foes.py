from unittest import TestCase
from unittest.mock import patch
from game import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.choice', return_value=True)
    def test_check_for_foes(self, _):
        expected = True
        actual = check_for_foes()
        self.assertEqual(actual, expected)