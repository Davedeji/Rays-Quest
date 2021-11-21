from unittest import TestCase
from game import make_board


class TestMakeBoard(TestCase):
    def test_make_board(self):
        expected = {(0, 0): 'none', (1, 0): 'none', (2, 0): 'none', (3, 0): 'none', (4, 0): 'wall',
                    (5, 0): 'none', (6, 0): 'none', (7, 0): 'none', (8, 0): 'none', (9, 0): 'none',
                    (10, 0): 'none', (11, 0): 'none', (12, 0): 'wall', (13, 0): 'none',
                    (14, 0): 'none', (15, 0): 'none', (16, 0): 'none', (17, 0): 'none',
                    (18, 0): 'none', (19, 0): 'none', (20, 0): 'none', (21, 0): 'none',
                    (22, 0): 'none', (23, 0): 'none', (24, 0): 'none', (0, 1): 'none',
                    (1, 1): 'none', (2, 1): 'none', (3, 1): 'none', (4, 1): 'wall',
                    (5, 1): 'none', (6, 1): 'none', (7, 1): 'none', (8, 1): 'none',
                    (9, 1): 'none', (10, 1): 'none', (11, 1): 'none', (12, 1): 'wall',
                    (13, 1): 'none', (14, 1): 'none', (15, 1): 'none', (16, 1): 'none',
                    (17, 1): 'none', (18, 1): 'none', (19, 1): 'none', (20, 1): 'none',
                    (21, 1): 'none', (22, 1): 'none', (23, 1): 'boss', (24, 1): 'none',
                    (0, 2): 'none', (1, 2): 'none', (2, 2): 'none', (3, 2): 'none',
                    (4, 2): 'wall', (5, 2): 'none', (6, 2): 'none', (7, 2): 'none',
                    (8, 2): 'none', (9, 2): 'none', (10, 2): 'none', (11, 2): 'none',
                    (12, 2): 'wall', (13, 2): 'none', (14, 2): 'none', (15, 2): 'none',
                    (16, 2): 'none', (17, 2): 'none', (18, 2): 'none', (19, 2): 'none',
                    (20, 2): 'none', (21, 2): 'none', (22, 2): 'none', (23, 2): 'none',
                    (24, 2): 'none', (0, 3): 'none', (1, 3): 'none', (2, 3): 'none',
                    (3, 3): 'none', (4, 3): 'wall', (5, 3): 'none', (6, 3): 'none',
                    (7, 3): 'none', (8, 3): 'none', (9, 3): 'none', (10, 3): 'none',
                    (11, 3): 'none', (12, 3): 'wall', (13, 3): 'none', (14, 3): 'none',
                    (15, 3): 'none', (16, 3): 'none', (17, 3): 'none', (18, 3): 'none',
                    (19, 3): 'none', (20, 3): 'none', (21, 3): 'none', (22, 3): 'none',
                    (23, 3): 'none', (24, 3): 'none', (0, 4): 'none', (1, 4): 'none',
                    (2, 4): 'none', (3, 4): 'none', (4, 4): 'wall', (5, 4): 'none',
                    (6, 4): 'none', (7, 4): 'none', (8, 4): 'wall', (9, 4): 'none',
                    (10, 4): 'none', (11, 4): 'none', (12, 4): 'wall', (13, 4): 'wall',
                    (14, 4): 'wall', (15, 4): 'wall', (16, 4): 'wall', (17, 4): 'wall',
                    (18, 4): 'wall', (19, 4): 'wall', (20, 4): 'wall', (21, 4): 'wall',
                    (22, 4): 'none', (23, 4): 'none', (24, 4): 'none', (0, 5): 'none',
                    (1, 5): 'none', (2, 5): 'none', (3, 5): 'none', (4, 5): 'wall',
                    (5, 5): 'none', (6, 5): 'none', (7, 5): 'none', (8, 5): 'wall',
                    (9, 5): 'none', (10, 5): 'none', (11, 5): 'none', (12, 5): 'none',
                    (13, 5): 'none', (14, 5): 'none', (15, 5): 'none', (16, 5): 'none',
                    (17, 5): 'none', (18, 5): 'none', (19, 5): 'none', (20, 5): 'none',
                    (21, 5): 'wall', (22, 5): 'none', (23, 5): 'none', (24, 5): 'none',
                    (0, 6): 'none', (1, 6): 'none', (2, 6): 'none', (3, 6): 'none',
                    (4, 6): 'wall', (5, 6): 'none', (6, 6): 'none', (7, 6): 'none',
                    (8, 6): 'wall', (9, 6): 'none', (10, 6): 'none', (11, 6): 'none',
                    (12, 6): 'none', (13, 6): 'none', (14, 6): 'none', (15, 6): 'none',
                    (16, 6): 'none', (17, 6): 'none', (18, 6): 'none', (19, 6): 'none',
                    (20, 6): 'none', (21, 6): 'wall', (22, 6): 'none', (23, 6): 'none',
                    (24, 6): 'none', (0, 7): 'none', (1, 7): 'none', (2, 7): 'none',
                    (3, 7): 'none', (4, 7): 'wall', (5, 7): 'none', (6, 7): 'none',
                    (7, 7): 'none', (8, 7): 'wall', (9, 7): 'none', (10, 7): 'none',
                    (11, 7): 'none', (12, 7): 'none', (13, 7): 'none', (14, 7): 'none',
                    (15, 7): 'none', (16, 7): 'none', (17, 7): 'none', (18, 7): 'none',
                    (19, 7): 'none', (20, 7): 'none', (21, 7): 'wall', (22, 7): 'none',
                    (23, 7): 'none', (24, 7): 'none', (0, 8): 'none', (1, 8): 'none',
                    (2, 8): 'none', (3, 8): 'none', (4, 8): 'wall', (5, 8): 'none',
                    (6, 8): 'none', (7, 8): 'none', (8, 8): 'wall', (9, 8): 'none',
                    (10, 8): 'none', (11, 8): 'none', (12, 8): 'none', (13, 8): 'none',
                    (14, 8): 'none', (15, 8): 'none', (16, 8): 'none', (17, 8): 'none',
                    (18, 8): 'none', (19, 8): 'none', (20, 8): 'none', (21, 8): 'wall',
                    (22, 8): 'none', (23, 8): 'none', (24, 8): 'none', (0, 9): 'none',
                    (1, 9): 'none', (2, 9): 'none', (3, 9): 'none', (4, 9): 'wall',
                    (5, 9): 'none', (6, 9): 'none', (7, 9): 'none', (8, 9): 'wall',
                    (9, 9): 'none', (10, 9): 'none', (11, 9): 'none', (12, 9): 'none',
                    (13, 9): 'none', (14, 9): 'none', (15, 9): 'none', (16, 9): 'none',
                    (17, 9): 'none', (18, 9): 'none', (19, 9): 'none', (20, 9): 'none',
                    (21, 9): 'wall', (22, 9): 'none', (23, 9): 'none', (24, 9): 'none',
                    (0, 10): 'none', (1, 10): 'none', (2, 10): 'none', (3, 10): 'none',
                    (4, 10): 'wall', (5, 10): 'none', (6, 10): 'none', (7, 10): 'none',
                    (8, 10): 'wall', (9, 10): 'none', (10, 10): 'none', (11, 10): 'none',
                    (12, 10): 'none', (13, 10): 'none', (14, 10): 'none', (15, 10): 'none',
                    (16, 10): 'none', (17, 10): 'none', (18, 10): 'none', (19, 10): 'none',
                    (20, 10): 'none', (21, 10): 'wall', (22, 10): 'none', (23, 10): 'none',
                    (24, 10): 'none', (0, 11): 'none', (1, 11): 'none', (2, 11): 'none',
                    (3, 11): 'none', (4, 11): 'wall', (5, 11): 'none', (6, 11): 'none',
                    (7, 11): 'none', (8, 11): 'wall', (9, 11): 'none', (10, 11): 'none',
                    (11, 11): 'none', (12, 11): 'none', (13, 11): 'none', (14, 11): 'none',
                    (15, 11): 'none', (16, 11): 'none', (17, 11): 'none', (18, 11): 'none',
                    (19, 11): 'none', (20, 11): 'none', (21, 11): 'wall', (22, 11): 'none',
                    (23, 11): 'none', (24, 11): 'none', (0, 12): 'none', (1, 12): 'none',
                    (2, 12): 'none', (3, 12): 'none', (4, 12): 'wall', (5, 12): 'none',
                    (6, 12): 'none', (7, 12): 'none', (8, 12): 'wall', (9, 12): 'none',
                    (10, 12): 'none', (11, 12): 'none', (12, 12): 'none', (13, 12): 'none',
                    (14, 12): 'none', (15, 12): 'none', (16, 12): 'none', (17, 12): 'none',
                    (18, 12): 'none', (19, 12): 'none', (20, 12): 'none', (21, 12): 'wall',
                    (22, 12): 'none', (23, 12): 'none', (24, 12): 'none', (0, 13): 'none',
                    (1, 13): 'none', (2, 13): 'none', (3, 13): 'none', (4, 13): 'wall',
                    (5, 13): 'none', (6, 13): 'none', (7, 13): 'none', (8, 13): 'wall',
                    (9, 13): 'none', (10, 13): 'none', (11, 13): 'none', (12, 13): 'none',
                    (13, 13): 'none', (14, 13): 'none', (15, 13): 'none', (16, 13): 'none',
                    (17, 13): 'none', (18, 13): 'none', (19, 13): 'none', (20, 13): 'none',
                    (21, 13): 'wall', (22, 13): 'none', (23, 13): 'none', (24, 13): 'none',
                    (0, 14): 'none', (1, 14): 'none', (2, 14): 'none', (3, 14): 'none',
                    (4, 14): 'wall', (5, 14): 'none', (6, 14): 'none', (7, 14): 'none',
                    (8, 14): 'wall', (9, 14): 'none', (10, 14): 'none', (11, 14): 'none',
                    (12, 14): 'none', (13, 14): 'none', (14, 14): 'none', (15, 14): 'none',
                    (16, 14): 'none', (17, 14): 'none', (18, 14): 'none', (19, 14): 'none',
                    (20, 14): 'none', (21, 14): 'wall', (22, 14): 'none', (23, 14): 'none',
                    (24, 14): 'none', (0, 15): 'none', (1, 15): 'none', (2, 15): 'none',
                    (3, 15): 'none', (4, 15): 'wall', (5, 15): 'none', (6, 15): 'none',
                    (7, 15): 'none', (8, 15): 'wall', (9, 15): 'none', (10, 15): 'none',
                    (11, 15): 'none', (12, 15): 'none', (13, 15): 'none', (14, 15): 'none',
                    (15, 15): 'none', (16, 15): 'none', (17, 15): 'none', (18, 15): 'none',
                    (19, 15): 'none', (20, 15): 'none', (21, 15): 'wall', (22, 15): 'none',
                    (23, 15): 'none', (24, 15): 'none', (0, 16): 'none', (1, 16): 'none',
                    (2, 16): 'none', (3, 16): 'none', (4, 16): 'wall', (5, 16): 'none',
                    (6, 16): 'none', (7, 16): 'none', (8, 16): 'wall', (9, 16): 'none',
                    (10, 16): 'none', (11, 16): 'none', (12, 16): 'none', (13, 16): 'none',
                    (14, 16): 'none', (15, 16): 'none', (16, 16): 'none', (17, 16): 'none',
                    (18, 16): 'none', (19, 16): 'none', (20, 16): 'none', (21, 16): 'wall',
                    (22, 16): 'none', (23, 16): 'none', (24, 16): 'none', (0, 17): 'none',
                    (1, 17): 'none', (2, 17): 'none', (3, 17): 'none', (4, 17): 'wall',
                    (5, 17): 'none', (6, 17): 'none', (7, 17): 'none', (8, 17): 'wall',
                    (9, 17): 'none', (10, 17): 'none', (11, 17): 'none', (12, 17): 'none',
                    (13, 17): 'none', (14, 17): 'none', (15, 17): 'none', (16, 17): 'none',
                    (17, 17): 'none', (18, 17): 'none', (19, 17): 'none', (20, 17): 'none',
                    (21, 17): 'wall', (22, 17): 'none', (23, 17): 'none', (24, 17): 'none',
                    (0, 18): 'none', (1, 18): 'none', (2, 18): 'none', (3, 18): 'none',
                    (4, 18): 'wall', (5, 18): 'none', (6, 18): 'none', (7, 18): 'none',
                    (8, 18): 'wall', (9, 18): 'none', (10, 18): 'none', (11, 18): 'none',
                    (12, 18): 'none', (13, 18): 'none', (14, 18): 'none', (15, 18): 'none',
                    (16, 18): 'none', (17, 18): 'none', (18, 18): 'none', (19, 18): 'none',
                    (20, 18): 'none', (21, 18): 'wall', (22, 18): 'none', (23, 18): 'none',
                    (24, 18): 'none', (0, 19): 'none', (1, 19): 'none', (2, 19): 'none',
                    (3, 19): 'none', (4, 19): 'wall', (5, 19): 'none', (6, 19): 'none',
                    (7, 19): 'none', (8, 19): 'wall', (9, 19): 'none', (10, 19): 'none',
                    (11, 19): 'none', (12, 19): 'none', (13, 19): 'none', (14, 19): 'none',
                    (15, 19): 'none', (16, 19): 'none', (17, 19): 'none', (18, 19): 'none',
                    (19, 19): 'none', (20, 19): 'none', (21, 19): 'wall', (22, 19): 'none',
                    (23, 19): 'none', (24, 19): 'none', (0, 20): 'none', (1, 20): 'none',
                    (2, 20): 'none', (3, 20): 'none', (4, 20): 'none', (5, 20): 'none',
                    (6, 20): 'none', (7, 20): 'none', (8, 20): 'wall', (9, 20): 'none',
                    (10, 20): 'none', (11, 20): 'none', (12, 20): 'none', (13, 20): 'none',
                    (14, 20): 'none', (15, 20): 'none', (16, 20): 'none', (17, 20): 'none',
                    (18, 20): 'none', (19, 20): 'none', (20, 20): 'none', (21, 20): 'wall',
                    (22, 20): 'none', (23, 20): 'none', (24, 20): 'none', (0, 21): 'none',
                    (1, 21): 'none', (2, 21): 'none', (3, 21): 'none', (4, 21): 'none',
                    (5, 21): 'none', (6, 21): 'none', (7, 21): 'none', (8, 21): 'wall',
                    (9, 21): 'none', (10, 21): 'none', (11, 21): 'none', (12, 21): 'none',
                    (13, 21): 'none', (14, 21): 'none', (15, 21): 'none', (16, 21): 'none',
                    (17, 21): 'none', (18, 21): 'none', (19, 21): 'none', (20, 21): 'none',
                    (21, 21): 'none', (22, 21): 'none', (23, 21): 'none', (24, 21): 'none',
                    (0, 22): 'none', (1, 22): 'none', (2, 22): 'none', (3, 22): 'none',
                    (4, 22): 'none', (5, 22): 'none', (6, 22): 'none', (7, 22): 'none',
                    (8, 22): 'wall', (9, 22): 'none', (10, 22): 'none', (11, 22): 'none',
                    (12, 22): 'none', (13, 22): 'none', (14, 22): 'none', (15, 22): 'none',
                    (16, 22): 'none', (17, 22): 'none', (18, 22): 'none', (19, 22): 'none',
                    (20, 22): 'none', (21, 22): 'none', (22, 22): 'none', (23, 22): 'none',
                    (24, 22): 'none', (0, 23): 'none', (1, 23): 'none', (2, 23): 'none',
                    (3, 23): 'none', (4, 23): 'none', (5, 23): 'none', (6, 23): 'none',
                    (7, 23): 'none', (8, 23): 'wall', (9, 23): 'none', (10, 23): 'none',
                    (11, 23): 'none', (12, 23): 'none', (13, 23): 'none', (14, 23): 'none',
                    (15, 23): 'none', (16, 23): 'none', (17, 23): 'none', (18, 23): 'none',
                    (19, 23): 'none', (20, 23): 'none', (21, 23): 'none', (22, 23): 'none',
                    (23, 23): 'none', (24, 23): 'none', (0, 24): 'none', (1, 24): 'none',
                    (2, 24): 'none', (3, 24): 'none', (4, 24): 'none', (5, 24): 'none',
                    (6, 24): 'none', (7, 24): 'none', (8, 24): 'wall', (9, 24): 'none',
                    (10, 24): 'none', (11, 24): 'none', (12, 24): 'none', (13, 24): 'none',
                    (14, 24): 'none', (15, 24): 'none', (16, 24): 'none', (17, 24): 'none',
                    (18, 24): 'none', (19, 24): 'none', (20, 24): 'none', (21, 24): 'none',
                    (22, 24): 'none', (23, 24): 'none', (24, 24): 'none'}

        actual = make_board()
        self.assertEqual(expected, actual)
