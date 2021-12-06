"""
AoC day 6
"""


def get_input(filename):
    timers = [0] * 9
    with open(filename, "r") as fh:
        data = [int(day) for day in fh.readline().strip().split(",")]

        for timer in data:
            timers[timer] += 1

        return timers


def simulate(num_days):
    timers = get_input("input.txt")

    for _ in range(num_days):  # simulate for num_days
        new_timers = timers[0]
        timers[0] = 0
        for i in range(1, len(timers)):
            timers[i - 1] += timers[i]
            timers[i] = 0

        timers[6] += new_timers
        timers[8] += new_timers

    return sum(timers, 0)


def part1():
    return simulate(80)


def part2():
    return simulate(256)


print(part2())
