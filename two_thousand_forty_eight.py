import random
import copy


class TwoThousandFortyEight:
    WINNING_VALUE = 2048

    def __init__(self, board):
        self.board = board  # TODO add validators that board is square (and maybe only size 4 is accepted)
        self.size = len(self.board[0])

    def print_board(self):
        print(*self.board, sep='\n')

    def move_down(self):
        new_board = copy.deepcopy(self.board)
        for i in range(self.size - 1, 0, -1):
            for j in range(self.size):
                if new_board[i][j] > 0:
                    move = 0
                    while i - move - 1 >= 0 and new_board[i - move - 1][j] == 0:
                        move += 1
                    if i - move - 1 >= 0 and new_board[i][j] == new_board[i - move - 1][j]:
                        new_board[i][j] += new_board[i - move - 1][j]
                        new_board[i - move - 1][j] = 0
        for i in range(self.size - 2, -1, -1):
            for j in range(self.size):
                if new_board[i][j] > 0 and new_board[i + 1][j] == 0:
                    move = 1
                    while i + move + 1 < self.size and new_board[i + move + 1][j] == 0:
                        move += 1
                    new_board[i + move][j] = new_board[i][j]
                    new_board[i][j] = 0
        if new_board == self.board:
            raise ValueError('Cant move down, board stays the same')
        return new_board

    def move_up(self):
        new_board = copy.deepcopy(self.board)
        for i in range(self.size - 1):
            for j in range(self.size):
                if new_board[i][j] > 0:
                    move = 0
                    while i + move + 1 < self.size and new_board[i + move + 1][j] == 0:
                        move += 1
                    if i + move + 1 < self.size and new_board[i][j] == new_board[i + move + 1][j]:
                        new_board[i][j] += new_board[i + move + 1][j]
                        new_board[i + move + 1][j] = 0
        for i in range(1, self.size):
            for j in range(self.size):
                if new_board[i][j] > 0 and new_board[i - 1][j] == 0:
                    move = 1
                    while i - move - 1 >= 0 and new_board[i - move - 1][j] == 0:
                        move += 1
                    new_board[i - move][j] = new_board[i][j]
                    new_board[i][j] = 0
        if new_board == self.board:
            raise ValueError('Cant move down, board stays the same')
        return new_board

    def move_right(self):
        new_board = copy.deepcopy(self.board)
        for i in range(self.size - 1, 0, -1):
            for j in range(self.size):
                if new_board[j][i] > 0:
                    move = 0
                    while i - move - 1 >= 0 and new_board[j][i - move - 1] == 0:
                        move += 1
                    if i - move - 1 >= 0 and new_board[j][i] == new_board[j][i - move - 1]:
                        new_board[j][i] += new_board[j][i - move - 1]
                        new_board[j][i - move - 1] = 0
        for i in range(self.size - 2, -1, -1):
            for j in range(self.size):
                if new_board[j][i] > 0 and new_board[j][i + 1] == 0:
                    move = 1
                    while i + move + 1 < self.size and new_board[j][i + move + 1] == 0:
                        move += 1
                    new_board[j][i + move] = new_board[j][i]
                    new_board[j][i] = 0
        if new_board == self.board:
            raise ValueError('Cant move down, board stays the same')
        return new_board

    def move_left(self):
        new_board = copy.deepcopy(self.board)
        for i in range(self.size - 1):
            for j in range(self.size):
                if new_board[j][i] > 0:
                    move = 0
                    while i + move + 1 < self.size and new_board[j][i + move + 1] == 0:
                        move += 1
                    if i + move + 1 < self.size and new_board[j][i] == new_board[j][i + move + 1]:
                        new_board[j][i] += new_board[j][i + move + 1]
                        new_board[j][i + move + 1] = 0
        for i in range(1, self.size):
            for j in range(self.size):
                if new_board[j][i] > 0 and new_board[j][i - 1] == 0:
                    move = 1
                    while i - move - 1 >= 0 and new_board[j][i - move - 1] == 0:
                        move += 1
                    new_board[j][i - move] = new_board[j][i]
                    new_board[j][i] = 0
        if new_board == self.board:
            raise ValueError('Cant move down, board stays the same')
        return new_board

    def has_won(self):
        for i in range(self.size):
            if any(v >= self.WINNING_VALUE for v in self.board[i]):
                return True
        return False

    def add_value_to_random_zeroed_cell(self):
        zeros = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 0:
                    zeros.append((i, j))
        place = random.choice(zeros)
        value = 4 if random.randint(1, 10) == 10 else 2
        self.board[place[0]][place[1]] = value

    def parse_input(self):
        key = input()
        if key == 'a':
            print('Moving left')
            self.board = self.move_left()
        elif key == 'w':
            print('Moving up')
            self.board = self.move_up()
        elif key == 'd':
            print('Moving right')
            self.board = self.move_right()
        elif key == 's':
            print('Moving down')
            self.board = self.move_down()
        else:
            raise ValueError('Wrong input key')

    def has_lost(self):
        for f in [self.move_up, self.move_down, self.move_left, self.move_right]:
            try:
                f()
                return False
            except:
                pass
        return True
