"""
AoC day 9
"""
# directions on the matrix (N, E, S, W)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_input(filename):
    heightmap = []
    with open(filename, "r") as fh:
        for line in fh:
            heightmap.append([int(el) for el in line.strip()])

    return heightmap


def is_valid_position(i, j, height, width):
    return 0 <= i < height and 0 <= j < width


def get_low_points(heightmap, height, width):
    low_points = []
    for i in range(height):
        for j in range(width):
            is_lower = True

            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]

                if is_valid_position(new_i, new_j, height, width) and heightmap[i][j] >= heightmap[new_i][new_j]:
                    is_lower = False

            if is_lower:
                low_points.append((i, j))

    return low_points


def part1():
    heightmap = get_input("input.txt")
    risk_levels = 0
    height = len(heightmap)
    width = len(heightmap[0])

    low_points = get_low_points(heightmap, height, width)
    for low_point in low_points:
        i = low_point[0]
        j = low_point[1]
        risk_levels += heightmap[i][j] + 1

    return risk_levels


def flood_fill(heightmap, i, j, height, width):
    count = 1
    heightmap[i][j] = 9  # block this position

    for direction in directions:
        new_i = i + direction[0]
        new_j = j + direction[1]

        if is_valid_position(new_i, new_j, height, width) and heightmap[new_i][new_j] != 9:
            count += flood_fill(heightmap, new_i, new_j, height, width)

    return count


def part2():
    heightmap = get_input("input.txt")
    height = len(heightmap)
    width = len(heightmap[0])

    low_points = get_low_points(heightmap, height, width)
    basin_sizes = []
    for low_point in low_points:
        i = low_point[0]
        j = low_point[1]

        basin_size = flood_fill(heightmap, i, j, height, width)
        basin_sizes.append(basin_size)

    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


print(part2())
