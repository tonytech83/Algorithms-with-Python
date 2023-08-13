from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, distance, is_critical):
        self.first = first
        self.second = second
        self.distance = distance
        self.is_critical = is_critical

    def __gt__(self, other):
        return self.distance > other.distance


roads = int(input())

graph = {}
forest = set()
total_distance = 0

for _ in range(roads):
    is_critical = False
    line = input().split()
    first, second, distance = line[0], line[1], int(line[2])

    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []

    if 'critical' in line:
        is_critical = True

    edge = Edge(first, second, distance, is_critical)
    graph[first].append(edge)
    graph[second].append(edge)

for key in graph:
    for edge in graph[key]:
        if edge.is_critical and (edge.first not in forest or edge.second not in forest):
            forest.add(edge.first)
            forest.add(edge.second)
            total_distance += edge.distance

pq = PriorityQueue()
visited = set(forest)

for city in forest:
    for edge in graph[city]:
        if not edge.is_critical:
            pq.put(edge)

while not pq.empty():
    current_edge = pq.get()
    next_city = None

    if current_edge.first in visited and current_edge.second in visited:
        continue

    if current_edge.first in visited:
        next_city = current_edge.second
    else:
        next_city = current_edge.first

    visited.add(next_city)

    for edge in graph[next_city]:
        pq.put(edge)

    total_distance += current_edge.distance

print(total_distance)
