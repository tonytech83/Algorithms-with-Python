"""
exam: 04. Undefined
judge: https://judge.softuni.org/Contests/Practice/Index/3465#3

Solution with Bellman-Ford algorithm
"""
from collections import deque


def reconstruct_path(parent, node):
    current_path = deque()

    while node is not None:
        current_path.appendleft(node)
        node = parent[node]

    return current_path


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append((source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start] = 0

parent = [None] * (nodes + 1)

for _ in range(nodes - 1):
    updated = False

    for source, destination, weight in graph:
        if distance[source] == float('inf'):
            continue

        new_distance = distance[source] + weight

        if new_distance < distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source
            updated = True

    if not updated:
        break

for source, destination, weight in graph:
    new_distance = distance[source] + weight
    if new_distance < distance[destination]:
        print('Undefined')
        break
else:
    path = reconstruct_path(parent, target)

    print(*path, sep=' ')
    print(distance[target])
