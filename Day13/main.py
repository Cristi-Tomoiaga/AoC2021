"""
AoC day 13
"""


def get_input(filename):
    points = set()
    commands = []
    finished_points = False
    with open(filename, "r") as fh:
        for line in fh:
            if not finished_points:
                if line.strip() == "":
                    finished_points = True
                else:
                    x, y = [int(el) for el in line.strip().split(",")]
                    points.add((y, x))
            else:
                commands.append(line.strip().split("="))

    return {"points": points, "commands": commands}


def part1():
    data = get_input("input.txt")
    points = data["points"]
    command = data["commands"][0]

    new_points = set()
    removed_points = set()

    if command[0] == "fold along x":
        x = int(command[1])
        for point in points:
            if point[1] > x:
                new_x = 2 * x - point[1]
                new_points.add((point[0], new_x))
                removed_points.add(point)

    elif command[0] == "fold along y":
        y = int(command[1])
        for point in points:
            if point[0] > y:
                new_y = 2 * y - point[0]
                new_points.add((new_y, point[1]))
                removed_points.add(point)

    points = points.difference(removed_points)
    points = points.union(new_points)

    return len(points)


def part2():
    data = get_input("input.txt")
    points = data["points"]

    for command in data["commands"]:
        new_points = set()
        removed_points = set()

        if command[0] == "fold along x":
            x = int(command[1])
            for point in points:
                if point[1] > x:
                    new_x = 2 * x - point[1]
                    new_points.add((point[0], new_x))
                    removed_points.add(point)

        elif command[0] == "fold along y":
            y = int(command[1])
            for point in points:
                if point[0] > y:
                    new_y = 2 * y - point[0]
                    new_points.add((new_y, point[1]))
                    removed_points.add(point)

        points = points.difference(removed_points)
        points = points.union(new_points)

    bottom_x = 0
    bottom_y = 0
    for point in points:
        if point[0] > bottom_y:
            bottom_y = point[0]
        if point[1] > bottom_x:
            bottom_x = point[1]

    for i in range(bottom_y + 1):
        for j in range(bottom_x + 1):
            if (i, j) in points:
                print("▉", end="")
            else:
                print(" ", end="")
        print()


print(part1())
part2()
