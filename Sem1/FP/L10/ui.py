from Game import *
from board import *
from computer import *
from texttable import Texttable


class UI:
    def __init__(self, game):
        self._game = game

    def _readPlayerGuess(self):
        while True:
            try:
                cmd = input("your guess > ").split(" ")
                if len(cmd) != 2:
                    print("Invalid input")
                else:
                    return (cmd[0].upper(), int(cmd[1]))
            except ValueError:
                print("Invalid coordinates!")

    def _drawPlayerPlane(self, playerBoard):
        while True:
            while True:
                try:
                    cabin = input("choose your cabin (e.g. A 1, h 8) > ").split(" ")
                    if len(cabin) != 2:
                        print("Invalid input")
                    else:
                        cabin = (cabin[0].upper(), int(cabin[1]))
                        break
                except ValueError:
                    print("Invalid coordinates!")

            print("choose the orientation of the plane (up/down/left/right) > ")
            while True:
                orientation = input("> ")
                if orientation in ["up", "down", "left", "right"]:
                    break
                else:
                    print("Invalid input")

            try:
                p = playerBoard.draw_plane(cabin, orientation)
                break
            except ValueError as ve:
                print(ve)

        return p

    def start(self):
        playerBoard = self._game.getPlayerBoard()
        computerBoard = self._game.getComputerBoard()
        playerGuessBoard = self._game.getPlayerGuessBoard()
        computerGuessBoard = self._game.getComputerGuessBoard()

        playerBoard.plane1 = self._drawPlayerPlane(playerBoard)
        print(playerBoard)
        playerBoard.plane2 = self._drawPlayerPlane(playerBoard)

        print(" ")
        print("START GAME")
        '''print(playerBoard)
        print(playerGuessBoard)
        print(computerBoard)
        print(computerGuessBoard)'''

        playerTurn = True
        while playerGuessBoard.isWon() == False and computerGuessBoard.isWon() == False:
            if playerTurn == True:

                t = Texttable(max_width=100)
                row = []
                row.append("YOUR BOARD")
                row.append("YOUR GUESS BOARD")
                t.add_row(row)
                row = []
                row.append(str(playerBoard))
                row.append(str(playerGuessBoard))
                t.add_row(row)
                print(t.draw())

                while True:
                    try:
                        guess = self._readPlayerGuess()
                        self._game.playerGuess(guess[0], guess[1])
                        break
                    except ValueError as e:
                        print(e)
            else:
                self._game.computerGuess()
            playerTurn = not playerTurn

        if playerTurn == False:
            print("Congrats!")
            print("YOUR GUESS BOARD")
            print(playerGuessBoard)
        else:
            print("You were defeated!")
            t = Texttable(max_width=100)
            row = []
            row.append("YOUR BOARD")
            row.append("COMPUTER BOARD")
            t.add_row(row)
            row = []
            row.append(str(playerBoard))
            row.append(str(computerBoard))
            t.add_row(row)
            print(t.draw())


playerBoard = PlayBoard()
computerBoard = PlayBoard()
playerGuessBoard = GuessBoard()
computerGuessBoard = GuessBoard()
ai = ComputerPlayer(computerBoard)
game = Game(playerBoard, computerBoard, playerGuessBoard, computerGuessBoard, ai)
ui = UI(game)
ui.start()
