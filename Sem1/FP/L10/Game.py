class Game:
    def __init__(self, playerBoard, computerBoard, playerGuessBoard, computerGuessBoard, computerPlayer):
        self._playerBoard = playerBoard
        self._playerGuessBoard = playerGuessBoard
        self._computerBoard = computerBoard
        self._computerGuessBoard = computerGuessBoard
        self._computerPlayer = computerPlayer

    def getPlayerBoard(self):
        return self._playerBoard

    def getComputerBoard(self):
        return self._computerBoard

    def getPlayerGuessBoard(self):
        return self._playerGuessBoard

    def getComputerGuessBoard(self):
        return self._computerGuessBoard

    def playerGuess(self, x, y):
        '''
        :param x: the row of the player's guess (A-H)
        :param y: the column of the player's guess(1-8)
        Call board function guess on computer's board
        '''
        self._playerGuessBoard.guess(x, y, self._computerBoard)

    def computerGuess(self):
        '''
        Get calculated computer's guess
        Call board function guess on player's board
        '''
        guess = self._computerPlayer.calculateGuess(self._computerGuessBoard)
        self._computerGuessBoard.guess(guess[0], guess[1], self._playerBoard)

