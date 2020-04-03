from texttable import Texttable


class Board:
    def __init__(self):
        self._data = [0] * 36

    def __str__(self):
        t = Texttable()
        d = {1: "x", 0: " ", -1: "o"}
        for i in range(0, 31, 6):
            row = self._data[i:i+6]
            for j in range(6):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()

    def get_cell(self, x, y):
        try:
            return self._data[6*(x-1) + y-1]
        except IndexError:
            print("x: " + str(x) + " y: " +str(y))

    def set_cell(self, x, y, value):
        self._data[6*(x-1) + y-1] = value

    def max_symbol(self):
        s = 0
        for i in range(1, 6):
            for j in range(1, 6):
                s += self.get_cell(i, j)
        if s < 0:
            return -1
        return 1

    def neighbours_sum(self, i, j):
        s = 0
        neighbours = [[i-1, j], [i+1, j], [i, j-1], [i, j+1], [i-1, j-1], [i-1, j+1], [i+1, j+1], [i+1, j-1]]
        for i in range(8):
            neighbour = neighbours[i]
            if neighbour[0] < 1 or neighbour[0] > 6 or neighbour[1] < 1 or neighbour[1] > 6:
                continue
            else:
                s += self.get_cell(neighbour[0], neighbour[1])
        return s


    def move(self, x, y, symbol):
        d = {"x": 1, "o": -1}
        if symbol not in d.keys():
            raise ValueError("Invalid Symbol")
        if x < 1 or x > 6 or y < 1 or y > 6:
            raise ValueError("Invalid coordinates")
        cell = self.get_cell(x, y)
        if cell != 0:
            raise ValueError("Invalid move")
        self.set_cell(x, y, d[symbol])

    def isWon(self):
        for i in range(1, 7):
            s = 0
            for j in range(1, 7):
                s += self.get_cell(i, j)
            if (s == 5 or s == -5) and (self.get_cell(i, 1) == 0 or self.get_cell(i, 6) == 0):
                return True
        for j in range(1, 7):
            s = 0
            for i in range(1, 7):
                s += self.get_cell(i, j)
            if (s == 5 or s == -5) and (self.get_cell(1, j) == 0 or self.get_cell(6, j) == 0):
                return True
        i = 1
        j = 5
        s1 = 0
        s2 = 0
        while i <= 5:
            s1 += self.get_cell(i, j)
            s2 += self.get_cell(j, i)
            i += 1
            j -= 1
        if s1 == 5 or s1 == -5 or s2 == 5 or s2 == -5:
            return True

        i = 2
        j = 6
        s1 = 0
        s2 = 0
        while i <= 6:
            s1 += self.get_cell(i, j)
            s2 += self.get_cell(j, i)
            i += 1
            j -= 1
        if s1 == 5 or s1 == -5 or s2 == 5 or s2 == -5:
            return True

        s1 = 0
        s2 = 0
        for i in range(1, 6):
            s1 += self.get_cell(i, i)
            s2 += self.get_cell(i, 6-i-1)
        if ((s1 == 5 or s1 == -5) and (self.get_cell(1, 1) == 0 or self.get_cell(6, 6) == 0)) \
                or ((s2 == 5 or s2 == -5) and (self.get_cell(1, 6) == 0 or self.get_cell(6, 1) == 0)):
            return True

        return False

    def isFull(self):
        return 0 not in self._data
