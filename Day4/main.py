"""
AoC day 4
"""


class Board:
    DIM = 5

    def __init__(self, numbers):
        self.__numbers = numbers
        self.__checked = [[False for _ in range(Board.DIM)] for _ in range(Board.DIM)]
        self.__finished = False

    def check(self, number):
        for i in range(Board.DIM):
            for j in range(Board.DIM):
                if self.__numbers[i][j] == number:
                    self.__checked[i][j] = True
                    return

    def has_won(self):
        for i in range(Board.DIM):
            win = True
            for j in range(Board.DIM):
                if not self.__checked[i][j]:
                    win = False
            if win:
                self.__finished = True
                return True

        for j in range(Board.DIM):
            win = True
            for i in range(Board.DIM):
                if not self.__checked[i][j]:
                    win = False
            if win:
                self.__finished = True
                return True

        return False

    def is_finished(self):
        return self.__finished

    def get_score(self):
        score = 0
        for i in range(Board.DIM):
            for j in range(Board.DIM):
                if not self.__checked[i][j]:
                    score += self.__numbers[i][j]

        return score


class Bingo:
    def __init__(self, filename):
        self.__get_input(filename)

    def __get_input(self, filename):
        with open(filename, "r") as fh:
            self.__called_numbers = [int(num) for num in fh.readline().strip().split(",")]

            self.__boards = []
            done = False
            while not done:
                numbers = []
                fh.readline().strip()  # read the blank line
                line = fh.readline().strip()
                if line == "":
                    done = True
                else:
                    numbers.append([int(num) for num in line.split(" ") if num != ""])
                    for _ in range(Board.DIM - 1):
                        numbers.append([int(num) for num in fh.readline().strip().split(" ") if num != ""])

                    self.__boards.append(Board(numbers))

    def play_first(self):
        for num in self.__called_numbers:
            for board in self.__boards:
                board.check(num)
                if board.has_won():
                    return board.get_score() * num

    def play_last(self):
        scores = []
        for num in self.__called_numbers:
            for board in self.__boards:
                if not board.is_finished():
                    board.check(num)
                    if board.has_won():
                        scores.append(board.get_score() * num)

        return scores[-1]


game = Bingo("input.txt")
print(game.play_last())
