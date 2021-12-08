"""
AoC day 8
"""
segments = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]  # segments for each digit

# translations in terms of basis (won't use 1, 4, 7, 8 here)
translations = [[0, 2, 3], [], [2, 3], [0, 2], [], [1, 2], [1, 2, 3], [], [], [0, 1, 2]]


def get_input(filename):
    entries = []
    with open(filename, "r") as fh:
        for line in fh:
            data = line.strip().split(" | ")

            signal_patterns = data[0].strip().split(" ")
            output_value = data[1].strip().split(" ")
            entries.append({"patterns": signal_patterns, "output": output_value})

    return entries


def part1():
    unique_digits = 0
    entries = get_input("input.txt")

    for entry in entries:
        for digit in entry["output"]:
            if len(digit) in [segments[1], segments[4], segments[7], segments[8]]:
                unique_digits += 1

    return unique_digits


def get_basis(patterns):
    one = ""
    four = ""
    seven = ""
    eight = ""

    for digit in patterns:
        if len(digit) == segments[1]:
            one = digit
        elif len(digit) == segments[4]:
            four = digit
        elif len(digit) == segments[7]:
            seven = digit
        elif len(digit) == segments[8]:
            eight = digit

    set_one = set(one)
    set_four = set(four)
    set_seven = set(seven)
    set_eight = set(eight)
    four = "".join(set_four.difference(set_one))  # S4 \ S1
    seven = "".join(set_seven.difference(set_one))  # S7 \ S1
    eight = "".join(set_eight.difference(set_one.union(set_four, set_seven)))  # S8 \ union(S1, S4, S7)
    one = "".join(set_one)  # S1

    return one, four, seven, eight


def get_digit(digit, basis):
    # base cases
    if len(digit) == segments[1]:
        return 1
    if len(digit) == segments[4]:
        return 4
    if len(digit) == segments[7]:
        return 7
    if len(digit) == segments[8]:
        return 8

    # general case
    translated_digit = []
    for i, value in enumerate(basis):
        if set(value).issubset(set(digit)):
            translated_digit.append(i)

    return translations.index(translated_digit)


def part2():
    result = 0
    entries = get_input("input.txt")

    for entry in entries:
        basis = get_basis(entry["patterns"])
        output = 0
        for digit in entry["output"]:
            output = output * 10 + get_digit(digit, basis)

        result += output

    return result


print(part2())
