class Game:
    def __init__(self, board, comp):
        self._board = board
        self._computer = comp

    def get_board(self):
        return self._board

    def playerMove(self, x, y, symbol):
        self._board.move(x, y, symbol)

    def computerMove(self):
        move = self._computer.calculate_move(self._board)
        self._board.move(move[0], move[1], move[2])