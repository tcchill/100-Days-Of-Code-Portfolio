

class Board():
    def __init__(self):
        self.cells = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def make_move(self, row, column, mark):
        self.cells[row][column] = mark

    def check_result(self, mark):
        for row in range(3):
            if all(self.cells[row][column] == mark for column in range(3)):
                return True
        for column in range(3):
            if all(self.cells[row][column] == mark for row in range(3)):
                return True

        if all(self.cells[i][i] == mark for i in range(3)):
            return True

        if all(self.cells[i][2 - i] == mark for i in range(3)):
            return True

        for row in range(3):
            for column in range(3):
                if self.cells[row][column] == " ":
                    return False
        return 'Draw'

    def reset_board(self):
        self.cells = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

class Logic():
    def __init__(self):
        self.mark = 'X'
        self.board = Board()
        self.game_over = False

    def switch_turn(self):
        self.mark = 'O' if self.mark == 'X' else 'X'


