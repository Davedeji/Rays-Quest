from unittest import TestCase
from game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_right(self):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 0}
        test_direction = 'd'
        expected_character = {'X-coordinate': 1, 'Y-coordinate': 0}
        move_character(test_character, test_direction)
        self.assertEqual(expected_character, test_character)

    def test_move_character_left(self):
        test_character = {'X-coordinate': 3, 'Y-coordinate': 0}
        test_direction = 'a'
        expected_character = {'X-coordinate': 2, 'Y-coordinate': 0}
        move_character(test_character, test_direction)
        self.assertEqual(expected_character, test_character)

    def test_move_character_up(self):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 5}
        test_direction = 'w'
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 4}
        move_character(test_character, test_direction)
        self.assertEqual(expected_character, test_character)

    def test_move_character_down(self):
        test_character = {'X-coordinate': 0, 'Y-coordinate': 6}
        test_direction = 's'
        expected_character = {'X-coordinate': 0, 'Y-coordinate': 7}
        move_character(test_character, test_direction)
        self.assertEqual(expected_character, test_character)

