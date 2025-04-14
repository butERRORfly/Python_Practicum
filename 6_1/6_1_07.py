import numpy as np


def make_board(size):
    board = np.zeros((size, size), dtype=np.int8)
    board[::2, ::2] = 1
    board[1::2, 1::2] = 1
    return board
