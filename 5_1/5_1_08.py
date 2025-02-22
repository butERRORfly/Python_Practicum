class Cell:
    def __init__(self, state):
        self.state = state

    def status(self):
        return self.state


class Checkers:
    def __init__(self):
        self.board = {}
        for row in range(8):
            for col in range(8):
                pos = f"{chr(ord('A') + col)}{8 - row}"
                if (row + col) % 2 == 1:
                    if row < 3:
                        self.board[pos] = Cell('B')
                    elif row > 4:
                        self.board[pos] = Cell('W')
                    else:
                        self.board[pos] = Cell('X')
                else:
                    self.board[pos] = Cell('X')

    def move(self, f, t):
        self.board[t] = self.board[f]
        self.board[f] = Cell('X')

    def get_cell(self, p):
        return self.board[p]

