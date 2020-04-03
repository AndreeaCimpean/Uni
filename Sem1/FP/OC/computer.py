import random
from board import *


class Computer:
    def calculate_move_a(self, board):
        while True:
            i = random.randint(1, 6)
            j = random.randint(1, 6)
            if board.get_cell(i, j) == 0:
                break
        symbol = random.choice(["x", "o"])
        return i, j, symbol


    def calculate_move_b(self, board):
        auxiliary_board = Board()
        for i in range(1, 6):
            for j in range(1, 6):
                auxiliary_board.set_cell(i, j, board.get_cell(i, j))

        for i in range(1, 6):
            for j in range(1, 6):
                if auxiliary_board.get_cell(i, j) == 0:
                    auxiliary_board.set_cell(i, j, 1)
                    if auxiliary_board.isWon():
                        return i, j, "x"
                    else:
                        auxiliary_board.set_cell(i, j, -1)
                        if auxiliary_board.isWon():
                            return i, j, "o"
                    auxiliary_board.set_cell(i, j, 0)

    def calculate_move_c(self, board):
        symbol = board.max_symbol()
        move = [0, 0]
        if symbol < 0:
            maxim = 1
            for i in range(1, 6):
                for j in range(1, 6):
                    s = board.neighbours_sum(i, j)
                    if board.get_cell(i, j) == 0 and s <= 0:
                        if maxim > s:
                            maxim = s
                            move[0] = i
                            move[1] = j
            return move[0], move[1], "o"
        else:
            maxim = -1
            for i in range(1, 6):
                for j in range(1, 6):
                    s = board.neighbours_sum(i, j)
                    if board.get_cell(i, j) == 0 and s >= 0:
                        if maxim < s:
                            maxim = s
                            move[0] = i
                            move[1] = j
        return move[0], move[1], "x"

    def calculate_move(self, board):
        ok = 0
        for i in range(1, 6):
            for j in range(1, 6):
                if board.get_cell(i, j) != 0:
                    ok = 1
                    break
        if ok == 0:
            return self.calculate_move_a(board)
        move = self.calculate_move_b(board)
        if move != None:
            return move
        move = self.calculate_move_c(board)
        return move
