from texttable import Texttable


class Board:
    def __init__(self):
        self._data = [0] * 64

    def __str__(self):
        '''
        Display the board
        *   - for part of plane     - 1
        ^   - for plane's cabin     - 2
        ' ' - for air               - 0
        o   - for miss              - -1
        x   - for hit part of plane - -2
        X   - for hit cabin         - -3
        '''
        t = Texttable()
        header = [' ', '1', '2', '3', '4', '5', '6', '7', '8']
        t.header(header)
        d = {-3: 'X', -2: 'x', -1: 'o', 0: ' ', 1: '*', 2: '^'}
        for i in range(0, 57, 8):
            row = []
            row += chr(ord('A') + i//8)
            row += self._data[i:i + 8]
            for j in range(1, 9):
                row[j] = d[row[j]]
            t.add_row(row)
        return t.draw()

    def get(self, x, y):
        '''
        :param x: the row (A-H)
        :param y: the column (1-8)
        :return: the value of the cell
        '''
        return self._data[(ord(x) - ord('A')) * 8 + y - 1]

    def set(self, x, y, value):
        '''
        :param x: the row (A-H)
        :param y: the column (1-8)
        :param value: the given value
        Set the value of the cell
        '''
        self._data[(ord(x) - ord('A')) * 8 + y - 1] = value

    def clear_board(self):
        '''
        Clear a board
        '''
        for i in range(64):
            self._data[i] = 0

class PlayBoard(Board):
    def __init__(self):
        super().__init__()
        self.plane1 = []
        self.plane2 = []

    def draw_plane(self, cabin, orientation):
        '''
        :param cabin: the coordinates of the cabin
        :param orientation: the given orientation
        Draw plane in the given direction if valid input and return it (cabin on board, planes do not overlap, plane is on board)
        Raise an error otherwise
        '''
        x = cabin[0]
        y = cabin[1]
        if x not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] or y not in [1, 2, 3, 4, 5, 6, 7, 8]:
            raise ValueError("Plane's cabin is not on the board")
        if self._data[(ord(x) - ord('A')) * 8 + y - 1] != 0:
            raise ValueError("Planes overlap")
        plane = Plane(cabin, orientation)
        cells = plane.determine_cells()
        for i in cells:
            self.validate_position(i)

        self._data[(ord(x) - ord('A')) * 8 + y - 1] = 2
        for i in cells:
            self.set(i[0], i[1], 1)
        return plane

    def validate_position(self, pos):
        '''
        :param pos: the given position
        Raise an error if position is occupied/if it is outside the board
        '''
        if pos[0] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] or pos[1] < 1 or pos[1] > 8:
            raise ValueError("Plane not on the board")
        if self.get(pos[0], pos[1]) != 0:
            raise ValueError("Planes overlap")

    def is_cabin(self, x, y):
        '''
        :param x: the row of the given cell
        :param y: the column of the given cell
        :return: True if the cell contains a cabin
                 False otherwise
        '''
        return self.get(x, y) == 2

    def is_part_of_plane(self, x, y):
        '''
        :param x: the row of the given cell
        :param y: the column of the given cell
        :return: True if the cell contains a part of a plane
                 False otherwise
        '''
        return self.get(x, y) == 1


class GuessBoard(Board):
    def __init__(self):
        super().__init__()

    def guess(self, x, y, other_board):
        '''
        :param x: the row of the guess
        :param y: the column of the guess
        :param other_board: the opponent's board
        Mark on the player's guess board and the opponent's board the guess if valid input
        Raise an error otherwise
        If cabin hit mark the whole plane as hit
        '''
        if x not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] or y not in [1, 2, 3, 4, 5, 6, 7, 8]:
            raise ValueError("Guess not inside the board")
        if self._data[(ord(x) - ord('A'))*8 + y - 1] != 0:
            raise ValueError("Square already checked" + x + str(y))
        symbol = self.determine_guess_symbol(x, y, other_board)
        self.set(x, y, symbol)
        other_board.set(x, y, symbol)
        if symbol == -3:
            if other_board.plane1.Cabin[0] == x and other_board.plane1.Cabin[1] == y:
                cells = other_board.plane1.determine_cells()
            else:
                cells = other_board.plane2.determine_cells()
            for i in cells:
                self.set(i[0], i[1], -2)
                other_board.set(i[0], i[1], -2)

    def determine_guess_symbol(self, x, y, other_board):
        '''
        :param x: the row of the guess
        :param y: the column of the guess
        :param other_board: the opponent's board
        :return: the result of the guess
        '''
        if other_board.is_cabin(x, y):
            return -3
        if other_board.is_part_of_plane(x, y):
            return -2
        return -1

    def isWon(self):
        '''
        :return: True if player has won
                 False otherwise
        '''
        cabin_hit_count = 0
        for i in self._data:
            if i == -3:
                cabin_hit_count += 1
        return cabin_hit_count == 2


class Plane:
    def __init__(self, cabin, orientation):
        self.Cabin = cabin
        self.Orientation = orientation

    @property
    def Cabin(self):
        return self._cabin

    @Cabin.setter
    def Cabin(self, value):
        self._cabin = value

    @property
    def Orientation(self):
        return self._orientation

    @Orientation.setter
    def Orientation(self, value):
        self._orientation = value

    def determine_cells(self):
        '''
        :return: The corresponding cells of the plane
        '''
        cells = []
        x = self.Cabin[0]
        y = self.Cabin[1]
        if self.Orientation == "up":
            cells.append((chr(ord(x) - 1), y))
            cells.append((chr(ord(x) - 1), y - 1))
            cells.append((chr(ord(x) - 1), y - 2))
            cells.append((chr(ord(x) - 1), y + 1))
            cells.append((chr(ord(x) - 1), y + 2))
            cells.append((chr(ord(x) - 2), y))
            cells.append((chr(ord(x) - 3), y))
            cells.append((chr(ord(x) - 3), y - 1))
            cells.append((chr(ord(x) - 3), y + 1))
        elif self.Orientation == "down":
            cells.append((chr(ord(x) + 1), y))
            cells.append((chr(ord(x) + 1), y - 1))
            cells.append((chr(ord(x) + 1), y - 2))
            cells.append((chr(ord(x) + 1), y + 1))
            cells.append((chr(ord(x) + 1), y + 2))
            cells.append((chr(ord(x) + 2), y))
            cells.append((chr(ord(x) + 3), y))
            cells.append((chr(ord(x) + 3), y - 1))
            cells.append((chr(ord(x) + 3), y + 1))
        elif self.Orientation == "left":
            cells.append((chr(ord(x)), y - 1))
            cells.append((chr(ord(x) - 1), y - 1))
            cells.append((chr(ord(x) - 2), y - 1))
            cells.append((chr(ord(x) + 1), y - 1))
            cells.append((chr(ord(x) + 2), y - 1))
            cells.append((chr(ord(x)), y - 2))
            cells.append((chr(ord(x)), y - 3))
            cells.append((chr(ord(x) - 1), y - 3))
            cells.append((chr(ord(x) + 1), y - 3))
        else:
            cells.append((chr(ord(x)), y + 1))
            cells.append((chr(ord(x) - 1), y + 1))
            cells.append((chr(ord(x) - 2), y + 1))
            cells.append((chr(ord(x) + 1), y + 1))
            cells.append((chr(ord(x) + 2), y + 1))
            cells.append((chr(ord(x)), y + 2))
            cells.append((chr(ord(x)), y + 3))
            cells.append((chr(ord(x) + 1), y + 3))
            cells.append((chr(ord(x) - 1), y + 3))
        return cells

