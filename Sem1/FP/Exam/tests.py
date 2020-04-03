import unittest
from board import *


class TestPlaceStars(unittest.TestCase):
    def test_empty_neighbours(self):
        board = Board()
        for i in range(0, 8):
            for j in range(1, 9):
                board.set_cell(chr(ord("A") + i), j, 0)
        for i in range(0, 7):
            for j in range(1, 8):
                self.assertEqual(board.empty_neighbours(chr(ord("A") + i), j), True)
        board.set_cell("A", 1, 1)
        self.assertEqual(board.empty_neighbours("B", 1), False)
        self.assertEqual(board.empty_neighbours("A", 1), True)

    def test_place_stars(self):
        board = Board()
        for i in range(0, 8):
            for j in range(1, 9):
                board.set_cell(chr(ord("A") + i), j, 0)
        board.place_stars()
        count_stars = 0
        for i in range(0, 8):
            for j in range(1, 9):
                if board.get_cell(chr(ord("A") + i), j) == 1:
                    count_stars += 1
        self.assertEqual(count_stars, 10)
        for i in range(0, 8):
            for j in range(1, 9):
                if board.get_cell(chr(ord("A") + i), j) == 1:
                    self.assertEqual(board.empty_neighbours(chr(ord("A") + i), j), True)