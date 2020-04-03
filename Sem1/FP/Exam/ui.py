from board import *
from game import *


class UI:
    def __init__(self, game):
        self._game = game

    def read_command(self):
        command = input("your command:")
        command = command.split(" ")
        if len(command) == 1:
            if command[0] != "cheat":
                raise ValueError("Not a valid command!")
            return command[0]
        else:
            if command[0] != "fire" and command[0] != "warp":
                raise ValueError("Not a valid command")
            coordinate = command[1]
            if coordinate[0] < 'A' or coordinate[0] > 'H' or int(coordinate[1]) < 1 or int(coordinate[1]) > 8:
                raise ValueError("Not a valid command")
            return command[0], coordinate[0], int(coordinate[1])

    def start(self):
        board = self._game.get_board()
        #print(board)
        while board.is_won() == False and board.is_lost() == False:
            print(self._game.get_board_for_player())
            #print(board)
            while True:
                try:
                    command = self.read_command()
                    if command == "cheat":
                        print(board)
                    elif command[0] == "fire":
                        self._game.fire(command[1], command[2])
                    elif command[0] == "warp":
                        self._game.warp(command[1], command[2])
                    break
                except ValueError as ve:
                    print(ve)
        if board.is_won() == True:
            print("CONGRATS")
        else:
            print("GAME OVER !")

board = Board()
game = Game(board)
ui = UI(game)
ui.start()