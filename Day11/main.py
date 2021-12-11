"""
AoC day 11
"""
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def get_input(filename):
    grid = []
    with open(filename, "r") as fh:
        for line in fh:
            grid.append([int(el) for el in line.strip()])

    return grid


def valid_position(i, j, dimension):
    return 0 <= i < dimension and 0 <= j < dimension


def flood_fill(grid, dimension, i, j):
    extend = []
    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]
        if valid_position(new_i, new_j, dimension) and grid[new_i][new_j] < 10:
            grid[new_i][new_j] += 1

            if grid[new_i][new_j] == 10:
                extend.append((new_i, new_j))

    flashes = len(extend)

    for i, j in extend:
        flashes += flood_fill(grid, dimension, i, j)

    return flashes


def apply_step(grid, dimension):
    # phase 1
    points = []
    for i in range(dimension):
        for j in range(dimension):
            grid[i][j] += 1
            if grid[i][j] == 10:
                points.append((i, j))

    flashes = len(points)

    # phase 2
    for i, j in points:
        flashes += flood_fill(grid, dimension, i, j)

    # phase 3
    for i in range(dimension):
        for j in range(dimension):
            if grid[i][j] == 10:
                grid[i][j] = 0

    return flashes


def part1():
    grid = get_input("input.txt")
    steps = 100
    dimension = 10
    flashes = 0

    for _ in range(steps):
        flashes += apply_step(grid, dimension)

    return flashes


def part2():
    grid = get_input("input.txt")
    dimension = 10
    null_grid = [[0] * dimension] * dimension
    step = 0

    while grid != null_grid:
        apply_step(grid, dimension)
        step += 1

    return step


print(part2())
