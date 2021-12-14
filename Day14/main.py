"""
AoC day 14
"""


def get_input(filename):
    data = {}
    with open(filename, "r") as fh:
        data["template"] = fh.readline().strip()
        fh.readline().strip()  # reads the empty file

        data["substitutions"] = {}
        for line in fh:
            substitution = line.strip().split(" -> ")
            data["substitutions"][substitution[0]] = substitution[1]

    return data


def part1():
    data = get_input("input.txt")
    template = data["template"]
    substitutions = data["substitutions"]

    steps = 10
    for _ in range(steps):
        new_template = template[0]
        for i in range(len(template) - 1):
            new_template += substitutions[template[i:i+2]] + template[i+1]

        template = new_template

    freq = {}
    for char in template:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 0

    char_maximum = max(freq.keys(), key=lambda el: freq[el])
    char_minimum = min(freq.keys(), key=lambda el: freq[el])

    return freq[char_maximum] - freq[char_minimum]


def part2():
    data = get_input("input.txt")
    template = data["template"]
    substitutions = data["substitutions"]

    prev_polymer = {k: 0 for k in substitutions.keys()}
    for i in range(len(template) - 1):
        prev_polymer[template[i:i+2]] += 1

    freq = {}
    for el in template:
        if el not in freq:
            freq[el] = 0
        freq[el] += 1

    steps = 40
    for _ in range(steps):
        curr_polymer = {k: 0 for k in substitutions.keys()}

        for k in prev_polymer:
            curr_polymer[k[0] + substitutions[k]] += prev_polymer[k]
            curr_polymer[substitutions[k] + k[1]] += prev_polymer[k]

            if substitutions[k] not in freq:
                freq[substitutions[k]] = 0
            freq[substitutions[k]] += prev_polymer[k]

        prev_polymer = curr_polymer

    char_maximum = max(freq.keys(), key=lambda elem: freq[elem])
    char_minimum = min(freq.keys(), key=lambda elem: freq[elem])

    return freq[char_maximum] - freq[char_minimum]


print(part2())
