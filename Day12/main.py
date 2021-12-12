"""
AoC day 12
"""


def get_input(filename):
    graph = {}
    with open(filename, "r") as fh:
        for line in fh:
            nodes = line.strip().split("-")
            node1 = nodes[0]
            node2 = nodes[1]

            if node1 not in graph:
                graph[node1] = {node2}
            else:
                graph[node1].add(node2)

            if node2 not in graph:
                graph[node2] = {node1}
            else:
                graph[node2].add(node1)

    return graph


def dfs(graph, src, dest, visited):
    if src.islower():
        visited[src] = True

    number = 0

    if src == dest:
        number += 1
    else:
        for node in graph[src]:
            if not visited[node]:
                number += dfs(graph, node, dest, visited)

    visited[src] = False

    return number


def dfs2(graph, curr, src, dest, visited, used):
    if curr.islower():
        visited[curr] += 1
        if visited[curr] == 2:
            used = True

    number = 0

    if curr == dest:
        number += 1
    else:
        maximum = 2 if not used else 1
        for node in graph[curr]:
            if visited[node] < maximum and node != src:
                number += dfs2(graph, node, src, dest, visited, used)

    visited[curr] -= 1

    return number


def part1():
    graph = get_input("input.txt")
    src = "start"
    dest = "end"
    visited = {key: False for key in graph}

    return dfs(graph, src, dest, visited)


def part2():
    graph = get_input("input.txt")
    src = "start"
    dest = "end"
    visited = {key: 0 for key in graph}

    return dfs2(graph, src, src, dest, visited, False)


print(part2())
