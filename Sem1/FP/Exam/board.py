from texttable import Texttable
import random


class Board:
    def __init__(self):
        self._data = [0] * 64
        self.place_stars()
        self.place_endeavour()
        self.place_cruisers(3)

    def get_cell(self, i, j):
        return self._data[((ord(i) - ord('A')) * 8 + j - 1)]

    def set_cell(self, i, j, value):
        self._data[((ord(i) - ord('A')) * 8 + j - 1)] = value

    def __str__(self):
        d = {0: " ", 1: "*", -2:"E", 2:"B"}
        t = Texttable()
        row = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
        t.add_row(row)
        for i in range(0, 64, 8):
            row = []
            row.append(chr(ord("A") + i//8))
            row += self._data[i:i+8]
            for j in range(1, 9):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()

    def empty_neighbours(self, i, j):
        '''
        Check if all neighbours of a cell are empty
        :param i: the row of the cell
        :param j: the column of the cell
        :return:
            True if all neighbours are empty
            False otherwise
        '''
        neighbours = self.get_neighbours(i, j)
        for neighbour in neighbours:
            if self.get_cell(neighbour[0], neighbour[1]) != 0:
                return False
        return True

    def get_neighbours(self, i, j):
        neighbours = []
        directionsi = [0, 0, 1, -1, 1, 1, -1, -1]
        directionsj = [1, -1, 0, 0, 1, -1, -1, 1]
        for index in range(0, 8):
            # print(index)
            neighbour = chr(ord(i) + directionsi[index]), j + directionsj[index]
            if neighbour[0] >= 'A' and neighbour[0] <= 'H' and neighbour[1] >= 1 and neighbour[1] <= 8:
                neighbours.append(neighbour)
        return neighbours

    def place_stars(self):
        '''
        Place random 10 stars on the board, so that there is no 2 adjacent stars(row, column, diagonal)
        :return:
            None, but place the start
        '''
        count = 0
        while count != 10:
            while True:
                x = random.randint(0, 7)
                x = chr(ord('A') + x)
                y = random.randint(1, 8)
                if self.get_cell(x, y) != 0:
                    continue
                else:
                    break
            if self.empty_neighbours(x, y) == False:
                continue
            else:
                self.set_cell(x, y, 1)
                count += 1

    def place_endeavour(self):
        while True:
            x = random.randint(0, 7)
            x = chr(ord('A') + x)
            y = random.randint(1, 8)
            if self.get_cell(x, y) != 0:
                continue
            else:
                break
        self.set_cell(x, y, -2)

    def place_cruisers(self, number):
        count = 0
        while count != number:
            while True:
                x = random.randint(0, 7)
                x = chr(ord('A') + x)
                y = random.randint(1, 8)
                if self.get_cell(x, y) != 0:
                    continue
                else:
                    break
            self.set_cell(x, y, 2)
            count += 1

    def is_won(self):
        count_cruisers = 0
        for i in range(0, 8):
            for j in range(1, 9):
                if self.get_cell(chr(ord("A") + i), j) == 2:
                    count_cruisers += 1
        if count_cruisers == 0:
            return True
        return False

    def is_lost(self):
        for i in range(0, 8):
            for j in range(1, 9):
                if self.get_cell(chr(ord("A") + i), j) == -2:
                    return False
        return True

    def find_number_of_ships(self):
        count_cruisers = 0
        for i in range(0, 8):
            for j in range(1, 9):
                if self.get_cell(chr(ord("A") + i), j) == 2:
                    count_cruisers += 1
        return count_cruisers

    def find_endeavour(self):
        for i in range(0, 8):
            for j in range(1, 9):
                if self.get_cell(chr(ord("A") + i), j) == -2:
                    return chr(ord("A") + i), j
