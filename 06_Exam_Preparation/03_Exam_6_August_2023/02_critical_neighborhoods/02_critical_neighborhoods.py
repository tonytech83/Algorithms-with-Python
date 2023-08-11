"""
exam: 02. Critical Neighborhoods
judge: https://judge.softuni.org/Contests/Practice/Index/4044#1

Solution with Bellman-Ford algorithm without detection of negative cycle
"""
from collections import deque

roads_count = int(input())

graph = []
towns = set()

for _ in range(roads_count):
    first, second, distance = input().split(' - ')
    distance = int(distance)
    graph.append((first, second, distance))
    graph.append((second, first, distance))
    towns.add(first)
    towns.add(second)

closed_roads = set(tuple(closed_road.split("-")) for closed_road in input().split(","))
start = input()
end = input()

distances = {x: float('inf') for x in towns}
parent = {x: None for x in towns}

distances[start] = 0

for _ in range(len(towns) - 1):

    for source, destination, distance in graph:
        if (source, destination) in closed_roads or (destination, source) in closed_roads:
            continue

        if distances[source] == float('inf'):
            continue

        new_distance = distances[source] + distance

        if new_distance < distances[destination]:
            distances[destination] = new_distance
            parent[destination] = source


def reconstruct_path(parent, node):
    current_path = deque()

    while node is not None:
        current_path.appendleft(node)
        node = parent[node]

    return current_path


path = reconstruct_path(parent, end)
if len(path) > 1:
    print(*path, sep=' - ')
    print(distances[end])
