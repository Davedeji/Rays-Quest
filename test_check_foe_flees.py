from unittest import TestCase
from unittest.mock import patch
from game import check_foe_flees


class TestCheckFoeFlees(TestCase):
    @patch('random.choices', return_value=[True])
    def test_check_foe_flees_true(self, _):
        expected = True
        actual = check_foe_flees()
        self.assertEqual(expected, actual)
