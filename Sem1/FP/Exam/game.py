from board import *

class Game:
    def __init__(self, board):
        self._board = board

    def get_board_for_player(self):
        auxiliary_board = Board()
        for i in range(0, 8):
            for j in range(1, 9):
                value = self._board.get_cell(chr(ord("A") + i), j)
                if value == 2:
                    value = 0
                    neighbours = self._board.get_neighbours(chr(ord("A") + i), j)
                    for neighbour in neighbours:
                        if self._board.get_cell(neighbour[0], neighbour[1]) == -2:
                            value = 2
                auxiliary_board.set_cell(chr(ord("A") + i), j, value)
        return str(auxiliary_board)

    def get_board(self):
        return self._board

    def warp(self, i, j):
        x = self._board.find_endeavour()
        y = x[1]
        x = x[0]
        if x != i:
            if y != j:
                if (abs(ord(x)-ord(i)) != abs(y-j)):
                    raise ValueError("Not a valid move")
        value = self._board.get_cell(i, j)
        if value == 1:
            raise ValueError("You cannot land on a star")
        else:
            self._board.set_cell(i, j, value - 2)
            self._board.set_cell(x, y, 0)

    def fire(self, i, j):
        x = self._board.find_endeavour()
        y = x[1]
        x = x[0]
        neighbours = self._board.get_neighbours(x, y)
        ok = 0
        for neighbour in neighbours:
            if neighbour == (i, j):
                ok = 1
        if ok == 0:
            raise ValueError("Not a valid fire")
        if self._board.get_cell(i, j) != 2:
            raise ValueError("Not a valid fire")

        count = self._board.find_number_of_ships()
        self.clear_ships()
        self._board.place_cruisers(count - 1)

    def clear_ships(self):
        for i in range(0, 8):
            for j in range(1, 9):
                if self._board.get_cell(chr(ord("A") + i), j) == 2:
                    self._board.set_cell(chr(ord("A") + i), j, 0)




