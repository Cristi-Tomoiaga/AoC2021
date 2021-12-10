"""
AoC day 10
"""


def get_input(filename):
    lines = []
    with open(filename, "r") as fh:
        for line in fh:
            lines.append(line.strip())

    return lines


def part1():
    lines = get_input("input.txt")
    score = 0
    scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}

    for line in lines:
        stack = []
        for symbol in line:
            if symbol in ["(", "[", "{", "<"]:
                stack.append(symbol)
            elif stack[-1] == pairs[symbol]:
                stack.pop()
            else:  # error case
                score += scores[symbol]
                break

    return score


def part2():
    lines = get_input("input.txt")
    score_list = []
    scores = {")": 1, "]": 2, "}": 3, ">": 4}
    pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    closing = {"(": ")", "[": "]", "{": "}", "<": ">"}

    for i, line in enumerate(lines):
        stack = []
        for symbol in line:
            if symbol in ["(", "[", "{", "<"]:
                stack.append(symbol)
            elif stack[-1] == pairs[symbol]:
                stack.pop()
            else:  # error case
                lines[i] = ""  # "delete" incorrect lines
                stack = []
                break

        if len(stack) > 0:  # incomplete line
            completion = ""
            for symbol in reversed(stack):
                completion += closing[symbol]

            score = 0
            for symbol in completion:
                score = score * 5 + scores[symbol]
            score_list.append(score)

    score_list.sort()
    return score_list[len(score_list) // 2]


print(part2())
