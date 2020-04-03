from game import *
from computer import *
from board import *


class UI:
    def __init__(self, g):
        self._game = g

    def read_player_move(self):
        while True:
            command = input("your move: ")
            command = command.split(" ")
            if len(command) != 3:
                print("Invalid command")
                continue
            try:
                x = int(command[0])
                y = int(command[1])
                symbol = command[2]
                break
            except ValueError as ve:
                print(ve)
        return x, y, symbol

    def start(self):
        board = self._game.get_board()
        print(board)
        playerTurn = False
        while board.isWon() == False and board.isFull() == False:
            if playerTurn == True:
                while True:
                    try:
                        move = self.read_player_move()
                        self._game.playerMove(move[0], move[1], move[2])
                        break
                    except ValueError as ve:
                        print(ve)
            else:
                self._game.computerMove()
                print(board)
            playerTurn = not playerTurn
        if board.isFull() == True:
            print("CONGRATS!")
        else:
            print(board)
            print("GAME OVER! YOU LOST!")

b = Board()
comp = Computer()
g = Game(b, comp)
ui = UI(g)

ui.start()