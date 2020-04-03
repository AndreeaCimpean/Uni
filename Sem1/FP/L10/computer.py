import random


class ComputerPlayer:
    def __init__(self, board):
        self.draw_computer_planes(board)
        self._guess_stack = []
        self._previous_guess = ()
        self._not_checked = []
        for i in range(0, 8):
            for j in range(1, 9):
                self._not_checked.append((chr(i + ord('A')), j))

    def draw_computer_planes(self, board):
        '''
        :param board: computer's board
        Draw computer's planes randomly
        '''
        orientations = ['up', 'down', 'left', 'right']
        while True:
            board.clear_board()
            i1 = random.randint(0, 7)
            j1 = random.randint(1, 8)
            orientation1 = random.choice(orientations)
            i2 = random.randint(0, 7)
            j2 = random.randint(1, 8)
            orientation2 = random.choice(orientations)
            try:
                p1 = board.draw_plane((chr(i1 + ord('A')), j1), orientation1)
                p2 = board.draw_plane((chr(i2 + ord('A')), j2), orientation2)
                break
            except ValueError:
                pass
        board.plane1 = p1
        board.plane2 = p2

    def random_guess(self):
        '''
        :return: A random guess
        '''
        guess = random.choice(self._not_checked)
        return guess

    def calculateGuess(self, guess_board):
        '''
        :param guess_board: computer's guess board
        :return: Computer's guess
        '''

        if len(self._previous_guess) > 0 and guess_board.get(self._previous_guess[0], self._previous_guess[1]) == -3:
            self.remove_checked(guess_board)
            self._guess_stack.clear()
        if len(self._previous_guess) > 0 and guess_board.get(self._previous_guess[0], self._previous_guess[1]) == -2:
            neighbours = self.available_neighbours(self._previous_guess[0], self._previous_guess[1], guess_board)
            for n in neighbours:
                self._guess_stack.append(n)

        if len(self._guess_stack) == 0:
            guess = self.random_guess()
        else:
            guess = self._guess_stack.pop()

        self._previous_guess = guess
        self._not_checked.remove(guess)
        return guess

    def remove_checked(self, guess_board):
        '''
        :param guess_board: the guess board of the computer
        Remove all checked cells from the list of not_checked cells
        '''
        for i in range(0, 8):
            for j in range(1, 9):
                g = (chr(i + ord('A')), j)
                if guess_board.get(g[0], g[1]) == -2 and g in self._not_checked:
                    self._not_checked.remove(g)

    def available_neighbours(self, x, y, guess_board):
        '''
        :param x: the row of the given cell
        :param y: the column of the given cell
        :param guess_board: the guess board of the computer
        :return: The valid and not checked neighbours of the given cell
        '''
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        neighbours = []
        for i in range(4):
            neighbour = (chr(ord(x) + directions[i][0]), y + directions[i][1])
            if neighbour[0] in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] and 0 < neighbour[1] < 9 \
                    and guess_board.get(neighbour[0], neighbour[1]) == 0 and neighbour not in self._guess_stack:
                neighbours.append(neighbour)
        if len(neighbours) > 0:
            random.shuffle(neighbours)
        return neighbours
