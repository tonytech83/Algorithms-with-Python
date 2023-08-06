"""
exam: 01. Distance Between Vertices
judge: https://judge.softuni.org/Contests/Practice/Index/3465#0
"""

from collections import deque


def find_parent_by_node(start, end, graph):
    visited = [False] * len(graph)

    parent = [None] * len(graph)

    visited[start] = True
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node == end:
            break

        for child in graph[node]:
            if visited[child]:
                continue

            visited[child] = True
            queue.append(child)
            parent[child] = node

    return parent


def calculate_path(parent, end):
    path_weight = 0
    node = end

    while node is not None:
        path_weight += 1
        node = parent[node]

    return path_weight - 1


nodes_count = int(input())
pairs_count = int(input())

graph = []
[graph.append([]) for _ in range(nodes_count + 1)]

# read graph
for _ in range(nodes_count):
    line = input().split(':')
    source = int(line[0])
    destinations = [int(x) for x in line[1].split()] if line[1] else []

    graph[source] = destinations

# read pairs
for _ in range(pairs_count):
    start, end = [int(x) for x in input().split('-')]

    parent = find_parent_by_node(start, end, graph)

    if parent[end] is None:
        print(f'{{{start}, {end}}} -> -1')

    else:
        path_size = calculate_path(parent, end)
        print(f'{{{start}, {end}}} -> {path_size}')
