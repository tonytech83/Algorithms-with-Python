"""
exam: 03. Gateways
judge: https://judge.softuni.org/Contests/Practice/Index/3623#2
"""
from collections import deque


def find_parent_by_node(start, end, graph):
    visited = [False] * len(graph)
    parents = [None] * len(graph)

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
            parents[child] = node

    return parents


def reconstruct_path(parents, end):
    path = deque()
    node = end

    while node is not None:
        path.appendleft(node)
        node = parents[node]

    return path


nodes = int(input())
connections = int(input())

graph = [[] for _ in range(nodes + 1)]

for _ in range(connections):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start = int(input())
end = int(input())

parents = find_parent_by_node(start, end, graph)
path = reconstruct_path(parents, end)

if len(path) > 1:
    print(*path, sep=' ')
