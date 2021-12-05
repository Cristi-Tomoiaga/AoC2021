"""
AoC day 2
"""


class Submarine:
    IN_FILE = "input.txt"

    def __init__(self):
        self.__h_pos = 0
        self.__depth = 0
        self.__aim = 0

        self.__commands = Submarine.parse_input(Submarine.IN_FILE)
        self.__options = {
            "forward": self.__forward,
            "down": self.__down,
            "up": self.__up
        }

    @staticmethod
    def parse_input(file):
        cmds = []
        with open(file, "r") as fh:
            for line in fh:
                elements = line.strip().split(" ")
                cmds.append([elements[0], int(elements[1])])

        return cmds

    def __forward(self, x):
        self.__h_pos += x
        self.__depth += self.__aim * x

    def __down(self, x):
        self.__aim += x

    def __up(self, x):
        self.__aim -= x

    def execute_commands(self):
        for cmd in self.__commands:
            option = cmd[0]
            argument = cmd[1]
            self.__options[option](argument)

    def get_depth(self):
        return self.__depth

    def get_h_pos(self):
        return self.__h_pos


def run():
    sub = Submarine()
    sub.execute_commands()
    print(sub.get_depth() * sub.get_h_pos())


run()
