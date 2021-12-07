"""
AoC day 7
"""


def get_input(filename):
    with open(filename, "r") as fh:
        data = list(map(int, fh.readline().strip().split(",")))
        max_pos = max(data)

        positions = [0] * (max_pos + 1)
        for pos in data:
            positions[pos] += 1

        return positions


def part1():
    minimum = -1
    positions = get_input("input.txt")

    for i in range(len(positions)):  # check possible align positions
        fuel = 0
        for j in range(len(positions)):
            fuel += positions[j] * abs(i - j)

        if minimum < 0 or fuel < minimum:
            minimum = fuel

    return minimum


def part2():
    minimum = -1
    positions = get_input("input.txt")

    for i in range(len(positions)):  # check possible align positions
        fuel = 0
        for j in range(len(positions)):
            fuel += positions[j] * ((abs(i - j) * (abs(i - j) + 1)) // 2)

        if minimum < 0 or fuel < minimum:
            minimum = fuel

    return minimum


print(part2())
