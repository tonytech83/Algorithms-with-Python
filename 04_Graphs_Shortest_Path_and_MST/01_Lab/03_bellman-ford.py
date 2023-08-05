"""
exam: 03. Bellman-Ford
judge: https://judge.softuni.org/Contests/Compete/Index/3464#2

Computes shortest paths from a source node to all the other nodes in a weighted graph.
- weights on edges can be negative
- can detect and report negative cycles
"""
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
target = int(input())

# create two arrays for distances and parents
distance = [float('inf')] * (nodes + 1)
parent = [None] * (nodes + 1)

distance[start] = 0

for _ in range(nodes - 1):
    updated = False

    # iterate through all edges
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue

        new_distance = distance[edge.source] + edge.weight
        # if True updates destination distance and parent
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True

    # if False stop iteration because we don't have any updates on distances
    if not updated:
        break

# detection of negative cycle
for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    print(distance[target])
