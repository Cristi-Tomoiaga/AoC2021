"""
AoC day 3
"""


def get_input(filename):
    nums = []
    with open(filename, "r") as fh:
        for line in fh:
            nums.append(line.strip())

    return nums


def part1():
    nums = get_input("input.txt")
    num_len = len(nums[0])
    gamma = list("0" * num_len)
    epsilon = list("0" * num_len)

    for i in range(num_len):
        ones = 0
        zeros = 0
        for num in nums:
            if num[i] == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            gamma[i] = "0"
            epsilon[i] = "1"
        else:
            gamma[i] = "1"
            epsilon[i] = "0"

    gamma = int("".join(gamma), 2)
    epsilon = int("".join(epsilon), 2)

    power_consumption = gamma * epsilon
    return power_consumption


def get_oxygen(nums):
    num_len = len(nums[0])

    for i in range(num_len):
        ones = 0
        zeros = 0
        for num in nums:
            if num[i] == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            nums = list(filter(lambda x: x[i] == "0", nums))
        else:
            nums = list(filter(lambda x: x[i] == "1", nums))

        if len(nums) == 1:
            return int(nums[0], 2)


def get_co2(nums):
    num_len = len(nums[0])

    for i in range(num_len):
        ones = 0
        zeros = 0
        for num in nums:
            if num[i] == "0":
                zeros += 1
            else:
                ones += 1

        if ones < zeros:
            nums = list(filter(lambda x: x[i] == "1", nums))
        else:
            nums = list(filter(lambda x: x[i] == "0", nums))

        if len(nums) == 1:
            return int(nums[0], 2)


def part2():
    nums = get_input("input.txt")

    oxygen = get_oxygen(nums[:])
    co2 = get_co2(nums[:])

    life_support = oxygen * co2
    return life_support


print(part2())
