"""
AoC day 1
"""


def get_input(file_name):
    result = []
    with open(file_name, "r") as fh:
        for line in fh:
            result.append(int(line))

    return result


def part1():
    data = get_input("input.txt")
    prev = data[0]
    num = 0

    for current in data[1:]:
        if prev < current:
            num += 1

        prev = current

    return num


def part2():
    data = get_input("input.txt")

    windows = [sum(data[i:i+3]) for i in range(len(data) - 2)]

    prev = windows[0]
    num = 0

    for current in windows[1:]:
        if prev < current:
            num += 1

        prev = current

    return num


print(part2())
