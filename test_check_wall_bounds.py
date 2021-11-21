from unittest import TestCase
import game


class TestCheckWallBounds(TestCase):
    def test_check_wall_bounds_false(self):
        test_destination = (3, 3)
        test_board = game.make_board()
        expected = False
        actual = game.check_wall_bounds(test_destination, test_board)
        self.assertEqual(expected, actual)

    def test_check_wall_bounds_true(self):
        test_destination = (4, 3)
        test_board = game.make_board()
        expected = True
        actual = game.check_wall_bounds(test_destination, test_board)
        self.assertEqual(expected, actual)
