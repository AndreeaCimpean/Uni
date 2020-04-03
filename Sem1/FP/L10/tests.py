from Game import *
from board import *
from computer import *
import unittest


class TestBoard(unittest.TestCase):
    def test_get_set_cell(self):
        b = Board()
        b.set('A', 1, -1)
        b.set('B', 2, -2)
        self.assertEqual(b.get('A', 1), -1)
        self.assertEqual(b.get('B', 2), -2)
        self.assertEqual(b.get('C', 3), 0)

    def test_clear_board(self):
        b = Board()
        b.set('A', 1, -1)
        b.set('B', 2, -2)
        b.clear_board()
        for i in range(8):
            for j in range(1, 9):
                value = b.get(chr(i + ord('A')), j)
                if value == 0:
                    assert True

    def test_validate_position(self):
        b = PlayBoard()
        b.set('A', 1, 1)
        self.assertEqual(b.validate_position(('B',2)), None)
        with self.assertRaises(ValueError):
            b.validate_position(('A', 1))
        with self.assertRaises(ValueError):
            b.validate_position(('J', 5))

    def test_draw_plane(self):
        b = PlayBoard()
        b.draw_plane(('A', 3), "down")
        self.assertEqual(b.get('A', 3), 2)
        self.assertEqual(b.get('B', 3), 1)
        self.assertEqual(b.get('B', 2), 1)
        self.assertEqual(b.get('B', 1), 1)
        self.assertEqual(b.get('B', 4), 1)
        self.assertEqual(b.get('B', 5), 1)
        self.assertEqual(b.get('C', 3), 1)
        self.assertEqual(b.get('D', 3), 1)
        self.assertEqual(b.get('D', 2), 1)
        self.assertEqual(b.get('D', 4), 1)
        count = 0
        for i in range(8):
            for j in range(1, 9):
                if b.get(chr(i + ord('A')), j) == 0:
                    count += 1
        self.assertEqual(count, 54)

        with self.assertRaises(ValueError):
            b.draw_plane(('B', 5), "right")

        with self.assertRaises(ValueError):
            b.draw_plane(('J', 8), "left")

        with self.assertRaises(ValueError):
            b.draw_plane(('A', 9), "left")

        with self.assertRaises(ValueError):
            b.draw_plane(('D', 6), 'centre')

    def test_is_cabin(self):
        b = PlayBoard()
        b.draw_plane(('A', 3), "down")
        self.assertEqual(b.is_cabin('A', 3), True)
        self.assertNotEqual(b.is_cabin('B', 3), True)

    def test_is_part_of_plane(self):
        b = PlayBoard()
        b.draw_plane(('A', 3), "down")
        self.assertEqual(b.is_part_of_plane('B', 3), True)
        self.assertNotEqual(b.is_part_of_plane('H', 8), True)

    def test_guess(self):
        b = PlayBoard()
        g = GuessBoard()
        b.plane1 = b.draw_plane(('A', 3), "down")
        b.plane2 = b.draw_plane(('D', 6), "down")
        g.guess('B', 3, b)
        self.assertEqual(g.get('B', 3), -2)
        self.assertEqual(b.get('B', 3), -2)
        g.guess('H', 1, b)
        self.assertEqual(g.get('H', 1), -1)
        self.assertEqual(b.get('H', 1), -1)
        g.guess('A', 3, b)
        self.assertEqual(g.get('A', 3), -3)
        self.assertEqual(b.get('A', 3), -3)

        cells = b.plane1.determine_cells()
        for i in cells:
            self.assertEqual(g.get(i[0], i[1]), -2)
            self.assertEqual(b.get(i[0], i[1]), -2)

        with self.assertRaises(ValueError):
            g.guess('J', 5, b)
        with self.assertRaises(ValueError):
            g.guess('A', 3, b)
        with self.assertRaises(ValueError):
            g.guess('A', 9, b)

    def test_determine_guess_symbol(self):
        b = PlayBoard()
        g = GuessBoard()
        b.plane1 = b.draw_plane(('A', 3), "down")
        b.plane2 = b.draw_plane(('D', 6), "down")
        self.assertEqual(g.determine_guess_symbol('B', 3, b), -2)
        self.assertEqual(g.determine_guess_symbol('H', 8, b), -1)
        self.assertEqual(g.determine_guess_symbol('A', 3, b), -3)

    def test_is_won(self):
        b = PlayBoard()
        g = GuessBoard()
        b.plane1 = b.draw_plane(('A', 3), "down")
        b.plane2 = b.draw_plane(('D', 6), "down")
        self.assertEqual(g.isWon(), False)
        g.guess('A', 3, b)
        self.assertEqual(g.isWon(), False)
        g.guess('D', 6, b)
        self.assertEqual(g.isWon(), True)

    def test_determine_plane_cells(self):
        p = Plane(('A', 3), "down")
        cells = p.determine_cells()
        self.assertIn(('B', 3), cells)
        self.assertIn(('B', 2), cells)
        self.assertIn(('B', 1), cells)
        self.assertIn(('B', 4), cells)
        self.assertIn(('B', 5), cells)
        self.assertIn(('C', 3), cells)
        self.assertIn(('D', 3), cells)
        self.assertIn(('D', 2), cells)
        self.assertIn(('D', 4), cells)


