# Should use Bellman-Ford algorithm, because we can have negative weight and negative cycles
from collections import deque


def find_path(parent, node):
    result = deque()
    while node is not None:
        result.appendleft(node)
        node = parent[node]
    return result


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split()]
    graph.append((first, second, weight))

source = int(input())
destination = int(input())

distance = [(float('inf'))] * (nodes + 1)
distance[source] = 0

parent = [None] * (nodes + 1)

# Bellman-Ford algorithm
for _ in range(nodes - 1):
    # walk thought any edge in our graph
    for first, second, weight in graph:
        if distance[first] == float('inf'):
            continue
        new_distance = distance[first] + weight
        if new_distance < distance[second]:
            distance[second] = new_distance
            # when we have better distance, we change the child parent to first node
            parent[second] = first

# Bellman-Ford second stage, searching for negative cycles
for first, second, weight in graph:
    new_distance = distance[first] + weight
    if new_distance < distance[second]:
        print('Undefined')
        break

else:
    path = find_path(parent, destination)

    print(*path, sep=' ')
    print(distance[destination])
