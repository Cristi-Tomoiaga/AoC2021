"""
AoC day 15
"""
# import stopwatch

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_input(filename):
    cave = []
    with open(filename, "r") as fh:
        for line in fh:
            cave.append([int(el) for el in line.strip()])

    return cave


def valid_position(i, j, dimension):
    return 0 <= i < dimension and 0 <= j < dimension


def part1():
    cave = get_input("input.txt")
    dimension = len(cave)

    distances = [[0 for _ in range(dimension)] for _ in range(dimension)]
    queue = []
    start = (0, 0)
    end = (dimension - 1, dimension - 1)
    queue.append(start)

    while queue:
        queue.sort(key=lambda pos: distances[pos[0]][pos[1]])
        i, j = queue.pop(0)
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if valid_position(new_i, new_j, dimension) and distances[new_i][new_j] == 0:
                distances[new_i][new_j] = distances[i][j] + cave[new_i][new_j]
                queue.append((new_i, new_j))

    return distances[end[0]][end[1]]


def get_value_at(tile, tile_dimension, i, j):
    value = tile[i % tile_dimension][j % tile_dimension] + i // tile_dimension + j // tile_dimension
    if value > 9:
        value = value % 10 + 1
    return value


def construct_cave(tile, tile_dimension, num_tiles):
    cave = [[0 for _ in range(tile_dimension * num_tiles)] for _ in range(tile_dimension * num_tiles)]

    for x in range(num_tiles):
        for y in range(num_tiles):
            for i in range(tile_dimension):
                for j in range(tile_dimension):
                    value = tile[i][j] + x + y
                    if value > 9:
                        value = value % 10 + 1
                    cave[i + x * tile_dimension][j + y * tile_dimension] = value

    return cave


def part2():
    tile = get_input("input.txt")
    tile_dimension = len(tile)
    num_tiles = 5
    dimension = tile_dimension * num_tiles

    # Memory optimization, does not improve the time

    # cave = construct_cave(tile, tile_dimension, num_tiles)

    distances = [[0 for _ in range(dimension)] for _ in range(dimension)]
    queue = []
    start = (0, 0)
    end = (dimension - 1, dimension - 1)
    queue.append(start)

    while queue:
        queue.sort(key=lambda pos: distances[pos[0]][pos[1]])
        i, j = queue.pop(0)
        for direction in directions:
            new_i = i + direction[0]
            new_j = j + direction[1]
            if valid_position(new_i, new_j, dimension) and distances[new_i][new_j] == 0:
                # distances[new_i][new_j] = distances[i][j] + cave[new_i][new_j]
                distances[new_i][new_j] = distances[i][j] + get_value_at(tile, tile_dimension, new_i, new_j)
                queue.append((new_i, new_j))

    return distances[end[0]][end[1]]


# sw = stopwatch.Stopwatch()
print(part2())
# print(sw.stop())
