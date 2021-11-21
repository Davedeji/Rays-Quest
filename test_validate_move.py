from unittest import TestCase
from unittest.mock import patch
import game


class TestValidateMove(TestCase):
    @patch('game.check_wall_bounds', return_value=False)
    def test_validate_move_valid(self, _):
        test_board = game.make_board()
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        test_direction = 'd'
        expected = True
        actual = game.validate_move(test_board, test_character, test_direction)
        self.assertEqual(actual, expected)

    @patch('game.check_wall_bounds', return_value=True)
    def test_validate_move_invalid(self, _):
        test_board = game.make_board()
        test_character = {'X-coordinate': 3, 'Y-coordinate': 3}
        test_direction = 'd'
        expected = False
        actual = game.validate_move(test_board, test_character, test_direction)
        self.assertEqual(actual, expected)