class TestPlayer(unittest.TestCase):
    def test_player_guess(self):
        playerBoard = PlayBoard()
        playerBoard.plane1 = playerBoard.draw_plane(('A', 3), "down")
        playerBoard.plane2 = playerBoard.draw_plane(('D', 6), "down")
        playerGuessBoard = GuessBoard()
        computerBoard = PlayBoard()
        computerGuessBoard = GuessBoard()
        computerPlayer = ComputerPlayer(computerBoard)
        game = Game(playerBoard, computerBoard, playerGuessBoard, computerGuessBoard, computerPlayer)
        game.playerGuess('A', 1)
        game.playerGuess('B', 1)
        count = 0
        for i in range(8):
            for j in range(1, 9):
                if playerGuessBoard.get(chr(i + ord('A')), j) != 0:
                    count += 1
        self.assertEqual(count, 2)

        with self.assertRaises(ValueError):
            game.playerGuess('A', 1)

        with self.assertRaises(ValueError):
            game.playerGuess('J', 5)

        with self.assertRaises(ValueError):
            game.playerGuess('A', 9)


class TestComputerPlayer(unittest.TestCase):
    def test_draw_planes(self):
        b = PlayBoard()
        comp = ComputerPlayer(b)
        count_cabines = 0
        count_planes = 0
        conut_air = 0
        for i in range(8):
            for j in range(1, 9):
                value = b.get(chr(i + ord('A')), j)
                if value == 0:
                    conut_air += 1
                elif value == 1:
                    count_planes += 1
                else:
                    count_cabines += 1
        self.assertEqual(count_cabines, 2)
        self.assertEqual(count_planes, 18)
        self.assertEqual(conut_air, 44)

    def test_computer_guess(self):
        playerBoard = PlayBoard()
        playerBoard.plane1 = playerBoard.draw_plane(('A', 3), "down")
        playerBoard.plane2 = playerBoard.draw_plane(('D', 6), "down")
        playerGuessBoard = GuessBoard()
        computerBoard = PlayBoard()
        computerGuessBoard = GuessBoard()
        computerPlayer = ComputerPlayer(computerBoard)
        game = Game(playerBoard, computerBoard, playerGuessBoard, computerGuessBoard, computerPlayer)
        game.computerGuess()
        game.computerGuess()
        count = 0
        for i in range(8):
            for j in range(1, 9):
                if computerGuessBoard.get(chr(i + ord('A')), j) != 0:
                    count += 1
        self.assertGreaterEqual(count, 2)

    def test_remove_checked(self):
        computerBoard = PlayBoard()
        computerGuessBoard = GuessBoard()
        computerPlayer = ComputerPlayer(computerBoard)
        computerGuessBoard.set('A', 1, -2)
        computerGuessBoard.set('B', 2, -2)
        computerPlayer.remove_checked(computerGuessBoard)
        self.assertNotIn(('A', 1), computerPlayer._not_checked)
        self.assertNotIn(('B', 2), computerPlayer._not_checked)

    def test_available_neighbours(self):
        computerBoard = PlayBoard()
        computerGuessBoard = GuessBoard()
        computerPlayer = ComputerPlayer(computerBoard)
        computerGuessBoard.set('A', 1, -2)
        neighbours = computerPlayer.available_neighbours('B', 1, computerGuessBoard)
        self.assertNotIn(('A', 1), neighbours)
        self.assertIn(('C', 1), neighbours)
        self.assertIn(('B', 2), neighbours)
        neighbours = computerPlayer.available_neighbours('E', 4, computerGuessBoard)
        self.assertIn(('E', 3), neighbours)
        self.assertIn(('E', 5), neighbours)
        self.assertIn(('D', 4), neighbours)
        self.assertIn(('F', 4), neighbours)


